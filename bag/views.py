from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view that renders bag contents """
    
    return render(request, 'home/index.html')