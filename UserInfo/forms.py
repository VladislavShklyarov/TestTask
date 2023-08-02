from .models import UserInfo
from django.forms import ModelForm


class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'city', 'job', 'date_of_birth']