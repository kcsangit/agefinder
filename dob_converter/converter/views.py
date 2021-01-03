from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def home(request):
    return render(request,'converter/home.html')


def agefind(request):
    b1 = int(request.GET.get('years'))
    m1 = int(request.GET.get('months'))
    d1 = int(request.GET.get('days'))

    barsa1=int(b1)
    maina1=int(m1)
    din1 = int(d1)



    today = date.today()

    stringdate =  str(today)

    barsa2 = int(stringdate[0:4])
    maina2= int(stringdate[5:7])
    din2 = int(stringdate[8:10])

    if din1>din2:
        din2 = din2+30
        maina2=maina2-1
        din = din2-din1
        
    else:
        din = din2-din1
        
    if maina1>maina2:
        maina2=maina2+12
        barsa2=barsa2-1
        maina = maina2-maina1
        
    else:
        maina = maina2-maina1
        
    barsa = barsa2-barsa1








    return render(request, 'converter/agefind.html', { "years" : barsa ,"months":maina,"days":din })


