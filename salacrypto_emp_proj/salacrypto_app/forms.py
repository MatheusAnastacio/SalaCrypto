from django import forms

from .models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['dono'].initial = self.user
            self.fields['dono'].widget = forms.HiddenInput()