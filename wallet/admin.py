from django.contrib import admin
from .models import Customer,Wallet,Account,Transaction,Card,ThirdParty,Notifications,Receipts,Loan,Reward,Currency


# Register your models here.
# configure you admin dashboard
class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','age','email','address','phonenumber','gender','profile_picture')
    search_fields=('first_name','last_name','age','email','address','phonenumber','gender','profile_picture')
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=('currency','customer','balance','amount','date','status')
    search_fields=('currency','customer','balance','amount','date','status')
admin.site.register(Wallet, WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=('account_number','account_type','account_name','balance','wallet')
    search_fields=('account_number','account_type','account_name','balance','wallet')
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=('transaction_ref','transaction_amount','customer','transaction_type','original_account','destination_account','transaction_charge','transaction_date')
    search_fields=('transaction_ref','transaction_amount','customer','transaction_type','original_account','destination_account','transaction_charge','transaction_date')
admin.site.register(Transaction, TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=('card_name','card_number','card_type','card_status','cvv_security','wallet','account','date_Issued','expiry_date')
    search_fields=('card_name','card_number','card_type','card_status','cvv_security','wallet','account','date_Issued','expiry_date')
admin.site.register(Card, CardAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display=('thirdparty_id','account','name','phonenumber','address','gender','transaction_cost')
    search_fields=('thirdparty_id','account','name','phonenumber','address','gender','transaction_cost')
admin.site.register(ThirdParty, ThirdPartyAdmin)

class NotificationsAdmin(admin.ModelAdmin):
    list_display=('notification_Id','name','status','recipient','title','description','date')
    search_fields=('notification_Id','name','status','recipient','title','description','date')
admin.site.register(Notifications, NotificationsAdmin)

class ReceiptsAdmin(admin.ModelAdmin):
    list_display=('receipt_type','recipt_number','account','total_Amount','transaction','recipt_File','receipt_date')
    search_fields=('receipt_type','recipt_number','account','total_Amount','transaction','recipt_File','receipt_date')
admin.site.register(Receipts, ReceiptsAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=('loan_type','amount','wallet','guaranter','loan_balance','loan_term','due_date')
    search_fields=('loan_type','amount','wallet','guaranter','loan_balance','loan_term','due_date')
admin.site.register(Loan, LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=('transaction','date','gender','bonus')
    search_fields=('transaction','date','gender','bonus')
admin.site.register(Reward, RewardAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display=('amount','country_of_origin')
    search_fields=('amount','country_of_origin')
admin.site.register(Currency, CurrencyAdmin)

