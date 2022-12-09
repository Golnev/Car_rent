from django.forms import ModelForm, TextInput, Textarea, EmailInput

from .models import Comment, Contact


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'message', 'post')
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'name',
                    'type': 'text'
                }
            ),
            'message': Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'message',
                    'cols': '30',
                    'rows': '10',
                    'name': ''
                }
            )
        }


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Your Name'
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Your Email'
                }
            ),
            'message': Textarea(
                attrs={
                    'class': 'form-control',
                    'name': '',
                    'id': '',
                    'cols': '30',
                    'rows': '7',
                    'placeholder': 'Message'
                }
            )
        }
