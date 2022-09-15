from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

""" 
def paginateProjects(request, projects, results):
    """ # Pagination code (check Django Documenmtation for more info)
    
    #page = request.GET.get('page')
    #paginator = Paginator(projects, results) #projects is Querry

    #try:
     #   projects = paginator.page(page)
    #except PageNotAnInteger:
     #   page = 1
      #  projects = paginator.page(page)
    #except EmptyPage:
     #   page = paginator.num_pages
      #  projects = paginator.page(page)

    #this is use to control number of pagination shows at d bottom of the page
    #leftindex = (int(page) - 4)
    #if leftindex < 1:
#        leftindex = 1
    
    #rightindex = (int(page) + 5)

    #if rightindex > paginator.num_pages:
     #   rightindex = paginator.num_pages + 1

    #custom_range = range(leftindex, rightindex """)
   
    #return projects, custom_range


def searchProjects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query= request.GET.get('search_query')

    tags= Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
               Q(title__icontains=search_query)|
               Q(description__icontains=search_query)|
               Q(owner__name__icontains=search_query)|
               Q(Tags__in=tags)) #to search for name in many2many Model 
                                         #(Tags: is field name that links Tag model to Project Model)
    return projects, search_query
