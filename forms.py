from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=('empname','designation', 'empid', 'position')
        labels={
            'empname' : 'Emp Name',
            'empid': 'Emp ID'
        }

    def __init__(self, *args, **kwargs):
            super(EmployeeForm, self).__init__(*args, **kwargs)
            self.fields['position'].empty_label = "Choose"
           # self.fields['designation'].required = False  #Remove mandantory field
            # self.fields['position'].required = False




