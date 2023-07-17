from django.urls import path
from .views import (
                        AccountView,
                        AccountDetailView,
                        LoginView,
                    )

urlpatterns = [
    path('signup/', AccountView.as_view(), name='account'),
    path('account-detail/', AccountDetailView.as_view(), name='account-detail'),
    path('login/', LoginView.as_view(), name='login'),
   
]

