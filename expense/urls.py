from django.urls import path
from expense import views

urlpatterns = [
    path("add_expense", views.AddExpenseAPI.as_view()),
    path("get_expense", views.GetExpenseAPI.as_view()),
    path("verify_expense", views.VerifyExpense.as_view()),
]
