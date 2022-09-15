from .models import Skill, Profile
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProfiles(request, profiles, results):
    # Pagination code (check Django Documenmtation for more info)
    
    page = request.GET.get('page')
    paginator = Paginator(profiles, results) #projects is Querry

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    #this is use to control number of pagination shows at d bottom of the page
    leftindex = (int(page) - 4)
    if leftindex < 1:
        leftindex = 1
    
    rightindex = (int(page) + 5)

    if rightindex > paginator.num_pages:
        rightindex = paginator.num_pages + 1

    custom_range = range(leftindex, rightindex)
   
    return custom_range, profiles


def searchProfile(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query= request.GET.get('search_query')
    
    skills = Skill.objects.filter(name__icontains=search_query)
    profiles = Profile.objects.distinct().filter(
                Q(name__icontains=search_query) | 
                Q(short_intro__icontains=search_query) |
                Q(skill__in=skills)
                )

    return profiles, search_query