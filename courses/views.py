from datetime import date,datetime
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Course,Category
from django.core.paginator import Paginator


def index(request):
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()
    
    # for kurs in db["courses"] :
    #     if kurs["isActive"] == True:
    #         kurslar.append(kurs)
    

    return render(request, 'courses/index.html', {
        'categories' : kategoriler,
        'courses': kurslar
    })


def programlama(request):
    return HttpResponse('Programlama kurs listesi')

def mobiluygulamalar(request):
    return HttpResponse('Mobil uyhulamalar kurs listesi')

def details(request, slug):
    course = get_object_or_404(Course, slug = slug)
    context = {        
        'course': course
    }
    return render(request, 'courses/details.html',context)

def getCoursesByCategory(request, slug):
    
    kurslar = Course.objects.filter(categories__slug = slug, isActive = True).order_by("title")
    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar,2)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)

    return render(request,'courses/index.html',{
        'categories' : kategoriler,
        'page_obj': page_obj,
        'seciliKategori': slug
    })



    
