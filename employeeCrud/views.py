# from rest_framework import generics
from rest_framework.response import Response
from .serializer import EmployeeSerializer
from .models import Employee

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import NotFound


# class EmployeeCreateApi(generics.CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
class EmployeeCreateApi(APIView):
    def post(self, request):
        # Step 1: Deserialize the incoming data using the EmployeeSerializer
        serializer = EmployeeSerializer(data=request.data)
        
        # Step 2: Validate the data
        if serializer.is_valid():
            # Step 3: Save the new Employee object
            serializer.save()
            
            # Step 4: Return a success response with the created object
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Step 5: Return an error response if validation fails
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeeApi(generics.ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
class EmployeeApi(APIView):
    def get(self, request):
        try:
            # Query all Employee objects
            employees = Employee.objects.all()
            
            # Serialize the Employee objects
            serializer = EmployeeSerializer(employees, many=True)
            
            # Return the serialized data with a success status
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            # Log the exception or handle it appropriately
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

class EmployeeUpdateApi(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class EmployeeDeleteApi(generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
class EmployeeDeleteApi(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise NotFound(detail="Employee not found")

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response({"detail": "Employee deleted successfully"}, status=status.HTTP_200_OK)