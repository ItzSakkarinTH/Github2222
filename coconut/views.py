from django.shortcuts import render , HttpResponse

# Create your views here.
def IndexPage(request):
    return render(request, 'sakkarin.html')