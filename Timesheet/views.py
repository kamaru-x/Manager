from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def timesheet(request):
    context = {
        'page' : 'timesheet'
    }
    return render(request, 'timesheet/timesheet.html', context)