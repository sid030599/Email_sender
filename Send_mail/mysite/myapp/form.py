from django import forms

class PictureForm(forms.Form):
    CHOICES=[('shidharth030599@gmail.com','shidharth030599@gmail.com'),
         ('sidqazwsx801@gmail.com','sidqazwsx801@gmail.com'),
         ('shidharth030599@gmail.com','siddharth030599@gmail.com')]

    EmailChoice= forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    sub = forms.CharField()
    email = forms.EmailField()
    body = forms.CharField() 
