from .models import Footer, InsuranceList

def base_template(request):
    foot_data = Footer.objects.all()
    return {'footer': foot_data}

