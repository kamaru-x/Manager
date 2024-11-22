from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Journal.models import Journal
from datetime import datetime
from django.db.models import Count, Sum

# Create your views here.

@login_required
def journals(request):
    today = datetime.today().date()

    if not Journal.objects.filter(date=today).exists():
        Journal.objects.create(title="Nothing today?", content="", date=today)

    journals = Journal.objects.all().order_by('-date')

    context = {
        'page' : 'journals',
        'journals' : journals,
    }
    return render(request, 'journal/journals.html', context)

@login_required
def journal(request,id):
    journal = Journal.objects.get(id=id)

    context = {
        'page' : 'journals',
        'journal' : journal
    }
    return render(request, 'journal/journal.html', context)