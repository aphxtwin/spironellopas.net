from django.shortcuts import render, HttpResponseRedirect

from formtools.wizard.views import SessionWizardView
from .forms import ProductSelectionForm, QuoteForm, CarForm
from .models import InsuranceList, Quote, Car
# Create your views here.

def index(request):
    return render(request, 'spironellohome/homepage.html')

def marketplace(request):    
    products = InsuranceList.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'spironellohome/marketplace.html', context)

def product_detail(request, slug):
    detailed_product = InsuranceList.objects.filter(slug = slug)
    context = {
        'detailed_product':detailed_product
    }
    return render(request, 'spironellohome/producto.html', context)


class QuoteWizardView(SessionWizardView):
    form_list = [ProductSelectionForm, QuoteForm]

    def get_template_names(self):
        return ['spironellohome/quote_wizard_step_1.html', 'spironellohome/quote_wizard_step_2.html'] 


    


