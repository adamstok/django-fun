from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from handling.forms import SearchForm

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
    fields = ['name','address','equipment','description']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects':Apartments.objects.all()})
        return context
class ApartmentDetailView(LoginRequiredMixin,View):
    def get(self,request,pk):
        apartment = Apartments.objects.get(pk=pk)
        apartments = Apartments.objects.all()
        return render(request,'details.html',{'object':apartment,'apart':True,'objects':apartments})
class ApartmentEditView(LoginRequiredMixin,UpdateView):
    model = Apartments
    template_name = 'edit.html'
    fields = ['name','address','equipment','description']
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
        return render(request,'details.html',{'object':renter,'rent':True,'objects':renters})
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
        context.update({'objects':Payments.objects.all()})
        return context
class PaymentDetailView(LoginRequiredMixin,View):
    def get(self,request,pk):
        payment = Payments.objects.get(pk=pk)
        payments = Payments.objects.all()
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
        aparts = Apartments.objects.filter(a1 | a2 | a3 | a4)
        r_first = search_form.cleaned_data.get('query', "")
        r_last = search_form.cleaned_data.get('query', "")
        r1 = Q(first_name__icontains=r_first)
        r2 = Q(last_name__icontains=r_last)
        rent = Renters.objects.filter(r1 | r2 )
        p_date = search_form.cleaned_data.get('query', "")
        p_amount = search_form.cleaned_data.get('query', "")
        p1 = Q(date__icontains=p_date)
        p2 = Q(amount__icontains=p_amount)
        pay = Payments.objects.filter(p1 | p2 )
        return aparts,rent,pay
        

