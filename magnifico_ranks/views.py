from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Project
from .forms import EditProfileForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer


# Create your views here.
def home(request):
    projects=Project.objects.all()
    title='Welcome in a array of superb projects that are awaiting your genuine vote.'
    return render(request, 'index.html', {'title':title, 'projects':projects})

def profile(request):
    title='Build your profile'
    current_user = request.user
    profile=Profile.objects.all()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=current_user.profile)
        print(form.is_valid())
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user =current_user
            profile.project =Project.get_project_by_user(current_user)
            profile.save()
        return redirect('profile')

    else:
        form = EditProfileForm()
    
    return render(request, 'profile.html', {'title':title, 'profile':profile,'form':form})

class profileList(APIView):
    def get(self, request, format=None):
        all_profiles= Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)