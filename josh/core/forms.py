from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Message

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email','password1','password2')


    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
    

class LoginForm(AuthenticationForm):
     username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
     
     password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class':'w-full py-4 px-6 rounded-xl'
        }))
     
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

    from django import forms

# class ContactForm(forms.Form):
#     sender_name = forms.CharField(max_length=100)
#     sender_email = forms.EmailField()
#     sender_phone = forms.CharField(max_length=15)
#     message_content = forms.CharField(widget=forms.Textarea)

# class MessageForm(forms.ModelForm):
#     class Meta:
#         model = Message
#         fields = ['sender_name', 'sender_email', 'sender_phone', 'content']
#         widgets = {
#             'sender_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter your name'}),
#             'sender_email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Enter your email'}),
#             'sender_phone': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter your phone number'}),
#             'content': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Type your message here'}),
#         }
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('sender_name', 'sender_email', 'sender_phone', 'content')
        widgets = {
            'sender_name': forms.TextInput(attrs={
                'placeholder': 'Your Username',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'sender_email': forms.EmailInput(attrs={
                'placeholder': 'Your Email',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'sender_phone': forms.TextInput(attrs={
                'placeholder': 'Your phone number',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'I need this --- outfit',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
        }
         
       
   