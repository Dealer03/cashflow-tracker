from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import View

from .forms import BudgetForm
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CreateBudgetEntryView(View):
    template_name = "create-budget.html"

    def get(self, request, *args, **kwargs):
        form = BudgetForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = BudgetForm(request.POST)
        if form.is_valid():
            # Process the form data and save it to the database
            budget_entry = form.save(commit=False)
        # Assuming you have a user associated with the budget entry
            budget_entry.user = request.user
            budget_entry.save()
        # Redirect to the home page or another appropriate view
            return redirect('home')
        return render(request, self.template_name, {'form': form})
