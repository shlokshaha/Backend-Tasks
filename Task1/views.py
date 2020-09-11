from django.shortcuts import render
from django.http import HttpResponse

list = [item for item in range(1,21)]



def home(request):
    context = {
        'list' : list
    }
    return render(request, 'Task1/home.html', context)

def case(request):
    first=int(request.GET.get('fno'))
    last=int(request.GET['lno'])
    m=[]
    if first<last:
        for i in range(first,last+1):
            m.append(i)
        context={
            'series':m
        }
        return render(request,'Task1/case.html',context)
    else:
        return HttpResponse("First Number should be less than the last number")