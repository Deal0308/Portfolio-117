from django.shortcuts import render, redirect
from .models import Project, Experience
from .forms import ProjectForm

# Create your views here.

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects_list.html',{
        
        'projects': projects
                
    })

def project_new(request):
    form = ProjectForm(request.POST, request.FILES)
    if form.is_valid():
        project = form.save()
        return redirect('projects_list')
    else:
        form = ProjectForm()
        
    return render(request, 'projects/project_new.html', {
        'form': form
    })


def experience_list(request):
    experience = Experience.objects.all()
    return render(request, 'experience/experience_list.html', {
        'experience': experience
    })