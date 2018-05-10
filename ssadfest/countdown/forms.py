from django import forms
from .models import Member

class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ['email', 'name', 'phone', 'city', 'company', 'specialization']
