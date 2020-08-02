from django import forms

class ContactForm(forms.Form):
    To_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    count = forms.IntegerField(required=True)