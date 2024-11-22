from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Transactions.models import Category, Account, Transaction
from Checklist.models import Task
from Todo.models import Todo
from django.db.models import Sum
from datetime import date
today = date.today()

# Create your views here.

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(date=today).order_by('-id')
    income_today = transactions.filter(type='Income').aggregate(total_income=Sum('amount'))['total_income'] or 0
    expense_today = transactions.filter(type='Expense').aggregate(total_expense=Sum('amount'))['total_expense'] or 0
    todos = Todo.objects.filter(date=today)
    todo_completed = Todo.objects.filter(date=today, is_completed=True)
    tasks = Task.objects.filter(date=today)
    task_completed = Task.objects.filter(date=today, is_completed=True)

    context = {
        'page' : 'dashboard',
        'transactions' : transactions,
        'income_today' : income_today,
        'expense_today' : expense_today,
        'todos' : todos,
        'todo_completed' : todo_completed,
        'tasks' : tasks,
        'task_completed' : task_completed
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def masters(request):
    categories = Category.objects.all()
    accounts = Account.objects.all()

    context = {
        'page' : 'masters',
        'categories' : categories,
        'accounts' : accounts
    }
    return render(request, 'masters/masters.html', context)