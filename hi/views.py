from django.shortcuts import render

# Create your views here.


def home(request):
    
    return render(request, 'home.html')

def detail(request):
    k = request.GET["fulltext"]
    return render(request, 'detail.html', {'fulltext':k})