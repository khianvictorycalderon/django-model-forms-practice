from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "name",
            "email",
            "age"
        ]

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if not any(character.isalpha() for character in name):
            raise forms.ValidationError("Enter a name containing at least one letter.")
        if any(not (character.isalpha() or character in " '-") for character in name):
            raise forms.ValidationError(
                "Name can contain only letters, spaces, apostrophes, and hyphens."
            )
        return name

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        domain = email.rsplit("@", 1)[-1]
        if "." not in domain:
            raise forms.ValidationError("Enter an email address with a valid domain.")
        return email

    def clean_age(self):
        age = self.cleaned_data["age"]
        if not 1 <= age <= 120:
            raise forms.ValidationError("Age must be between 1 and 120.")
        return age