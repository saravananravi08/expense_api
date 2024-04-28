from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request
from expense import serializers
from rest_framework.viewsets import ModelViewSet
from expense import models

# Create your views here.


class GetExpenseAPI(APIView):
    def get(self, request: Request):
        expense_data = models.Expense.objects.all()
        serializer = serializers.GetExpenseSerializer(expense_data, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class AddExpenseAPI(APIView):

    def post(self, request: Request, format=None):
        serializer = serializers.AddExpenseSerializer(data=request.data)
        if serializer.is_valid():

            created_data = models.Expense.objects.create(
                name=serializer.validated_data["name"],
                employee_id=serializer.validated_data["employee_id"],
                email=serializer.validated_data["email"],
                type=serializer.validated_data["type"],
                amount=serializer.validated_data["amount"],
                description=serializer.validated_data["description"],
                approver=serializer.validated_data["approver"],
            )
            created_data.save()
            return Response(
                {"data": "expense added successfully"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyExpense(APIView):

    def put(self, request: Request, format=None):
        serializer = serializers.VerifyExpenseSerializer(data=request.data)
        if serializer.is_valid():
            id = serializer.validated_data["id"]
            approved = serializer.validated_data["approved"]

            message = ""
            if "message" in serializer.validated_data:
                message = serializer.validated_data["message"]

            filter_data = models.Expense.objects.filter(id=id)
            update_data = filter_data.update(approved=approved, message=message)
            email = filter_data.get().email
            print(f"user_email : {email} , email_content : {message}")
            return Response({"data": "update successfull"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
