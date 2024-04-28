from django.db import models

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
