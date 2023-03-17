from django import forms


class AttendanceForm(forms.Form):
    attendance_checkbox = forms.BooleanField(
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'attendance-disappear'}),
        label=''
    )
