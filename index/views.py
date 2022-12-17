from django.shortcuts import render

# Create your views here.

def index(request):
    # return HttpResponse("Hello, World!")
    return render(request, 'Index.html')