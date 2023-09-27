from django.shortcuts import render
from random import sample
# Create your views here.
def hello(request):
    print('hello')
    dict1 = {'lst' : [1,1,1,1,1,2,2,2,2]}
    return render(request, 'articles/hello.html', dict1)

def lotto(request):
    data = {'nums' : sorted(sample(range(1, 46), 6))}
    print(data)
    return render(request, 'articles/lotto.html', data)

def date(request):
    return render(request, 'articles/date.html')

