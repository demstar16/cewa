from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=255)
    email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)