from django.shortcuts import render
from rest_framework import viewsets
from wallet.models import Customer, Notifications, Wallet, Loan, Receipts, Transaction, Card, Account
from . import serializers

# Create your views here.
#Customer
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()   
    serializer_class = serializers.CustomerSerializer

#Wallet
class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = serializers.WalletSerializer

#Account   
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = serializers.AccountSerializer

#Card
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = serializers.CardSerializer

#Transaction
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer

#Loan
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = serializers.LoanSerializer

#Receipt
class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipts.objects.all()
    serializer_class = serializers.ReceiptSerializer

#Notifications
class NotificationSerializer(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = serializers.NotificationSerializer