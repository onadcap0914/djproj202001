from django import forms
from system_setting.models import Campus


class CampusForm(forms.ModelForm):

    class Meta:
        model = Campus
        fields = ['campus_code',
                  'campus_name',
                  'campus_add',
                  'registered_by',
                  # 'registered_date',
                  'updated_by',
                  'updated_date'
                  ]
        # https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = {'campus_code': forms.TextInput(attrs={'class': 'form-control d-inline'}),
                   'campus_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'campus_add': forms.TextInput(attrs={'class': 'form-control'}),
                   'registered_by': forms.HiddenInput(attrs={'class': 'form-control'}),
                   # 'registered_date': forms.HiddenInput(attrs={'class': 'form-control'}),
                   'updated_by': forms.HiddenInput(attrs={'class': 'form-control'}),
                   'updated_date': forms.HiddenInput(attrs={'class': 'form-control'}),
                   }
