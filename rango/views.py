from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    response_content = """
    Rango says hey there partner! Visit the <a href="/rango/about/">about page</a>.
    """
    return HttpResponse(response_content)

def about(request):
    response_content = """
    Rango says here is the about page. Go back to the <a href="/rango/">index page</a>.
    """
    return HttpResponse(response_content)
