from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Expense(models.Model):
    name = models.TextField()
    employee_id = models.CharField(max_length=1024)
    email = models.TextField()
    type = models.TextField()
    amount = models.IntegerField()
    description = models.TextField()
    approver = models.TextField(default="")
    approved = models.BooleanField(default=None, null=True)
    message = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ExpenseFlow(models.Model):
    name = models.TextField()
    description = models.CharField(max_length=1024)
    category_type = models.TextField()
    approval_type = models.TextField()
    condition = models.TextField(null=True)
    amount = models.IntegerField()
    approvers = models.JSONField(null=True, blank=True)
    alert_type = models.TextField()
    alert_recipients = models.JSONField(null=True, blank=True)
    content = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
