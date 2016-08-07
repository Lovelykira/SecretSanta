from django import forms
from django.contrib.auth import authenticate

from santa_app.models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField(label=u'Имя пользователя', widget=forms.TextInput(attrs={'class': 'login-username'}))
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput(attrs={'class': 'login-pass'}))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError(u'Упс, пользователя с таким именем и паролем не существует. Попробуй еще раз. ')
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user or None


class RegistrationForm(forms.ModelForm):
    #username = forms.CharField(label='Имя пользователя')
    password1 = forms.CharField(label=u'Пароль', widget=forms.PasswordInput(attrs={'class': 'registr-pass1'}))
    password2 = forms.CharField(label=u'Еще раз пароль', widget=forms.PasswordInput(attrs={'class': 'registr-pass2'}))

    #real_name = forms.CharField(label='Настоящее имя')
    #fav_present = forms.CharField(label='Лучший подарок, который тебе дарили', widget=forms.TextInput)
    class Meta:
        model = MyUser
        fields = ('username', 'real_name', 'fav_film', 'fav_game', 'fav_color', 'fav_present', 'hobbies', 'key_words')
        widgets = {'real_name': forms.TextInput(attrs={'class': 'reqistr-real-name'}),
                   'username': forms.TextInput(attrs={'class': 'reqistr-username'}),
                   'fav_film': forms.TextInput(attrs={'class': 'reqistr-fav-film'}),
                   'fav_game': forms.TextInput(attrs={'class': 'reqistr-fav-game'}),
                   'fav_color': forms.TextInput(attrs={'class': 'reqistr-fav-color'}),
                   'fav_present': forms.TextInput(attrs={'class': 'reqistr-fav-present'}),
                   'hobbies': forms.Textarea(attrs={'class': 'reqistr-hobbies'}),
                   'key_words': forms.Textarea(attrs={'class': 'reqistr-key-words'}),
                   }

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return self.cleaned_data


class PrivateOfficeChangeForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ( 'real_name', 'fav_film', 'fav_game', 'fav_color', 'fav_present', 'hobbies', 'key_words')
        widgets = {'real_name': forms.TextInput(attrs={'class': 'reqistr-real-name'}),
                   'fav_film': forms.TextInput(attrs={'class': 'reqistr-fav-film'}),
                   'fav_game': forms.TextInput(attrs={'class': 'reqistr-fav-game'}),
                   'fav_color': forms.TextInput(attrs={'class': 'reqistr-fav-color'}),
                   'fav_present': forms.TextInput(attrs={'class': 'reqistr-fav-present'}),
                   'hobbies': forms.Textarea(attrs={'class': 'reqistr-hobbies'}),
                   'key_words': forms.Textarea(attrs={'class': 'reqistr-key-words'}),
                   }