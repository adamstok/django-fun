from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from handling.forms import RenterSearchForm

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from handling.models import Apartments,Renters,Payments


class Home(LoginRequiredMixin, View):
    def get(self,request):
        return render(request, 'base.html')


# class CreateEquipmentsView(CreateView):
#     model = Equipments
#     template_name = 'obj_list.html'
#     success_url = reverse_lazy('equipments')
#     fields = ['description']
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({'objects':Equipments.objects.all()})
#         return context


class CreateApartmentsView(CreateView):
    model = Apartments
    template_name = 'obj_list.html'
    success_url = reverse_lazy('apartments')
    fields = ['name','address','equipment','description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects':Apartments.objects.all()})
        return context


# class CreateNumberOfEquipmentView(CreateView):
#     model = NumberOfEquipment
#     template_name = 'obj_list.html'
#     success_url = reverse_lazy('noe')
#     fields = ['equipment','apartment','equipments_number']
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update({'objects':NumberOfEquipment.objects.all()})
#         return context
#

class CreateRentersView(CreateView):
    model = Renters
    template_name = 'obj_list.html'
    success_url = reverse_lazy('renters')
    fields = ['first_name','last_name','apartment']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects':Renters.objects.all()})
        return context

    # def search_renters(self,request):
    #     search_form = RenterSearchForm(request.GET)
    #     search_form.is_valid()
    #     first_name = search_form.cleaned_data.get('query', "")
    #     last_name = search_form.cleaned_data.get('query', "")
    #     apartment = search_form.cleaned_data.get('query', "")
    #     q1 = Q(first_name__icontains=first_name)
    #     q2 = Q(last_name__icontains=last_name)
    #     q3 = Q(apartment__icontains=apartment)
    #     renters = Renters.objects.filter(q1 | q2 | q3)
    #     return renters, search_form

class CreatePaymentsView(CreateView):
    model = Payments
    template_name = 'obj_list.html'
    success_url = reverse_lazy('payments')
    fields = ['date','amount','renter','apartment']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects':Payments.objects.all()})
        return context

