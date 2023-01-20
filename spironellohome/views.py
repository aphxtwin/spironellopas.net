from django.shortcuts import render, HttpResponseRedirect

from formtools.wizard.views import SessionWizardView
from .forms import ProductSelectionForm, NameSurnameEmail
from .models import MarketPlaceProducts, User
# Create your views here.

def index(request):
    return render(request, 'spironellohome/homepage.html')

def marketplace(request):    
    products = MarketPlaceProducts.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'spironellohome/marketplace.html', context)

def product_detail(request, slug):
    detailed_product = MarketPlaceProducts.objects.filter(slug = slug)
    context = {
        'detailed_product':detailed_product
    }
    return render(request, 'spironellohome/producto.html', context)

class QuoteWizardView(SessionWizardView):
    form_list = [ProductSelectionForm, NameSurnameEmail]

    def get_template_names(self):
        return ['spironellohome/quote_wizard_step_1.html', 'spironellohome/quote_wizard_step_2.html']

    def done(self, form_list, **kwargs):
        product_form = form_list[0]
        user_form = form_list[1]
        if product_form.is_valid() and user_form.is_valid():
            product_choice = product_form.cleaned_data
            user = user_form.cleaned_data
            user_obj = User.objects.create(**user)
            user_obj.save()
            user_obj.products.add(*product_choice)
            return HttpResponseRedirect('success/')
        else:
            print("error")

    


