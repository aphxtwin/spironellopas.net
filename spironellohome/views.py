from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from formtools.wizard.views import SessionWizardView
from .forms import  QuoteForm, CarForm, HouseForm, BusinessForm, TripForm, CaucionForm, BasePjForms
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



class QuoteSelectionView(TemplateView):
    '''
    This class consists of the multistep form to get the quote
    '''
    template_name = 'spironellohome/cotizacion-step0.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_listed_products'] = InsuranceList.objects.all()
        return context
    


