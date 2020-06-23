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




class CreateApartmentsView(CreateView):
    model = Apartments
    template_name = 'obj_list.html'
    success_url = reverse_lazy('apartments')
    fields = ['name','address','equipment','description']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects':Apartments.objects.all()})
        return context
class ApartmentDetailView(View):
    def get(self,request,pk):
        apartment = Apartments.objects.get(pk=pk)
        apartments = Apartments.objects.all()
        return render(request,'details.html',{'object':apartment,'apart':True,'objects':apartments})
class ApartmentEditView(UpdateView):
    model = Apartments
    template_name = 'edit.html'
    fields = ['name','address','equipment','description']
    def get_success_url(self):
        apartmentid = self.kwargs['pk']
        return reverse_lazy('apartmentdetail',kwargs={'pk':apartmentid})
class ApartmentDeleteView(View):
    def get(self,request,pk):
        apart = Apartments.objects.get(pk=pk)
        apart.delete()
        return render(request,'edit.html',{'komunikat':'Datas have been deleted properly.'})




class CreateRentersView(CreateView):
    model = Renters
    template_name = 'obj_list.html'
    success_url = reverse_lazy('renters')
    fields = ['first_name','last_name','apartment']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects':Renters.objects.all()})
        return context
class RenterDetailView(View):
    def get(self,request,pk):
        renter = Renters.objects.get(pk=pk)
        renters = Renters.objects.all()
        return render(request,'details.html',{'object':renter,'rent':True,'objects':renters})
class RenterEditView(UpdateView):
    model = Renters
    template_name = 'edit.html'
    fields = ['first_name','last_name','apartment']
    def get_success_url(self):
        renterid = self.kwargs['pk']
        return reverse_lazy('renterdetail',kwargs={'pk':renterid})
class RenterDeleteView(View):
    def get(self,request,pk):
        renter = Renters.objects.get(pk=pk)
        renter.delete()
        return render(request,'edit.html',{'komunikat':'Datas have been deleted properly.'})



class CreatePaymentsView(CreateView):
    model = Payments
    template_name = 'obj_list.html'
    success_url = reverse_lazy('payments')
    fields = ['date','amount','renter','apartment']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects':Payments.objects.all()})
        return context
class PaymentDetailView(View):
    def get(self,request,pk):
        payment = Payments.objects.get(pk=pk)
        payments = Payments.objects.all()
        return render(request,'details.html',{'object':payment,'pay':True,'objects':payments})
class PaymentEditView(UpdateView):
    model = Payments
    template_name = 'edit.html'
    fields = ['date','amount','renter','apartment']
    def get_success_url(self):
        paymentid = self.kwargs['pk']
        return reverse_lazy('paymentdetail',kwargs={'pk':paymentid})
class PaymentDeleteView(View):
    def get(self, request, pk):
        pay = Payments.objects.get(pk=pk)
        pay.delete()
        return render(request, 'edit.html', {'komunikat': 'Datas have been deleted properly.'})




class SearchDatas(View):
    def get(self,request):
        search_form = SearchForm
        ap = Apartments.objects.all()
        ren = Renters.objects.all()
        pay = Payments.objects.all()
        context = {'search_form':search_form, 'objects_apartments':ap,'objects_renters':ren,'objects_payments':pay}
        return render(request,'search.html',context)

        # search_form = RenterSearchForm(request.GET)
        # search_form.is_valid()
        # first_name = search_form.cleaned_data.get('query', "")
        # last_name = search_form.cleaned_data.get('query', "")
        # apartment = search_form.cleaned_data.get('query', "")
        # q1 = Q(first_name__icontains=first_name)
        # q2 = Q(last_name__icontains=last_name)
        # q3 = Q(apartment__icontains=apartment)
        # renters = Renters.objects.filter(q1 | q2 | q3)
        # return renters, search_form
