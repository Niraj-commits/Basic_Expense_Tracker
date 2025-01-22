from django.shortcuts import render,HttpResponse,redirect
from .models import *

# Create your views here.

def view(request):
    expenses = account.objects.all()
    context = {"expenses":expenses}
    return render(request,'view.html',context)

def create_expense(request):
    
    if request.method == "POST":
        expense = request.POST.get('expense')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        type = request.POST.get('type')
        account.objects.create(name=expense,description=description,amount = amount,type=type)
        return redirect('/')
    return render(request,'create_expense.html')

def create_income(request):
    if request.method == "POST":
         income = request.POST.get('income')
         description = request.POST.get('description')
         amount = request.POST.get('amount')
         type = request.POST.get('type')
         account.objects.create(name=income,description=description,amount=amount,type=type)
         return redirect('/')
    return render(request,'create_income.html')

def edit(request,pk):
    task = account.objects.get(pk = pk)
    context = {"tasks": task}
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        type = request.POST.get('type')
        task.name = name
        task.description = description
        task.amount = amount
        task.type = type
        task.save()
        return redirect('/')
    return render(request,'edit.html',context)

 
def delete(request,pk):
    task = account.objects.get(pk = pk)
    task.delete()
    return redirect('/')
