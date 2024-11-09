from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.http import HttpResponse





def index(request):
    if request.method == "POST":
        data = request.POST
        p_company = data.get('p_company')
        p_name = data.get('p_name')
        p_email = data.get('p_email')
        p_description = data.get('p_description')

        
        People.objects.create(
            p_company = p_company,  
            p_name = p_name,
            p_email = p_email,
            p_description = p_description,
            )

        return redirect('/index/')
    queryset = People.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(p_company__icontains = request.GET.get('search'))
    context = {'index': queryset}


    return render(request,'index.html',context)



def update_people(request, id):
    queryset = People.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        p_company = data.get('p_company')
        p_name = data.get('p_name')
        p_email = data.get('p_email')
        p_description = data.get('p_description')

        queryset.p_company = p_company  
        queryset.p_name = p_name
        queryset.p_email = p_email
        queryset.p_description = p_description

        queryset.save() 
        return redirect('/index/')


    context = {'people': queryset}
    return render(request , 'update.html',context)




def delete_people(request , id):
    queryset = People.objects.get(id = id)
    queryset.delete()
    return redirect('/index/')