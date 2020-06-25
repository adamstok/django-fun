from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from handling.forms import SearchForm,ImageUploadForm,ImageUploadForm1,ApartmentsRoomsForm
from handling.models import ExamplePic,ApartmentsPics, ApartmentsRooms
from normalview.models import Messages

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView
from handling.models import Apartments,Renters,Payments
from handling.forms import ApartmentsForm


class Home(LoginRequiredMixin, View):
    def get(self,request):
        return render(request, 'base.html')




class CreateApartmentsView(LoginRequiredMixin,CreateView):
    model = Apartments
    template_name = 'obj_list.html'
    success_url = reverse_lazy('apartments')
    fields = ['name','address','surface','rent','costs','rooms','equipment','description']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects':Apartments.objects.all()})
        return context
class ApartmentDetailView(LoginRequiredMixin,View):
    def get(self,request,pk):
        apartment = Apartments.objects.get(pk=pk)
        apartments = Apartments.objects.all()
        pics = ApartmentsPics.objects.filter(apartment=apartment)
        payments = Payments.objects.filter(apartment=apartment)
        try:
            renter = Renters.objects.get(apartment=apartment)
        except Renters.DoesNotExist:
            renter = False
        rooms = ApartmentsRooms.objects.filter(apartments=apartment)
        return render(request,'details.html',{'object':apartment,'apart':True,'objects':apartments,'pics':pics,'payments':payments,'rooms':rooms,'renter':renter})
class ApartmentEditView(LoginRequiredMixin,UpdateView):
    model = Apartments
    template_name = 'edit.html'
    #fields = ['name','address','equipment','description']
    fields = ['name', 'address', 'surface', 'rent', 'costs', 'rooms', 'equipment', 'description']
    def get_success_url(self):
        apartmentid = self.kwargs['pk']
        return reverse_lazy('apartmentdetail',kwargs={'pk':apartmentid})
class ApartmentDeleteView(LoginRequiredMixin,View):
    def get(self,request,pk):
        apart = Apartments.objects.get(pk=pk)
        apart.delete()
        return render(request,'edit.html',{'komunikat':'Datas have been deleted properly.'})




class CreateRentersView(LoginRequiredMixin,CreateView):
    model = Renters
    template_name = 'obj_list.html'
    success_url = reverse_lazy('renters')
    fields = ['first_name','last_name','apartment']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects':Renters.objects.all()})
        return context
class RenterDetailView(LoginRequiredMixin,View):
    def get(self,request,pk):
        renter = Renters.objects.get(pk=pk)
        renters = Renters.objects.all()
        payments = Payments.objects.filter(renter=renter).order_by('date')
        return render(request,'details.html',{'object':renter,'rent':True,'objects':renters,'p':payments})
class RenterEditView(LoginRequiredMixin,UpdateView):
    model = Renters
    template_name = 'edit.html'
    fields = ['first_name','last_name','apartment']
    def get_success_url(self):
        renterid = self.kwargs['pk']
        return reverse_lazy('renterdetail',kwargs={'pk':renterid})
class RenterDeleteView(LoginRequiredMixin,View):
    def get(self,request,pk):
        renter = Renters.objects.get(pk=pk)
        renter.delete()
        return render(request,'edit.html',{'komunikat':'Datas have been deleted properly.'})



class CreatePaymentsView(LoginRequiredMixin,CreateView):
    model = Payments
    template_name = 'obj_list.html'
    success_url = reverse_lazy('payments')
    fields = ['date','amount','renter','apartment']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects':Payments.objects.all().order_by('date')})
        return context
class PaymentDetailView(LoginRequiredMixin,View):
    def get(self,request,pk):
        payment = Payments.objects.get(pk=pk)
        payments = Payments.objects.all().order_by('date')
        return render(request,'details.html',{'object':payment,'pay':True,'objects':payments})
class PaymentEditView(LoginRequiredMixin,UpdateView):
    model = Payments
    template_name = 'edit.html'
    fields = ['date','amount','renter','apartment']
    def get_success_url(self):
        paymentid = self.kwargs['pk']
        return reverse_lazy('paymentdetail',kwargs={'pk':paymentid})
class PaymentDeleteView(LoginRequiredMixin,View):
    def get(self, request, pk):
        pay = Payments.objects.get(pk=pk)
        pay.delete()
        return render(request, 'edit.html', {'komunikat': 'Datas have been deleted properly.'})




class SearchDatas(LoginRequiredMixin,View):
    def get(self,request):
        search_form = SearchForm
        aparts,rent,pay= self.search(request)
        context = {'search_form':search_form, 'objects_apartments':aparts,'objects_renters':rent,'objects_payments':pay}
        return render(request,'search.html',context)
    
    def search(self,request):
        search_form = SearchForm(request.GET)
        search_form.is_valid()
        a_name = search_form.cleaned_data.get('query', "")
        a_address = search_form.cleaned_data.get('query', "")
        a_equipment = search_form.cleaned_data.get('query', "")
        a_description = search_form.cleaned_data.get('query', "")
        a1 = Q(name__icontains=a_name)
        a2 = Q(address__icontains=a_address)
        a3 = Q(equipment__icontains=a_equipment)
        a4 = Q(description__icontains=a_description)
        aparts = Apartments.objects.filter(a1 | a2 | a3 | a4).order_by('name')
        r_first = search_form.cleaned_data.get('query', "")
        r_last = search_form.cleaned_data.get('query', "")
        r1 = Q(first_name__icontains=r_first)
        r2 = Q(last_name__icontains=r_last)
        rent = Renters.objects.filter(r1 | r2 ).order_by('first_name')
        p_date = search_form.cleaned_data.get('query', "")
        p_amount = search_form.cleaned_data.get('query', "")
        p1 = Q(date__icontains=p_date)
        p2 = Q(amount__icontains=p_amount)
        pay = Payments.objects.filter(p1 | p2 ).order_by('date')
        return aparts,rent,pay
        

class UploadPic(LoginRequiredMixin,View):
    def get(self,request):
        pics = ApartmentsPics.objects.all().order_by('apartment_id')
        form = ImageUploadForm1()
        return render(request,'upload.html',{'form':form,'objects':pics})

    def post(self,request):
        pics = ApartmentsPics.objects.all()
        form = ImageUploadForm1(request.POST, request.FILES)
        if form.is_valid():
            pic = form.cleaned_data['image']
            ap = form.cleaned_data['apartment']
            im1 = ApartmentsPics.objects.create(pics=pic,apartment=ap)
            im1.save()
            return render(request,'upload.html',{'komunikat':'image upload success','form':form,'objects':pics})
        return render(request, 'upload.html', {'komunikat': 'Error', 'form': form,'objects':pics})

class DeletePic(LoginRequiredMixin,View):
    def get(self, request, pk):
        pic = ApartmentsPics.objects.get(pk=pk)
        apartm = pic.apartment_id
        pic.delete()
        #return render(request, 'edit.html', {'komunikat': 'Datas have been deleted properly.'})
        apartment = Apartments.objects.get(pk=apartm)
        apartments = Apartments.objects.all()
        pics = ApartmentsPics.objects.filter(apartment=apartment)
        payments = Payments.objects.filter(apartment=apartment)
        try:
            renter = Renters.objects.get(apartment=apartment)
        except Renters.DoesNotExist:
            renter = False
        rooms = ApartmentsRooms.objects.filter(apartments=apartment)
        return render(request,'details.html',{'object':apartment,'apart':True,'objects':apartments,'pics':pics,'payments':payments,'rooms':rooms,'renter':renter})



# class DeletePic(LoginRequiredMixin,View):
#     def get(self, request, pk):
#         pic = ApartmentsPics.objects.get(pk=pk)
#         apart = pic.apartment_id
#         pic.delete()
#         return render(request, 'edit.html', {'komunikat': 'Datas have been deleted properly.'})



class CreateRoomsView(LoginRequiredMixin,CreateView):
    model = ApartmentsRooms
    template_name = 'obj_list.html'
    success_url = reverse_lazy('rooms')
    fields = ['name']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects':ApartmentsRooms.objects.all()})
        return context
class RoomsDetailView(LoginRequiredMixin,View):
    def get(self,request,pk):
        room = ApartmentsRooms.objects.get(pk=pk)
        rooms = ApartmentsRooms.objects.all()
        return render(request,'details.html',{'object':room,'rm':True,'objects':rooms})
class RoomsEditView(LoginRequiredMixin,UpdateView):
    model = ApartmentsRooms
    template_name = 'edit.html'
    fields = ['name']
    def get_success_url(self):
        roomid = self.kwargs['pk']
        return reverse_lazy('roomsdetail',kwargs={'pk':roomid})
class RoomsDeleteView(LoginRequiredMixin,View):
    def get(self,request,pk):
        room = ApartmentsRooms.objects.get(pk=pk)
        room.delete()
        return render(request,'edit.html',{'komunikat':'Datas have been deleted properly.'})


class SeeMessageView(LoginRequiredMixin,View):
    def get(self, request):
        msg = Messages.objects.all()
        return render(request,'msg.html',{'object':msg})
        #return HttpResponse(msg)

class DeleteMessages(LoginRequiredMixin,View):
    def get(self,request,pk):
        msg = Messages.objects.get(pk=pk)
        msg.delete()
        messages = Messages.objects.all()
        return render(request, 'msg.html', {'object': messages,'komunikat':'Message deleted'})


