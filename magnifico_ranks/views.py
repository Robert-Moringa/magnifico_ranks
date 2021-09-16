from django.shortcuts import render

# Create your views here.
def home(request):
    title='Welcome in a array of superb projects that are awaiting your genuine vote.'
    return render(request, 'index.html', {'title':title,})