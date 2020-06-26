from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from handling.models import Apartments, ApartmentsPics,ApartmentsRooms

from normalview.models import Messages
from normalview.forms import MessagesForm

# Create your views here.
from django.views import View
from django.views.generic import CreateView


class NormalHome(View):
    def get(self,request):
        free_apart = Apartments.objects.filter(renters__isnull=True)
        return render(request, 'home.html',{'freeaparts':free_apart})


class MessageView(View):
    def get(self,request):
        form = MessagesForm()
        return render(request,'message.html',{'form':form})

    def post(self,request):
        form = MessagesForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['from_mail']
            mess = form.cleaned_data['message']
            m1 = Messages.objects.create(from_mail=email,message=mess)
            m1.save()
            return render(request,'message.html',{'komunikat':'Message sended.','form':form})
        return render(request, 'message.html', {'komunikat': 'Error', 'form': form})

class NormalApartmentDetailView(View):
    def get(self,request,pk):
        free_apart = Apartments.objects.filter(renters__isnull=True)
        apartment = Apartments.objects.get(pk=pk)
        apartments = Apartments.objects.all()
        pics = ApartmentsPics.objects.filter(apartment=apartment)
        rooms = ApartmentsRooms.objects.filter(apartments=apartment)
        return render(request,'details2.html',{'object':apartment,'apart':True,'objects':apartments,'pics':pics,'rooms':rooms,'freeaparts':free_apart})
