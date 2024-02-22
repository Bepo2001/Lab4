from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
tax_rate=0.15
def index(request):
    return render(request, "interface/face.html")
def taxCal(request, price):
    return HttpResponse(f"Here is the total with tax {price+price*tax_rate}!")

def taxrate(request):
    return HttpResponse(f"the tax rate is {tax_rate*100}%")
