from django.shortcuts import render
from django.http import HttpResponse
from Second.models import AccessRecord,WebPage
def index(request):
    webpage=WebPage.objects.order_by('name')
    my_dict={'webpage_records':webpage}
    return render(request,'Second_app/index.html',context=my_dict)
