from .models import Footer, MarketPlaceProducts

def base_template(request):
    foot_data = Footer.objects.all()
    return {'footer': foot_data}

