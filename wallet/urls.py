
from django.urls import path
from .views import register_customer,register_wallet,register_account,register_transaction,register_card,register_thirdparty,register_notifications,register_receipts,register_loan,register_reward,register_currency

urlpatterns = [
    path("register/",register_customer, name='registrations'),
    path("registerwallet/",register_wallet, name='registrations'),
    path("registeraccount/",register_account, name='registrations'),
    path("registertransaction/",register_transaction, name='registrations'),
    path("registercard/",register_card, name='registrations'),
    path("registerthirdparty/",register_thirdparty, name='registrations'),
    path("registernotifications/",register_notifications, name='registrations'),
    path("registereceipts/",register_receipts, name='registrations'),
    path("registerloan/",register_loan, name='registrations'),
    path("registereward/",register_reward, name='registrations'),
    path("registercurrency/",register_currency, name='registrations'),
]