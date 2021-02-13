from django.shortcuts import render, redirect
from .models import Numbers
from django.contrib import messages
import random
# Create your views here.
def home(request):
     return render (request, 'calc/home.html')

def secret(request):
     nums = Numbers.objects.get(pk=1)
     return render (request, 'calc/secret.html',{'nums':nums})

def secsub(request):
     nums = Numbers.objects.get(pk=2)
     return render (request, 'calc/secret.html',{'nums':nums})

def calc(request):
     nums = Numbers.objects.get(pk=1)
     context = {
          'nums' : nums,
     }
     if request.method == "POST":
          if not request.POST.get('result'):
               messages.warning(request, 'Please enter an answer!')
          elif nums.num_1 + nums.num_2 == int(request.POST.get('result')):
               print('horray')
               messages.success(request, 'Right answer!')
               nums.num_1 = random.randint(1,15)
               nums.num_2 = random.randint(1,15)
               nums.result += 5
               nums.save()

          else:
               print('Incorrect')
               messages.warning(request, 'Incorrect!')
     if nums.result == 100:
          nums.result = 0
          nums.save()
          return redirect ('secret')

     return render (request, 'calc/calc.html', context)

def sub(request):
     nums = Numbers.objects.get(pk=2)
     context = {
          'nums' : nums,
     }
     if request.method == "POST":
          if not request.POST.get('result'):
               messages.warning(request, 'Please enter an answer!')
          elif nums.num_1 - nums.num_2 == int(request.POST.get('result')):
               print('horray')
               messages.success(request, 'Right answer!')
               nums.num_1 = random.randint(1,15)
               nums.num_2 = random.randint(0,nums.num_1)
               nums.result += 5
               nums.save()

          else:
               print('Incorrect')
               messages.warning(request, 'Incorrect!')
     if nums.result == 100:
          nums.result = 0
          nums.save()
          return redirect ('secsub')

     return render (request, 'calc/sub.html', context)