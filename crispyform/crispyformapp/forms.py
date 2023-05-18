from django import forms
from crispyformapp.models import Customer,GENDER_OPTIONS

class CustomerForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_OPTIONS,widget=forms.RadioSelect,initial='male')
    class Meta:
        model = Customer
        fields = '__all__'


