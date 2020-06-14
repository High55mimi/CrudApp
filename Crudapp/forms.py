from django import forms
from .models import employee_details

class employee_add(forms.ModelForm):
    class Meta:
        model=employee_details
        fields= {'fullname','phone_number','e_code','eposition'}

    def __init__(self,*args,**kwargs):
        super(employee_add,self).__init__(*args,**kwargs)
        self.fields['eposition'].empty_label="Select Position"



