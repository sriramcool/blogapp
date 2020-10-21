from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import tech_blog

# I have provided the html page along with this dev sir

def tech(request): #collect all blog posts and send to the browser
    
    techs = tech_blog.objects.all()
    techs = techs[::-1] #used to make appear new post in front
    return render(request, 'tech.html', {'tech_contents':techs}) #tech_contents list passed in htmp page

def explanation(request):

    if request.method =='GET':
        name = request.GET.get('name')

    m = tech_blog.objects.get(name = name)
    q1 = m.q1
    desc1 = m.desc1
    q2 = m.q2
    desc2 = m.desc2
    q3 = m.q3
    desc3 = m.desc3

    try:
        image1 = m.image2.url
    except:
        image1 = "none"
        print("image1 not found")

    try:
        image2 = m.image3.url
    except:
        image2 = "none"
        print("image2 not found")


    return render(request, 'tech_blog.html', {'desc1':desc1, 'desc2':desc2, 'desc3':desc3, 
    'image1':image1, "image2":image2, 
    "q1":q1, "q2":q2, "q3":q3
    })

def like(request):
    pass
