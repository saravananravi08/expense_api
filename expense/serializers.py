from rest_framework import serializers
from expense import models


class AddExpenseSerializer(serializers.Serializer):
    name = serializers.CharField()
    employee_id = serializers.CharField()
    email = serializers.EmailField()
    type = serializers.CharField()
    amount = serializers.IntegerField()
    description = serializers.CharField()
    approver = serializers.CharField()


class GetExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = [
            "id",
            "name",
            "employee_id",
            "email",
            "type",
            "amount",
            "description",
            "approved",
            "approver",
            "message",
            "created_at",
        ]


class VerifyExpenseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    approved = serializers.BooleanField()
    message = serializers.CharField(required=False)
