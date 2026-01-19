from django import forms

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField()
#
class SetNewPasswordForm(forms.Form):
    new_pwd1 = forms.CharField(widget=forms.PasswordInput)
    new_pwd2 = forms.CharField(widget=forms.PasswordInput)
    #
    def clean(self):
        cleaned_data = super().clean()
        pw1 = cleaned_data.get('new_pwd1')
        pw2 = cleaned_data.get('new_pwd2')
        #
        if pw1 != pw2:
            raise forms.ValidationError("le password non corrispondono")
        return cleaned_data