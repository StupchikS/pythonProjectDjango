from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    context = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))


