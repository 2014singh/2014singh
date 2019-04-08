from django import forms

class Emp_insert_Form(forms.Form):
    emp_id = forms.IntegerField(
        label="Enter Your Id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Enter Your Id"
            }
        )
    )
    emp_first_name=forms.CharField(
        label="Enter First Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':"First Name"
            }
        )
    )
    emp_last_name = forms.CharField(
        label="Enter Last Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Last Name"
            }
        )
    )
    emp_mobile_number = forms.IntegerField(
        label="Enter Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Your Mobile Number"
            }
        )
    )
    emp_email_id = forms.EmailField(
        label="Enter Email Id",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Your Email Id"
            }
        )
    )
    emp_salary = forms.IntegerField(
        label="Enter Your Salary",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Your Salary"
            }
        )
    )
    emp_location = forms.CharField(
        label="Enter Your Location",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Your location"
            }
        )
    )
    emp_position=forms.CharField(
        label="Enter Your Position",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':"Your Position"
            }
        )
    )

class Emp_update_form(forms.Form):
    emp_id = forms.IntegerField(
        label="Enter Your Id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Enter Your Id"
            }
        )
    )
    emp_location = forms.CharField(
        label="Enter Your Location",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Your location"
            }
        )
    )


class Emp_delete_form(forms.Form):
    emp_id = forms.IntegerField(
        label="Enter Your Id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Enter Your Id"
            }
        )
    )