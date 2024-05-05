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


class AddExpenseWorkFlowSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    category_type = serializers.CharField(required=True)
    approval_type = serializers.CharField(required=True)
    condition = serializers.CharField(required=False)
    amount = serializers.IntegerField(required=False)
    approvers = serializers.ListField(child=serializers.CharField(required=True))
    alert_type = serializers.CharField(required=True)
    alert_recipients = serializers.ListField(child=serializers.CharField(required=True))
    content = serializers.CharField(required=True)


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
