from django.shortcuts import render, redirect
from projects.models import Project, Tag
from .forms import ProjectForm, ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utis import searchProjects



def projects(request):
    projects, search_query = searchProjects(request) # Function unpacking (from utis.py)

    """projects, custom_range  = paginateProjects(request, projects, 3) #pagination"""


    context= {'projects': projects, 'search_query': search_query}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    
    form = ReviewForm() 
    
    if request.method == 'POST':             
        form = ReviewForm(request.POST)
        if form.is_valid:   # Check if the Data is Valid
            reviews = form.save(commit=False)
            reviews.project = projectObj
            reviews.owner = request.user.profile
            reviews.save()

#getvoteCount is the method we created in the  Project Model 
# and we dont use Parenthensis for it cos we use "property Decorator on it"
            projectObj.getvoteCount  

            messages.success(request, 'Your Review Was Successfully Submitted!')
            return redirect('project', pk=projectObj.id) # pk=projectObj.id was used here because we r redirectong to a page that requires ID

    return render (request, 'projects/single-project.html', {'project': projectObj, 'form': form})


@login_required(login_url="login")
def CreateProject (request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':  # If the form has been submitted...
        form = ProjectForm(request.POST, request.FILES)   # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            project=form.save(commit=False) 

            #linked new created project to the current USER
            project.owner = profile  # linked new project that user just created to the user Profile
            project.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def updateProject (request, pk):
    profile = request.user.profile   # assign the current user ID to profile
    project = profile.project_set.get(id=pk) #one to many (profile and projects)
    form = ProjectForm(instance=project) #fill the ProjectForm with existing data

    if request.method == 'POST':  # If the form has been submitted...
        form = ProjectForm(request.POST, request.FILES, instance=project)   # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return redirect('account')
    
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile 
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    context = {'object': project}
    return render (request, 'delete_template.html', context)