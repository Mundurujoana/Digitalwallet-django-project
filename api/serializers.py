# serializer for the Customer model
from rest_framework import serializers
from wallet.models import Customer, Wallet, Loan, Receipts, Transaction, Card, Account, Notifications



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('age', 'email')

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('currency', 'customer','userId')

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('account_number','account_type','account_name')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card        
        fields = ('card_name','card_number','card_type','card_status')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction      
        fields = ('transaction_ref','transaction_amount','customer')

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('account_number','account_type','account_name')

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipts
        fields = ('status','receipt_type','receipt_number','account')

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipts
        fields = ('status','receipt_type','receipt_number','account')

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ('notification_Id','name','status','recipient','title','description','date')


        

        
