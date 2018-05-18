# _*_ encoding:utf-8 _*_

from django import forms
from operation.models import UserOffer

class UserOfferForm(forms.ModelForm):
    class Meta:
        model=UserOffer
        fields=['name','mobile','course_name']