from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Transactions.models import Account, Category, Transaction
from datetime import datetime
from django.http import JsonResponse
from django.db.models import Sum

today = datetime.today()

# Create your views here.

@login_required
def add_category(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        title = request.POST.get('title')

        try:
            Category.objects.create(type=type,title=title)
            messages.success(request, 'Category created')
            return redirect('masters')

        except Exception as exception:
            messages.warning(request,str(exception))
            return redirect('add-category')

    context = {
        'page' : 'masters'
    }
    return render(request, 'masters/category.html', context)

@login_required
def delete_category(request,id):
    try:
        category = Category.objects.get(id=id)
        category.delete()
        messages.error(request, 'Category deleted')
    except Exception as exception:
        messages.error(request, str(exception))

    return redirect('masters')

@login_required
def add_account(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        bank = request.POST.get('bank')

        try:
            Account.objects.create(title=title, bank=bank)
            messages.success(request, 'Account added')
            return redirect('masters')

        except Exception as exception:
            messages.warning(request,str(exception))
            return redirect('add-account')

    context = {
        'page' : 'masters'
    }
    return render(request, 'masters/account.html', context)

@login_required
def delete_account(request,id):
    try:
        account = Account.objects.get(id=id)
        account.delete()
        messages.error(request, 'Account deleted')
    except Exception as exception:
        messages.error(request, str(exception))

    return redirect('masters')


@login_required
def transactions(request):
    transactions = Transaction.objects.all()
    
    # Get filter parameters
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    category_id = request.GET.get('category')

    # Apply filters if they exist
    if start_date:
        transactions = transactions.filter(date__gte=start_date)
    if end_date:
        transactions = transactions.filter(date__lte=end_date)
    if category_id:
        transactions = transactions.filter(category_id=category_id)

    # Order the transactions
    transactions = transactions.order_by('-date', '-id')

    # Calculate totals based on filtered transactions
    income = transactions.filter(type='Income').aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    expense = transactions.filter(type='Expense').aggregate(total_amount=Sum('amount'))['total_amount'] or 0
    balance = float(income) - float(expense)

    # Get all categories for the filter dropdown
    categories = Category.objects.all().order_by('type', 'title')

    context = {
        'page': 'transactions',
        'transactions': transactions,
        'income': income,
        'expense': expense,
        'balance': balance,
        'start_date': start_date,
        'end_date': end_date,
        'selected_category': category_id,
        'categories': categories
    }
    return render(request, 'transactions/transactions.html', context)


def fetch_categories(request):
    category_type = request.GET.get('type')
    categories = Category.objects.filter(type=category_type).values('id', 'title')
    return JsonResponse({'categories': list(categories)})


@login_required
def add_transaction(request):
    categories = Category.objects.all()
    accounts = Account.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        type = request.POST.get('type')
        category_id = request.POST.get('category')
        account_id = request.POST.get('account')
        amount = request.POST.get('amount')

        try:
            category = Category.objects.get(id=category_id)
            account = Account.objects.get(id=account_id)

            Transaction.objects.create(title=title, date=date, type=type, category=category, account=account, amount=amount)
            messages.success(request, 'transaction added')
            return redirect('transactions')

        except Exception as exception:
            messages.warning(request,str(exception))
            return redirect('add-transaction')

    context = {
        'page' : 'transactions',
        'today' : today,
        'categories' : categories,
        'accounts' : accounts
    }
    return render(request, 'transactions/transaction-add.html', context)

@login_required
def delete_transaction(request,id):
    try:
        transaction = Transaction.objects.get(id=id)
        transaction.delete()
        messages.error(request, 'Transaction deleted')
    except Exception as exception:
        messages.error(request, str(exception))

    return redirect('transactions')