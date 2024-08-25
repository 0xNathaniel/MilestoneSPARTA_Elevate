from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpUserForm(UserCreationForm):
    # Remove Password-based authentication field
    usable_password = None
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control form-control-size"}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control form-control-size"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control form-control-size"}))
    
    class Meta:
        model = User    
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        
    def __init__(self, *args, **kwargs):
        super(SignUpUserForm, self).__init__(*args, **kwargs)
        
        self.fields["username"].widget.attrs['class'] = 'form-control form-control-size'
        self.fields["password1"].widget.attrs['class'] = 'form-control form-control-size'
        self.fields["password2"].widget.attrs['class'] = 'form-control form-control-size'