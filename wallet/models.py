
from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
  first_name=models.CharField(max_length=50,null=True)
  last_name=models.CharField(max_length=50,null=True)
  age=models.CharField(max_length=20,null=True)
  email=models.EmailField(max_length=55,null=True)
  address=models.CharField(max_length=50,null=True)
  phonenumber=models.CharField(max_length=55,null=True)
  date_created = models.DateTimeField(default=timezone.now)
  nationality=models.CharField(max_length=50,null=True)
  gender_choices = (('m', 'male'),('f', 'female'),)
  gender = models.CharField(max_length=5, choices=gender_choices,null=True)
  profile_picture = models.ImageField(upload_to='profile_pictures/',null=True)


class Wallet(models.Model):
  currency =models.ForeignKey('Currency', on_delete=models.CASCADE, related_name ='Wallet_currency')
  customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Wallet_customer')
  userId =models.CharField(max_length=50, null=True)
  balance = models.IntegerField()
  amount = models.IntegerField()
  date=models.DateTimeField(default=timezone.now)
  status_choices = ('a', 'active'),('i', 'inactive')
  status=models.CharField(max_length=50,choices=status_choices, null=True)
  pin=models.CharField(max_length=30,null=True)


class Account(models.Model):


  account_number = models.IntegerField(default=0)
  account_type = models.CharField(max_length=50,null=True)
  balance = models.IntegerField()
  account_name = models.CharField(max_length=50,null=True)
  wallet = models.ForeignKey('Wallet',on_delete=models.CASCADE, related_name ='Account_wallet')

  def deposit(self, amount):
            if amount <= 0:
                message =  "Invalid amount"
                status = 403
            else:
                self.balance += amount
                self.save()
                message = f"You have deposited {amount}, your new balance is {self.balance}"
                status = 200
            return message, status
    
  def transfer(self, destination, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
      
       elif amount < self.account_balance:
           message =  "Insufficient balance"
           status = 403
      
       else:
           self.account_balance -= amount
           self.save()
           destination.deposit(amount)
          
           message = f"You have transfered {amount}, your new balance is {self.account_balance}"
           status = 200
       return message, status
       
class Transaction(models.Model):
 transaction_ref=models.CharField(max_length=255,null=True)
 wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name = 'Transaction_wallet')
 transaction_amount=models.IntegerField()
 customer=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Transaction_customer',null=True)
 transaction_choices = (('withdraw', 'Withdrawal'),('deposit', 'Deposit'))
 transaction_type=models.CharField(max_length=10, choices=transaction_choices,null=True)
 transaction_history = models.TextField(null=True)
 transaction_charge=models.IntegerField()
 transaction_date=models.DateTimeField(default=timezone.now)
 receipts =models.ForeignKey('Receipts', on_delete=models.CASCADE, related_name ='Transaction_receipt',null=True)
 original_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_original_account')
 destination_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_destination_account')


class Card(models.Model):
 date_Issued = models.DateTimeField(default=timezone.now)
 card_name = models.CharField(max_length=50,null=True)
 card_number = models.IntegerField()
 issuer_choices = (('Master', 'Mastercard'),('visa', 'visacard'))
 card_type = models.CharField(max_length=20, choices=issuer_choices,null=True)
 expiry_date = models.DateTimeField(default=timezone.now)
 status_choices=(('d', 'debit'),('c', 'credit'))
 card_status= models.CharField(max_length=1, choices=status_choices,null=True)
 cvv_security=models.IntegerField()
 wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name ='Card_wallet')
 account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name ='Card_account')     


class ThirdParty(models.Model):
 account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name ='ThirdParty_account')
 name=models. CharField(max_length=25,null=True)
 thirdparty_id=models.CharField(max_length=20,null=True)
 phonenumber=models.CharField(max_length=55,null=True)
 address=models.CharField(max_length=50,null=True)
 transaction_cost =models.IntegerField(null=True)
 gender_choices = (('m', 'male'),('f', 'female'),)
 gender = models.CharField(max_length=5, choices=gender_choices,null=True)


class Notifications(models.Model):
 notification_Id=models.CharField(max_length=30,null=True)
 name=models. CharField(max_length=50,null=True)
 status_choices = (('read', 'read'),('unread', 'unread'),)
 status=models.CharField(max_length=12, choices=status_choices,null=True)
 date=models.DateTimeField(default=timezone.now)
 recipient=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Notifications_recipient')    
 title = models.CharField(max_length=105, null=True)
 description=models.TextField(null=True)


class Receipts(models.Model):
 status_choices = (('deposits', 'Bank deposits'),('withdrawals', 'Cash withdrawals'),('loan', 'loan payments'),('creditcard', 'creditcard payments'))
 status=models.CharField(max_length=15, choices=status_choices,null=True)
 receipt_type=models.CharField(max_length=30, choices=status_choices, null=True)
 receipt_date=models.DateTimeField(default=timezone.now)
 receipt_number=models.CharField(max_length=30, null=True)
 account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name ='Receipts_account')
 total_Amount=models.IntegerField()
 transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name ='Receipts_transaction')
 receipt_File=models.FileField(upload_to='wallet/')


class Loan(models.Model):
 loan_number=models.IntegerField()
 loan_type=models.CharField(max_length=30, null=True)
 amount=models.IntegerField()
 date=models.DateTimeField(default=timezone.now)
 wallet=models.ForeignKey('Wallet', on_delete=models.CASCADE, related_name ='Loan_wallet')
 interest_rate=models.IntegerField()
 guaranter=models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Loan_guaranter')
 due_date=models.DateField(default=timezone.now)
 loan_balance=models.IntegerField(default=0)
 loan_term=models.IntegerField()


class Reward(models.Model):  
 transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name ='Reward_transaction')
 date = models.DateTimeField(default=timezone.now)
 customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name ='Reward_customer')
 gender_choices = (('m', 'male'),('f', 'female'),)
 gender = models.CharField(max_length=5, choices=gender_choices,null=True) 
 bonus = models.CharField(max_length=30, null=True)

class Currency(models.Model):
 amount = models.IntegerField()
 country_of_origin = models.CharField(max_length=30, null=True)


        