from django.shortcuts import render
from django.http import HttpResponse

from home.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

# Create your views here.
def index(request):
    return render (request, 'home/index.html')

def about(request):
    return render (request, 'home/about.html')

def service_3pl(request):
    return render (request, 'home/service_3pl.html')

def service_it(request):
    return render (request, 'home/service_it.html')   

def contactus(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            contact_subject = request.POST.get('contact_subject', '')
            contact_content = request.POST.get('contact_content', '')

            # Email the profile with the 
            # contact information
            #template = get_template('home/contactus_tr.html')
            template = get_template('home/contact_template.txt')
            
            context = { 'contact_name': contact_name,
                        'contact_email': contact_email,
                        'contact_subject': contact_subject,
                        'contact_content': contact_content,
                      }
            content = template.render(context)

            email = EmailMessage(
                contact_subject,  #subject
                content,                        #body
                contact_email,             #frome_email
                ['spot360.team@gmail.com'],     #to
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return render(request, 'home/contactus.html', {'form': form_class,})

    return render(request, 'home/contactus.html', {'form': form_class,})


# def contactus(request):
#     return render (request, 'home/contactus.html')

def account(request):
    return render (request, 'home/contactus.html')    
    