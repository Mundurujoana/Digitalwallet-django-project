
from django.urls import path
from .import views
urlpatterns = [
    path("register/",views.register_customer, name='registrations'),
    path("registerwallet/",views.register_wallet, name='registrations'),
    path("registeraccount/",views.register_account, name='registrations'),
    path("registertransaction/",views.register_transaction, name='registrations'),
    path("registercard/",views.register_card, name='registrations'),
    path("registerthirdparty/",views.register_thirdparty, name='registrations'),
    path("registernotifications/",views.register_notifications, name='registrations'),
    path("registereceipts/",views.register_receipts, name='registrations'),
    path("registerloan/",views.register_loan, name='registrations'),
    path("registereward/",views.register_reward, name='registrations'),
    path("registercurrency/",views.register_currency, name='registrations'),
    path("customers/",views.list_customers, name='customer'),
    path("wallets/",views.list_wallets, name='wallet'),
    path("accounts/",views.list_accounts, name='account'),
    path("cards/",views.list_cards, name='card'),
    path("currencys/",views.list_currencys, name='currency'),
    path("loans/",views.list_loans, name='loan'),
    path("notifications/",views.list_notifications, name='notifications'),
    path("receipts/",views.list_receipts, name='receipts'),
    path("rewards/",views.list_rewards, name='rewards'),
    path("thirdpartys/",views.list_thirdpartys, name='thirdpartys'),
    path("transactions/",views.list_transactions, name='transactions'),
    path("wallets/",views.list_wallets, name='wallets'),
]