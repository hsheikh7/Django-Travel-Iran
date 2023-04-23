from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from website.forms import ContactForm

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            #email = form.cleaned_data['email']
            #message = form.cleaned_data['message']
            #print(name, subject, email, message)
            return HttpResponse('done')
        else: 
            return HttpResponse('Not Valid')
        
    form = ContactForm()
    return render(request, 'test.html' , {'form': form})
    
