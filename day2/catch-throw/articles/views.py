from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def detail(request, num, id):
    context = {
        'id':id,
        'num':num
    }
    return render(request, 'articles/detail.html', context)