from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # Include the `id` field
    employee_regNo = serializers.CharField(max_length=255)
    employee_name = serializers.CharField(max_length=255)
    employee_email = serializers.EmailField()
    employee_mobile = serializers.CharField(max_length=255, required=False, allow_null=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.employee_regNo = validated_data.get('employee_regNo', instance.employee_regNo)
        instance.employee_name = validated_data.get('employee_name', instance.employee_name)
        instance.employee_email = validated_data.get('employee_email', instance.employee_email)
        instance.employee_mobile = validated_data.get('employee_mobile', instance.employee_mobile)
        instance.save()
        return instance
