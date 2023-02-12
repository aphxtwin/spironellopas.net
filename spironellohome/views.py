from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from formtools.wizard.views import SessionWizardView
from .forms import ProductSelectionForm, QuoteForm, CarForm, HouseForm
from .models import InsuranceList, VisitorData, Car, LearningArticles, Section
# Create your views here.

class IndexView(TemplateView):
    '''
    This class is used to render the homepage
    '''
    template_name = 'spironellohome/homepage.html'

class LearningView(TemplateView):
    '''
    This class is used to render the articles section
    '''
    template_name = 'spironellohome/learning.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['learning_articles'] = LearningArticles.objects.all()
        return context
    
class DetailedArticle(TemplateView):
    '''
    This class is used to render the detailed article
    '''
    template_name = 'spironellohome/detailed_article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_slug = self.kwargs['slug']
        article_id = LearningArticles.objects.get(slug = article_slug)
        context['slug'] = LearningArticles.objects.filter(slug = article_slug)
        context['sections'] = Section.objects.filter(article = article_id)
        return context
    

class MarketplaceView(TemplateView):
    '''
    This class is used to render the marketplace
    '''
    template_name = 'spironellohome/marketplace.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = InsuranceList.objects.all()
        return context

class ProductDetailView(TemplateView):
    '''
    This class is used to render the product detail page
    '''
    template_name = 'spironellohome/producto.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detailed_product'] = InsuranceList.objects.filter(slug = self.kwargs['slug'])
        return context

# Forms and templates for the QuoteWizard
FORMS = [
    ("ProductSelection", ProductSelectionForm),
    ("CarForm", CarForm),
]
TEMPLATES = {
    "ProductSelection": "spironellohome/quote-wizard-step-0.html",
    "CarForm": "spironellohome/quote-wizard-car.html",
}
class QuoteWizardView(SessionWizardView):
    '''
    This view renders a multistep form for the user to get a quote
    '''
    # the list of forms that will be used in the wizard
    form_list = FORMS
    

    def get_template_names(self):
        '''
        This method is used to get the template name for each step
        '''
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        cleaned_data = self.get_cleaned_data_for_step('ProductSelection')
        products = cleaned_data.get('products')
        return render(self.request,'spironellohome/success_quote_wizard.html',{
            'form_data': [form.cleaned_data for form in form_list],
            })    



