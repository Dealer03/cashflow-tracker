from django.shortcuts import render, redirect
from django.views import View
from .forms import TransactionForm
from .models import Transaction



class CreateTransactionView(View):
    # Implementation for manual entry
