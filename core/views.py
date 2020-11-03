from django.shortcuts import render, redirect
from django.core.paginator import Paginator
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Province, ProvinceSource, ProvinceBudget, Contact, Year, TotalBudget, ActualExpenditure, Blog, \
    AboutMission, Glossary, ExtraNecessaryData


class BudgetVisualization(DetailView):
    model = Province
    template_name = 'budgetvisualization.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BudgetVisualization, self).get_context_data(**kwargs)
        calculation = Province.objects.order_by('id')
        test5 = ProvinceSource.objects.all()
        source = ProvinceSource.objects.filter(province_name=self.kwargs['pk'])
        budget = ProvinceBudget.objects.filter(province_name=self.kwargs['pk']).values('province_name__name',
                                                                                       'office_name',
                                                                                       'total_budget__total',
                                                                                       'total_budget__current',
                                                                                       'total_budget__capital',
                                                                                       'actual_expenditure__total',
                                                                                       'actual_expenditure__current',
                                                                                       'actual_expenditure__capital',
                                                                                       'total_budget__year__year',
                                                                                       'actual_expenditure__year__year')
        tot_bug = TotalBudget.objects.filter(province_name=self.kwargs['pk'])
        act_exp = ActualExpenditure.objects.filter(province_name=self.kwargs['pk'])
        topdata = Province.objects.filter(id=self.kwargs['pk'])
        date = Year.objects.all()
        first_date1 = Year.objects.filter().first()
        first_date = first_date1.year
        context['source'] = source
        context['topdata'] = topdata
        context['first_date'] = str(first_date)
        context['budget'] = budget
        context['date'] = date
        context['calculation'] = calculation
        context['tot_bug'] = tot_bug
        context['act_exp'] = act_exp
        context['object1'] = self.kwargs['pk']
        context['datatosend1'] = 'Actual Expenditure'
        context['data1'] = '2015/2016'

        return context

    def post(self, request, *args, **kwargs):
        data1 = self.request.POST['year']
        data2 = self.request.POST['budget']
        if str(data2) == str(2):
            datatosend1 = 'Actual Expenditure'
        if str(data2) == str(1):
            datatosend1 = 'Total Budget'
        calculation = Province.objects.order_by('id')
        print(calculation)
        topdata = Province.objects.filter(id=self.kwargs['pk'])
        date = Year.objects.all()
        source = ProvinceSource.objects.filter(province_name=self.kwargs['pk'])
        budget = ProvinceBudget.objects.filter(province_name=self.kwargs['pk']).values('province_name__name',
                                                                                       'office_name',
                                                                                       'total_budget__total',
                                                                                       'total_budget__current',
                                                                                       'total_budget__capital',
                                                                                       'actual_expenditure__total',
                                                                                       'actual_expenditure__current',
                                                                                       'actual_expenditure__capital',
                                                                                       'total_budget__year__year',
                                                                                       'actual_expenditure__year__year')
        if data2 == str(1):

            context = {
                'datatosend1': datatosend1,
                'data1': data1,
                'topdata': topdata,
                'calculation': calculation,
                'source': source,
                'budget': budget,
                'date': date,
                'first_date': data1,
                'object1': self.kwargs['pk'],
                'val': '1'

            }
            return render(request, 'budgetvisualization.html', context)
        elif data2 == str(2):

            context = {
                'datatosend1': datatosend1,
                'data1': data1,
                'topdata': topdata,
                'source': source,
                'budget': budget,
                'date': date,
                'first_date': data1,
                'object1': self.kwargs['pk'],
                'val': '2'

            }
            return render(request, 'budgetvisualization.html', context)


class HomePage(TemplateView):

    def get(self, request, *args, **kwargs):
        province_data = Province.objects.order_by('id')
        provincefilter = Province.objects.filter().first()
        total_budget_nepal = ExtraNecessaryData.objects.filter().first()
        blog = Blog.objects.order_by('id')
        paginator = Paginator(blog, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'blog': page_obj,
            'provincefilter': provincefilter,
            'province_data': province_data,
            'total_budget_nepal': total_budget_nepal
        }
        return render(request, 'index.html', context)


class AboutView(TemplateView):

    def get(self, request, *args, **kwargs):
        provincefilter = Province.objects.filter().first()
        aboutmission = AboutMission.objects.order_by('id')
        context = {
            'provincefilter': provincefilter,
            'aboutmission': aboutmission
        }
        return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email1 = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if email1:
            data = Contact.objects.create(name=name, email=email1, phone=phone, message=message)
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


class BlogData(TemplateView):
    template_name = 'blogs.html'

    def get(self, request, *args, **kwargs):
        blog = Blog.objects.order_by('id')
        provincefilter = Province.objects.filter().first()
        paginator = Paginator(blog, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'paginator': paginator,
            'page_obj': page_obj,
            'provincefilter': provincefilter
        }
        return render(request, 'blogs.html', context)


class GlossaryView(TemplateView):
    template_name = 'glossary.html'

    def get(self, request, *args, **kwargs):
        provincefilter = Province.objects.filter().first()
        glossarydate = Glossary.objects.latest('updated_at')
        findletter = Glossary.objects.order_by('id')
        E = []
        H = []
        J = []
        K = []
        L = []
        O = []
        Q = []
        S = []
        T = []
        U = []
        W = []
        X = []
        Y = []
        Z = []
        zero = []
        for data in findletter:
            test = data.title[0][0]
            if test == "A" or test == "a":
                A = test
            elif test == "B" or test == "b":
                B = test
            elif test == "C" or test == "c":
                C = test
            elif test == "D" or test == "d":
                D = test
            elif test == "E" or test == "e":
                E = test
            elif test == "F" or test == "f":
                F = test
            elif test == "G" or test == "g":
                G = test
            elif test == "H" or test == "h":
                H = test
            elif test == "I" or test == "i":
                I = test
            elif test == "J" or test == "j":
                J = test
            elif test == "K" or test == "k":
                K = test
            elif test == "L" or test == "l":
                L = test
            elif test == "M" or test == "m":
                M = test
            elif test == "N" or test == "n":
                N = test
            elif test == "O" or test == "o":
                O = test
            elif test == "P" or test == "p":
                P = test
            elif test == "Q" or test == "q":
                Q = test
            elif test == "R" or test == "r":
                R = test
            elif test == "S" or test == "s":
                S = test
            elif test == "T" or test == "t":
                T = test
            elif test == "U" or test == "u":
                U = test
            elif test == "V" or test == "v":
                V = test
            elif test == "W" or test == "w":
                W = test
            elif test == "X" or test == "x":
                X = test
            elif test == "Y" or test == "y":
                Y = test
            elif test == "Z" or test == "z":
                Z = test
            else:
                zero = 0

        context = {
            'findletter': findletter,
            'glossary': glossarydate,
            'provincefilter': provincefilter,
            'A': A,
            'B': B,
            'C': C,
            'D': D,
            'E': E,
            'F': F,
            'G': G,
            'H': H,
            'I': I,
            'J': J,
            'K': K,
            'L': L,
            'M': M,
            'N': N,
            'O': O,
            'P': P,
            'Q': Q,
            'R': R,
            'S': S,
            'T': T,
            'U': U,
            'V': V,
            'W': W,
            'X': X,
            'Y': Y,
            'Z': Z,
            'zero': zero

        }
        return render(request, 'glossary.html', context)


class BlogDetailView(DetailView, MultipleObjectMixin):
    model = Blog
    template_name = 'blogitems.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        object_list = Blog.objects.order_by('id')
        context = super(BlogDetailView, self).get_context_data(object_list=object_list, **kwargs)

        provincefilter = Province.objects.filter().first()

        context['provincefilter'] = provincefilter

        return context
