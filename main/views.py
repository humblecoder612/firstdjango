from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Tut,Cat,Series
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .forms import Newform
# Create your views here.
def single_link(request,single_link):
    categories=[c.cat_link for c in Cat.objects.all()]
    if single_link in categories:
        matching_series=Series.objects.filter(tut_cat__cat_link=single_link)
        ser_url={}
        for m in matching_series.all():
            part_one=Tut.objects.filter(tut_ser__tut_ser=m.tut_ser).earliest("tut_publish")
            ser_url[m]=part_one.tut_link
        return render(request,"main/category.html",context={"part_ones":ser_url})
    
    tuto=[t.tut_link for t in Tut.objects.all()]
    if single_link in tuto:
        this_tut=Tut.objects.filter(tut_link=single_link)
        return render(request,'main/tutorial.html',context={"tutorial":this_tut})
    return HttpResponse(f"{single_link} does not correspond to anything")





def homepage(request):
    return render(request=request, template_name="main/categories.html", context={"categories": Cat.objects.all()})


def register(request):
    if request.method=="POST":
        form=Newform(request.POST)
        if form.is_valid():
            user=form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f"yup:{username}")
            login(request,user)
            messages.info(request,f"you are in the page:{username}")
            return redirect("main:home")
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}:{form.error_messages[msg]}")
    form=Newform
    return render(request,"main/register.html",context={"form":form})


def logout_req(request):
    logout(request)
    messages.info(request,"logged out")
    return redirect("main:home")

def login_req(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"you are in the page:{username}")
                return redirect("/")
            else:
                messages.error(request,"Invalid user/password")
        else:
                messages.error(request,"Invalid user/password")
    form=AuthenticationForm()
    return render(request,"main/login.html",context={"form":form})