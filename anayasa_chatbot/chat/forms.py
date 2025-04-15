# chat/forms.py

from django import forms
from .models import Feedback

class ChatForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Anayasa hakkında bir soru sorun...',
            'class': 'form-control'
        }),
        label=''
    )

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Yorumunuzu buraya yazın (isteğe bağlı)',
                'class': 'form-control'
            }),
        }


# chat/forms.py dosyasını düzenleyin veya oluşturun
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ChatForm(forms.Form):
    # Mevcut chat formu (zaten vardı)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Sorunuzu yazın...'}), label='')


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Form alanlarına Bootstrap stilleri ekle
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})