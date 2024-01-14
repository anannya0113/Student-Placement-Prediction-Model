from django import forms


class Placement(forms.Form):

    CHOICES = [('1', 'Yes'), ('0', 'No')]

    Internships = forms.FloatField(label='Internships', min_value=0, max_value=10,
                              widget=forms.NumberInput(attrs={'class': 'form-control'}))
    CGPA = forms.FloatField(label='CGPA', min_value=0, max_value=10,
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    Hostel = forms.CharField(label='Hostel', widget=forms.RadioSelect(choices=CHOICES))

    HistoryOfBacklogs = forms.CharField(label='HistoryOfBacklogs', widget=forms.RadioSelect(choices=CHOICES))
    