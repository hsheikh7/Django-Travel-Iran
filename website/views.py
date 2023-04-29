from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from website.forms import ContactForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        post = request.POST.copy()
        post['name'] = "Anonymous"
        request.POST = post
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your Ticket Submited Successfully. Thank You!')
        else: 
            messages.add_message(request, messages.ERROR, 'Ooops! Your Ticket Didnt Submit.')
    form = ContactForm() 
    return render(request, 'website/contact.html', {'form': form})


def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            massage = form.cleaned_data['massage']
            print(name, subject, email, massage)
            form.save()
            return HttpResponse('done')
        else: 
            return HttpResponse('Not Valid')
        
    form = ContactForm()
    return render(request, 'test.html' , {'form': form})
    
