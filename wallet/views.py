from django.shortcuts import redirect, render
from .forms import CustomerRegistrationForm,WalletRegistrationForm,AccountRegistrationForm,TransactionRegistrationForm,CardRegistrationForm,ThirdPartyRegistrationForm,NotificationsRegistrationForm,ReceiptsRegistrationForm,LoanRegistrationForm,RewardRegistrationForm,CurrencyRegistrationForm
from .models import Customer,Wallet,Account,Transaction,Card,ThirdParty,Notifications,Receipts,Loan,Reward,Currency
# it renders http requests


# Create your views here.
def register_customer(request):
    # #    creat an instance of the class CustomerResigrationForm
#     form = CustomerRegistrationForm()
#     #renders the response
#     return render(request,"wallet/register_customer.html",{'form':form})
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
           form.save()
    else:
        form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{'form':form})


def register_wallet(request):
    # form = WalletRegistrationForm()
    # return render(request,"wallet/register_wallet.html",{'form':form})
    if request.method == 'POST':
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{'form':form})


def register_account(request):
    # form = AccountRegistrationForm()
    # return render(request,"wallet/register_account.html",{'form':form})
   if request.method == 'POST':
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
   else:
        form = AccountRegistrationForm()
        return render(request,"wallet/register_account.html",{'form':form})


def register_transaction(request):
    # form = TransactionRegistrationForm()
    # return render(request,"wallet/register_transaction.html",{'form':form})
    if request.method == 'POST':
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TransactionRegistrationForm()
        return render(request,"wallet/register_transaction.html",{'form':form})

    
def register_card(request):
    # form = CardRegistrationForm()
    # return render(request,"wallet/register_card.html",{'form':form})
    if request.method == 'POST':
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CardRegistrationForm()
        return render(request,"wallet/register_card.html",{'form':form})


def register_thirdparty(request):
    # form = ThirdPartyRegistrationForm()
    # return render(request,"wallet/register_thirdparty.html",{'form':form})
    if request.method == 'POST':
        form = ThirdPartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ThirdPartyRegistrationForm()
        return render(request,"wallet/register_thirdparty.html",{'form':form})


def register_notifications(request):
    # form = NotificationsRegistrationForm()
    # return render(request,"wallet/register_notifications.html",{'form':form})
    if request.method == 'POST':
        form = NotificationsRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NotificationsRegistrationForm()
    return render(request,"wallet/register_notifications.html",{'form':form})

    
def register_receipts(request):
    # form = ReceiptsRegistrationForm()
    # return render(request,"wallet/register_receipts.html",{'form':form})
   if request.method == 'POST':
        form = ReceiptsRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
   else:
        form = ReceiptsRegistrationForm()
        return render(request,"wallet/register_receipts.html",{'form':form})


def register_loan(request):
    # form = LoanRegistrationForm()
    # return render(request,"wallet/register_loan.html",{'form':form})
    if request.method == 'POST':
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LoanRegistrationForm()
        return render(request,"wallet/register_loan.html",{'form':form})
    

def register_reward(request):
    # form = RewardRegistrationForm()
    # return render(request,"wallet/register_reward.html",{'form':form})
    if request.method == 'POST':
        form = RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RewardRegistrationForm()
        return render(request,"wallet/register_reward.html",{'form':form})
    
    
def register_currency(request):
    # form = CurrencyRegistrationForm()
    # return render(request,"wallet/register_currency.html",{'form':form})
    if request.method == 'POST':
        form = CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CurrencyRegistrationForm()
        return render(request,"wallet/register_currency.html",{'form':form})
    


# Lists
def list_customers(request):
    customers = Customer.objects.all()
    return render(request,"wallet/list_customers.html",{'customers':customers})

def list_wallets(request):
    wallets = Wallet.objects.all()
    return render(request,"wallet/list_wallets.html",{'wallets':wallets})

def list_accounts(request):
    accounts = Account.objects.all()
    return render(request,"wallet/list_accounts.html",{'accounts':accounts})

def list_transactions(request):
    transactions = Transaction.objects.all()
    return render(request,"wallet/list_transactions.html",{'transactions':transactions})

def list_cards(request):
    cards = Card.objects.all()
    return render(request,"wallet/list_cards.html",{'cards':cards})

def list_thirdpartys(request):
    thirdpartys = ThirdParty.objects.all()
    return render(request,"wallet/list_thirdpartys.html",{'thirdpartys':thirdpartys})

def list_notifications(request):
    notifications = Notifications.objects.all()
    return render(request,"wallet/list_notifications.html",{'notifications':notifications})

def list_receipts(request):
    receipts = Receipts.objects.all()
    return render(request,"wallet/list_receipts.html",{'receipts':receipts})

def list_loans(request):
    loans = Loan.objects.all()
    return render(request,"wallet/list_loans.html",{'loans':loans})

def list_rewards(request):
    rewards = Reward.objects.all()
    return render(request,"wallet/list_rewards.html",{'rewards':rewards})

def list_currencys(request):
    currencys = Currency.objects.all()
    return render(request,"wallet/list_currencys.html",{'currencys':currencys})

#Single Object Views and Edit Views with corresponding URLs, views and templates for these models.
#Customer
def customer_profile(request,id):
   customerz= Customer.objects.get(id=id)
    #we inject the variable in the request
   return render(request,"wallet/customer_profile.html",{'customerz':customerz})
   
def edit_customer_profile(request,id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return  redirect("customer_profile", id = customer.id)

    else:
            form = CustomerRegistrationForm(instance=customer)
    return render(request, "wallet/edit_customer.html", {'form':form})    

#Wallet 
def wallet_profile(request,id):
   walletz= Wallet.objects.get(id=id)
    #we inject the variable in the request
   return render(request,"wallet/wallet_profile.html", {'walletz':walletz })
   
def edit_wallet_profile(request, id):
    wallet =Wallet.objects.get(id=id)
    if request.method == "POST":
        form = WalletRegistrationForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
            return redirect("wallet_profile", id =wallet.id)
    else:
            form = WalletRegistrationForm(instance=wallet)
    return render(request, "wallet/edit_wallet.html",{'form':form})


#Account 
def account_profile(request,id):
   accountz= Account.objects.get(id=id)
    #we inject the variable in the request
   return render(request,"wallet/account_profile.html", {'accountz':accountz })
   
def edit_account_profile(request, id):
    account =Account.objects.get(id=id)
    if request.method == "POST":
        form = AccountRegistrationForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect("account_profile", id = account.id)
    else:
            form = AccountRegistrationForm(instance = account)
    return render(request, "wallet/edit_account.html",{'form':form})


#Card
def card_profile(request,id):
   cardz= Card.objects.get(id=id)
    #we inject the variable in the request
   return render(request,"wallet/card_profile.html", {'cardz':cardz })
   
def edit_card_profile(request, id):
    card = Card.objects.get(id=id)
    if request.method == "POST":
        form = CardRegistrationForm(request.POST, instance = card)
        if form.is_valid():
            form.save()
            return redirect("card_profile", id = card.id)
    else:
            form = CardRegistrationForm(instance=card)
    return render(request, "wallet/edit_card.html",{'form':form})


#Transaction
def transaction_profile(request,id):
   transactionz = Transaction.objects.get(id=id)
    #we inject the variable in the request
   return render(request,"wallet/transaction_profile.html", {'transactionz':transactionz })
   
def edit_transaction_profile(request, id):
    transaction = Transaction.objects.get(id=id)
    if request.method == "POST":
        form = TransactionRegistrationForm(request.POST, instance = transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction_profile", id = transaction.id)
    else:
            form = TransactionRegistrationForm(instance = transaction)
    return render(request, "wallet/edit_transaction.html",{'form':form})


#Receipt
def receipt_profile(request,id):
   receiptz= Receipts.objects.get(id=id)
    #we inject the variable in the request
   return render(request,"wallet/receipt_profile.html", {'receiptz':receiptz })
   
def edit_receipt_profile(request, id):
    receipt = Receipts.objects.get(id=id)
    if request.method == "POST":
        form = ReceiptsRegistrationForm(request.POST, instance = receipt)
        if form.is_valid():
            form.save()
            return redirect("receipt_profile", id = receipt.id)
    else:
            form = ReceiptsRegistrationForm(instance = receipt)
    return render(request, "wallet/edit_receipt.html",{'form':form})