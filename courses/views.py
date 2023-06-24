from datetime import date,datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Course,Category

data = {
    "programlama" : "Programlama Kategorisine Ait Kurs Listesi",
    "web-gelistirme" : "Web Geliştirme Kategorisine Ait Kurs Listesi",
    "mobil":"Mobil Kategorisine Ait Kurs Listesi",
    "mobil-uygulama":"Mobil Uygulama Kategorisine Ait Kurs Listesi"
}

db = {
    "courses": [
        {
            "title":"javascript kursu",
            "description":"javascript kurs açıklaması",
            "imageUrl":"java_img.jpg",
            "slug": "javascript-kursu",
            "date":datetime.now(),
            "isActive": True,
            "isUpdated":False
        },
        {
            "title":"python",
            "description":"python kurs açıklaması",
            "imageUrl":"python_img.jpg",
            "slug": "python-kursu",
            "date":date(2022,9,10),
            "isActive": True,
            "isUpdated":False
        },
        {
            "title":"web geliştirme kursu",
            "description":"web geliştirme kurs açıklaması",
            "imageUrl":"web_img.jpg",
            "slug": "web-gelistirme-kursu",
            "date":date(2022,8,10),
            "isActive": True,
            "isUpdated":True
        }
    ],
    "categories":[
        {"id": 1,"name":"programlama","slug":"programlama"},
        {"id": 2,"name":"web gelistirme","slug":"web-gelistirme"},
        {"id": 3,"name":"mobil uygulamalar", "slug":"mobil-uygulamalar"}
    ]
}


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

def getCoursesByCategory(request, category_name):
    
    try:
        category_text = data[category_name]
        
        return render(request,'courses/kurslar.html',{
            'category' : category_name,
            'category_text' : category_text
        })
    except:
        return HttpResponseNotFound("<h1>Yanlış Kategori Seçimi</h1>")


def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())
    if (category_id > len(category_list)):
        return HttpResponseNotFound("Yanlış Kategori Seçimi")
    category_name = category_list[category_id-1]

    redirect_url = reverse('courses_by_category', args=[category_name])
    return redirect(redirect_url)
    
