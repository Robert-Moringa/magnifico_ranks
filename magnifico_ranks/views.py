from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projects=Project.objects.all()
    title='Welcome in a array of superb projects that are awaiting your genuine vote.'
    return render(request, 'index.html', {'title':title, 'projects':projects})