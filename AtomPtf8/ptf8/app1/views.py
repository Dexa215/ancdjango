from django.http import HttpResponse

def indexapp1(request):
    return HttpResponse("Hello, world. You're at the app1 index.")


