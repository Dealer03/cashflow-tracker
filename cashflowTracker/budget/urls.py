from django.urls import path
from .views import SignUpView
from .views import CreateBudgetEntryView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("create_budget/", CreateBudgetEntryView.as_view(),
         name="create_budget_entry"),

]
