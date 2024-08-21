from rest_framework import serializers
from .models import Employee
from django.core.validators import RegexValidator, EmailValidator

class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    employee_regNo = serializers.CharField(
        max_length=255,
        validators=[
            RegexValidator(regex=r'^\w+$', message="Registration number must be alphanumeric.")
        ]
    )
    employee_name = serializers.CharField(max_length=255)
    employee_email = serializers.EmailField(
        validators=[EmailValidator(message="Please enter a valid email address.")]
    )
    employee_mobile = serializers.CharField(
        max_length=15, 
        required=False, 
        allow_null=True, 
        validators=[
            RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Please enter a valid phone number.")
        ]
    )
    created_at = serializers.DateTimeField(read_only=True)

    def validate_employee_regNo(self, value):
        # Custom validation logic for registration number
        instance = self.instance
        if instance:
            # Exclude the current instance from the check
            if Employee.objects.filter(employee_regNo=value).exclude(id=instance.id).exists():
                raise serializers.ValidationError("Employee ID already exists.")
        else:
            if Employee.objects.filter(employee_regNo=value).exists():
                raise serializers.ValidationError("Employee ID already exists.")
        return value

    def validate_employee_email(self, value):
        # Custom validation logic for email
        instance = self.instance
        if instance:
            # Exclude the current instance from the check
            if Employee.objects.filter(employee_email=value).exclude(id=instance.id).exists():
                raise serializers.ValidationError("This email address is already in use.")
        else:
            if Employee.objects.filter(employee_email=value).exists():
                raise serializers.ValidationError("This email address is already in use.")
        return value

    def validate(self, data):
        # Additional validation logic for mobile
        if 'employee_mobile' in data and not data['employee_mobile']:
            data['employee_mobile'] = None
        return data

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.employee_regNo = validated_data.get('employee_regNo', instance.employee_regNo)
        instance.employee_name = validated_data.get('employee_name', instance.employee_name)
        instance.employee_email = validated_data.get('employee_email', instance.employee_email)
        instance.employee_mobile = validated_data.get('employee_mobile', instance.employee_mobile)
        instance.save()
        return instance
