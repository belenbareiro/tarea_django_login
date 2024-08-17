from django import forms


class TaskCreationForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255)
    content = forms.CharField(label="Content", widget=forms.Textarea())
