from django.shortcuts import render,redirect
from django.db.models import Sum
from .models import TrackingHistory,CurrentBalance
 
# Create your views here.

def index(request):
    if request.method=="POST":
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        expense_type = "CREDIT"
        current_balance,_ = CurrentBalance.objects.get_or_create(id=1)
        if float(amount) < 0:
            expense_type = "DEBIT"

        tracking_history = TrackingHistory.objects.create(
            amount = amount,
            expense_type = expense_type,
            current_balance = current_balance,
            description = description 
            )
        
        current_balance.current_balance += float(tracking_history.amount)
        current_balance.save()
        
        print(description,amount)
        return redirect('/')
    
    current_balance,_ = CurrentBalance.objects.get_or_create(id=1)
    #Aggreate all to sum 
    income = 0
    expense = 0

    for tracking_history in TrackingHistory.objects.all():
        if tracking_history.expense_type == "CREDIT":
            income += tracking_history.amount 
        else:
            expense += tracking_history.amount
    #Track Transaction history 
    context = {'income':income,
               'expense':expense,
               'transactions': TrackingHistory.objects.all(),
               'current_balance': current_balance}
    
    return render(request,'index.html',context)


def delete_transaction(request,id):
    tracking_history = TrackingHistory.objects.filter(id=id)
    if tracking_history.exists():
        current_balance,_ = CurrentBalance.objects.get_or_create(id=1)
        tracking_history = tracking_history[0]
        current_balance.current_balance = current_balance.current_balance - tracking_history.amount
        current_balance.save()

    tracking_history.delete()
    return redirect('/')