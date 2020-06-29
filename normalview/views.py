from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
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
        rooms = ApartmentsRooms.objects.all()
        free_apart2 = Apartments.objects.filter(renters__isnull=True)
        city = request.GET.get('address','')
        surfacefrom = request.GET.get('surfacefrom','')
        surfaceto = request.GET.get('surfaceto', '')
        if surfacefrom == '':
            surfacefrom = 0
        if surfaceto == '':
            surfaceto = 9999999

        rentfrom = request.GET.get('rentfrom','')
        rentto = request.GET.get('rentto','')
        if rentfrom == '':
            rentfrom = 0
        if rentto == '':
            rentto = 999999999

        equipment = request.GET.get('equipment','')
        selected_rooms = request.GET.getlist('rooms')
        #
        # selected_rooms_queryset = ApartmentsRooms.objects.filter(pk__icontains=selected_rooms)
        #
        a1 = Q(address__icontains=city)
        a2 = Q(surface__gte=surfacefrom)
        a3 = Q(surface__lte=surfaceto)
        a4 = Q(rent__gte=rentfrom)
        a5 = Q(rent__lte=rentto)
        # a6 = Q(equipment__icontains=equipment)
        free_apart = free_apart2.filter( a1 & a2 & a3 & a4 & a5).order_by('name')


        a7 = Q(rooms__name__in=selected_rooms)
        if len(selected_rooms)>=1:
            free_apart = free_apart2.filter( a1 & a2 & a3 & a4 & a5 & a7 ).order_by('name')
        return render(request, 'home.html',{'freeaparts':free_apart,'rooms2':rooms,'main':True,'komm':''})



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
