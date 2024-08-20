from django.shortcuts import render , HttpResponse

# Create your views here.
def cocoPage(request):
    return render(request, 'index.html')
def IndexPage(request):
    return render(request, 'sakkarin.html')