"""apartments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from handling import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('', views.Home.as_view(), name='home'),
    # path('equipments/', views.CreateEquipmentsView.as_view(), name='equipments'),
    path('apartments/', views.CreateApartmentsView.as_view(), name='apartments'),
    path('apartments/<int:pk>/', views.ApartmentDetailView.as_view(), name='apartmentdetail'),
    path('apartments/edit/<int:pk>/', views.ApartmentEditView.as_view(), name='apartmentedit'),
    # path('noe/', views.CreateNumberOfEquipmentView.as_view(), name='noe'),
    path('renters/', views.CreateRentersView.as_view(), name='renters'),
    path('renters/<int:pk>/', views.RenterDetailView.as_view(), name='renterdetail'),
    path('renters/edit/<int:pk>/', views.RenterEditView.as_view(), name='renteredit'),
    path('payments/', views.CreatePaymentsView.as_view(), name='payments'),
    path('payments/<int:pk>', views.PaymentDetailView.as_view(), name='paymentdetail'),
    path('payments/edit/<int:pk>/', views.PaymentEditView.as_view(), name='paymentedit'),

]
