"""Forms for registration, login, profile editing, and password changes."""
from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=150, help_text="Enter your full name.")
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["full_name", "username", "email", "password1", "password2"]

    def save(self, commit=True):
        """Split full name into first and last name before saving the user."""
        user = super().save(commit=False)
        full_name = self.cleaned_data["full_name"].strip()
        names = full_name.split(" ", 1)
        user.first_name = names[0]
        user.last_name = names[1] if len(names) > 1 else ""
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]


class StyledPasswordChangeForm(PasswordChangeForm):
    """PasswordChangeForm kept as a class so views can import a friendly name."""
