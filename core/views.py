from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Province, ProvinceSource, ProvinceBudget, Contact, Year, TotalBudget, ActualExpenditure


class BudgetVisualization(LoginRequiredMixin, DetailView):
    model = Province
    template_name = 'budgetvisualization.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BudgetVisualization, self).get_context_data(**kwargs)
        calculation = Province.objects.order_by('id')
        for data in calculation:
            percentage_male = (data.male_population) / (data.male_population + data.female_population)
            percentage_female = (data.female_population) / (data.male_population + data.female_population)
            total_population = data.male_population + data.female_population
        source = ProvinceSource.objects.filter(province_name=self.kwargs['pk'])
        budget = ProvinceBudget.objects.filter(province_name=self.kwargs['pk']).values('province_name__name',
                                                                                       'office_name',
                                                                                       'total_budget__total',
                                                                                       'actual_expenditure__total',
                                                                                       'total_budget__year__year',
                                                                                       'actual_expenditure__year__year')
        tot_bug = TotalBudget.objects.filter(province_name=self.kwargs['pk'])
        act_exp = ActualExpenditure.objects.filter(province_name=self.kwargs['pk'])
        topdata = Province.objects.filter(id=self.kwargs['pk'])
        for bug in budget:
            print(bug['total_budget__year__year'])
        date = Year.objects.all()
        first_date = Year.objects.filter().first()
        context['source'] = source
        context['topdata'] = topdata
        context['first_date'] = str(first_date)
        context['budget'] = budget
        context['percentage_male'] = percentage_male
        context['percentage_female'] = percentage_female
        context['total_population'] = total_population
        context['date'] = date
        context['tot_bug'] = tot_bug
        context['act_exp'] = act_exp
        context['object1'] = self.kwargs['pk']

        return context

    def post(self, request, *args, **kwargs):
        data1 = self.request.POST['year']
        data2 = self.request.POST['budget']
        calculation = Province.objects.order_by('id')
        topdata = Province.objects.filter(id=self.kwargs['pk'])
        date = Year.objects.all()
        for data in calculation:
            percentage_male = (data.male_population) / (data.male_population + data.female_population)
            percentage_female = (data.female_population) / (data.male_population + data.female_population)
            total_population = data.male_population + data.female_population
        source = ProvinceSource.objects.filter(province_name=self.kwargs['pk'])
        budget = ProvinceBudget.objects.filter(province_name=self.kwargs['pk']).values('province_name__name',
                                                                                       'office_name',
                                                                                       'total_budget__total',
                                                                                       'actual_expenditure__total',
                                                                                       'total_budget__year__year',
                                                                                       'actual_expenditure__year__year')
        if data2 == str(1):

            context = {
                'topdata': topdata,
                'source': source,
                'budget': budget,
                'percentage_male': percentage_male,
                'percentage_female': percentage_female,
                'total_population': total_population,
                'date': date,
                'first_date': data1,
                'object1': self.kwargs['pk'],
                'val': '1'

            }
            return render(request, 'budgetvisualization.html', context)
        elif data2 == str(2):

            context = {
                'topdata': topdata,
                'source': source,
                'budget': budget,
                'percentage_male': percentage_male,
                'percentage_female': percentage_female,
                'total_population': total_population,
                'date': date,
                'first_date': data1,
                'object1': self.kwargs['pk'],
                'val': '2'

            }
            return render(request, 'budgetvisualization.html', context)


class HomePage(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        province_data = Province.objects.order_by('id')
        provincefilter = Province.objects.filter().first()
        total_budget_nepal = 0
        for data in province_data:
            total_budget_nepal = data.total_budget + total_budget_nepal
        context = {
            'provincefilter': provincefilter,
            'province_data': province_data,
            'total_budget_nepal': total_budget_nepal
        }
        return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email1 = request.POST['email']
        email2 = request.POST['email1']
        message = request.POST['message']

        if email1 == email2:
            data = Contact.objects.create(name=name, email=email1, message=message)
            data.save()
            resp = {
                'result': 'success'
            }
            return JsonResponse(resp)
        else:
            resp = {
                'result': 'failed'
            }
            return JsonResponse(resp)


class Blog(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        provincefilter = Province.objects.filter().first()
        context = {
            'provincefilter': provincefilter
        }
        return render(request, 'blogs.html', context)
