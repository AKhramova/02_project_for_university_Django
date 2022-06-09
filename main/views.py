from django.shortcuts import render
from django.views.generic.base import View
from .models import Questions
def index(request):
    if request.method == 'POST':
        if request.POST.get('phoneNumber') and request.POST.get('email') and request.POST.get('message'):
            post=Questions()
            post.name = request.POST.get('name')
            post.phoneNumber = request.POST.get('phoneNumber')
            post.email = request.POST.get('email')
            post.service = request.POST.get('service')
            post.message = request.POST.get('message')
            post.save()
    return render(request, 'main/index.html')
def gallery(request):
    return render(request, 'main/gallery.html')
def projects(request):
    return render(request, 'main/projects.html')
def certificates(request):
    return render(request, 'main/certificates.html')
def contacts(request):
    return render(request, 'main/contacts.html')
def project2(request):
    return render(request, 'main/project2.html')

