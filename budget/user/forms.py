from  django import forms
from  . models import income , expense


class DateInput(forms.DateInput):
    input_type = 'date'


class IncomeForms(forms.ModelForm):
    class Meta:
        model=income
        fields='__all__'
        widgets = {
            'date': DateInput()
        }   
        labels = {
            'iteam':'Enter iteam',
            'amount':'Enter Amount',
            'date':'Select date',
        }

class ExpenseForms(forms.ModelForm):
    class Meta:
        model=expense
        fields='__all__'
        widgets = {
            'date': DateInput()
        }
        labels = {
            'iteam':'Enter iteam',
            'amount':'Enter Amount',
            'date':'Select date',
        }