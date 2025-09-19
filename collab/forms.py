from django import forms
from .models import CollabRequest


class CollaborateForm(forms.ModelForm):
    # Provide a message field that maps to the model's project_description
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), required=False)

    class Meta:
        model = CollabRequest
        # keep model fields minimal; `message` is handled separately
        fields = ('name', 'email')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.project_description = self.cleaned_data.get('message', '')
        if commit:
            instance.save()
        return instance
