from django.http import HttpResponse


def hello(request,name):
    return HttpResponse("<b> hello " + name + "<b>")
