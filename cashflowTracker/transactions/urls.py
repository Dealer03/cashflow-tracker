from django.urls import path
from .views import ImportCSVView, CreateTransactionView

urlpatterns = [
    path('import-csv/', ImportCSVView.as_view(), name='import_csv'),
    path('create-transaction/', CreateTransactionView.as_view(),
         name='create_transaction'),
]
