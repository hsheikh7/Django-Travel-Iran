from django import forms
from website.models import Contact
#from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    
    #captcha = CaptchaField() 
    class Meta: 
        model = Contact
        fields = ['name','email', 'subject', 'massage']
        #'__all__' - #['name','email'] - #exclude = ['name']


