from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Profile, ListModel


@login_required
def home(request):
 user = request.user
 user_profile = request.user.profile
 user_list = ListModel.objects.filter(user_profile=user_profile, name="ToDo").first()
 if request.method == "POST":
  if request.POST.get("newItem"):
   #add new item to the to do list

   text = request.POST.get("new")
   if len(text) > 2:
    user_list.item_set.create(text=text,complete=False)

  elif request.POST.get("prog"):
   val = request.POST.get("prog")
   item = user_list.item_set.get(id=val)
   item.complete = True
   item.save()

  elif request.POST.get("end"):
   val = request.POST.get("end")
   item = user_list.item_set.get(id=val)
   item.delete()

  elif request.POST.get("endProg"):
   val = request.POST.get("endProg")
   item = user_list.item_set.get(id=val)
   item.delete()

  elif request.POST.get("logOut"):
   logout(request)

   return redirect("base:login")
  
  elif request.POST.get("shopping"):
   return redirect("base:shopping")
   

  return render(request, "home.html", {"user":user,"ls":user_list})
 else:
  return render(request, "home.html", {"user":user,"ls":user_list})

def myLogOut(request):
  if request.method == "POST":
   logout(request)

   return redirect("base:login")

  return render(request, "registration/logout.html", {})


def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   user = form.save()

   profile = Profile.objects.create(user=user)
   profile.save()

   ListModel.objects.create(user_profile=profile, name='ToDo')
   ListModel.objects.create(user_profile=profile, name='Shopping')
   


   return redirect("base:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})


@login_required
def shopping(request):
 user = request.user
 user_profile = request.user.profile
 user_list = ListModel.objects.filter(user_profile=user_profile, name="Shopping").first()
 if request.method == "POST":
  if request.POST.get("logOut"):
   logout(request)

   return redirect("base:login")
  
  elif request.POST.get("home"):
   return redirect("base:home")
  
  elif request.POST.get("newItem"):
   text = request.POST.get("new")
   if len(text) > 2:
    user_list.item_set.create(text=text,complete=False)

  elif request.POST.get("end"):
   val = request.POST.get("end")
   item = user_list.item_set.get(id=val)
   item.delete()



 return render(request,"shopping.html",{"user":user,"ls":user_list})
