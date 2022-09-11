from django.shortcuts import render
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
    notifcations = Notifications.objects.all()
    return render(request,"wallet/list_notifications.html",{'notifcations':notifcations})

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

