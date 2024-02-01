from django.shortcuts import render, redirect
from pages.forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def about(request):
    return render(request, 'pages/about.html') 

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email_from = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('pages/email.html', request.POST)
            
            # send email('The Subject', 'The Message', 'from email', 'michaeldeal1010@gmail.com')
            send_mail('Message from ' + name, message, email_from, ['Michaeldeal1010@gmail.com'], html_message=html)
            


            return redirect('about')
            # send email
        else:
            print('the message can not be sent. Please try again.')
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})

