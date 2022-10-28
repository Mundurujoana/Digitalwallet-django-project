from django.urls import path, include
from rest_framework import routers
from . import views
from .views import AccountDepositView


router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'wallets', views.WalletViewSet)
router.register(r'cards', views.CardViewSet)
router.register(r'customers', views.TransactionViewSet)
router.register(r'loans', views.LoanViewSet)
router.register(r'receipts', views.ReceiptViewSet)
router.register(r'notifications', views.NotificationSerializer)


urlpatterns = [
  path('', include(router.urls)),
  path("deposit/", AccountDepositView.as_view(), name="deposit-view"),
]
