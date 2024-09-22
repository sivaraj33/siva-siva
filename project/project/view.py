from django.http import HttpResponse

def displayview(request):
    return HttpResponse('welcome')