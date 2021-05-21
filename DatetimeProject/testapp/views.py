from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def datetimeinfo(request):
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))
    msg='<h1> Hello Gautam very '
    if h<12:
        msg=msg+'Good Morning </h1><hr>'
    elif  h<16:
        msg=msg+'Good Afternoon</h1><hr>'
    elif  h<23:
        msg=msg+'Good Evening</h1><hr>'
    else:
        msg=msg+'Good Night</h1><hr>'
    msg=msg+'<h1> Now Server Time is :'+str(date)+'</h1>'
    return HttpResponse(msg)
