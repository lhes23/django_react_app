from django.http import HttpResponse

def index(request):
    return HttpResponse("Server running on port 8000")