from django import forms
from django.core import validators
from first_app.models import Webpage

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z,])
    email = forms.EmailField()
    vmail = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, 
                                    validators=[validators.MaxLengthValidator(0)])

    ## adding clean_ to the from field names
    def clean_botcatcher(self):
        print(self.cleaned_data)
        data = self.cleaned_data['botcatcher']

        if len(data) > 0:
            raise forms.ValidationError('Bot catched')
        
        return data
    
    def clean(self) -> dict[str, any]:
        all_cleaned_data = super().clean()

        eml = all_cleaned_data['email']
        vml = all_cleaned_data['vmail']

        if eml != vml:
            raise forms.ValidationError("Email does not mathch")
        
        return all_cleaned_data


class WebFrom(forms.ModelForm):
    class Meta():
        model = Webpage
        fields = '__all__'
