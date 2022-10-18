from distributed import Sub
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import smtplib as s
from myapp.form import PictureForm


def homepage(request):
    
    if request.method == 'POST':
        form = PictureForm(request.POST)
        if form.is_valid():
            
            cd = form.cleaned_data
            
            if cd['EmailChoice'] == 'sidqazwsx801@gmail.com':
                ob = s.SMTP('smtp.gmail.com',587)
                ob.ehlo()
                ob.starttls()
                ob.login('sidqazwsx801@gmail.com','losrpddvyrqioybl')

                sub = cd['sub']
                body = cd['body']
                emails = cd['email']
                
                message = "subject:{}\n\n{}".format(sub,body)
                
                lst = emails.split(",")
                print(message)
                print(lst)
                

                ob.sendmail('sidqazwsx801@gmail.com',lst,message)
                ob.quit()
        
    
        if cd['EmailChoice'] == 'shidharth030599@gmail.com':
                ob = s.SMTP('smtp.gmail.com',587)
                ob.ehlo()
                ob.starttls()
                ob.login('shidharth030599@gmail.com','ijcsczqlbzxchsvr')

                sub = cd['sub']
                body = cd['body']
                emails = cd['email']
                
                message = "subject:{}\n\n{}".format(sub,body)
                
                lst = emails.split(",")
                print(lst)
                

                ob.sendmail('shidharth030599@gmail.com',lst,message)
                ob.quit()

        if cd['EmailChoice'] == 'shidharth030599@gmail.com':
                ob = s.SMTP('smtp.gmail.com',587)
                ob.ehlo()
                ob.starttls()
                ob.login('shidharth030599@gmail.com','ijcsczqlbzxchsvr')

                sub = cd['sub']
                body = cd['body']
                emails = cd['email']
                
                message = "subject:{}\n\n{}".format(sub,body)
                
                lst = emails.split(",")
                print(lst)
                

                ob.sendmail('shidharth030599@gmail.com',lst,message)
                ob.quit()

                return render(request,'myapp/sent.html')
    else:
        form = PictureForm()
        return render(request,'myapp/homepage.html',{'form':form})
    
        
        
        
        

    
    return render(request,'myapp/homepage.html')
# Create your views here.
