
from django import forms
from .models import Customer,Wallet,Account,Transaction,Card,ThirdParty,Notifications,Receipts,Loan,Reward,Currency
# from. means current directory

# it inherents from a class modelform
class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        # tell it  what model to used in this form
        model = Customer
        # what fields you want to collect data for
        fields = "__all__"

class WalletRegistrationForm(forms.ModelForm):
     class Meta:
        model = Wallet
        fields = "__all__"
        # widgets = {
        #     'birthday': forms.TextInput(attrs={'class': 'datepicker'})
        # }

class AccountRegistrationForm(forms.ModelForm):
     class Meta:
        model = Account
        fields = "__all__"

class TransactionRegistrationForm(forms.ModelForm):
     class Meta:
        model = Transaction
        fields = "__all__"

class CardRegistrationForm(forms.ModelForm):
     class Meta:
        model = Card
        fields = "__all__"

class ThirdPartyRegistrationForm(forms.ModelForm):
     class Meta:
        model = ThirdParty
        fields = "__all__"

class NotificationsRegistrationForm(forms.ModelForm):
     class Meta:
        model = Notifications
        fields = "__all__"

class ReceiptsRegistrationForm(forms.ModelForm):
     class Meta:
        model = Receipts
        fields = "__all__"

class LoanRegistrationForm(forms.ModelForm):
     class Meta:
        model = Loan
        fields = "__all__"

class RewardRegistrationForm(forms.ModelForm):
     class Meta:
        model = Reward
        fields = "__all__"

class CurrencyRegistrationForm(forms.ModelForm):
     class Meta:
        model = Currency
        fields = "__all__"
