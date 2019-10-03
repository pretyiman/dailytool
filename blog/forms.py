from django import forms
from blog.models import Expenses,Income,Contacts, list,catagory,subcatagory,item,warehouse,rack
from django.contrib.auth.forms import authenticate
from django.utils import formats
from dal import autocomplete
from django.forms.widgets import DateTimeInput
# from tempus_dominus.widgets import DatePicker
# from bootstrap_datepicker_plus import DatePickerInput
# import django_filters

class ItemForm(forms.ModelForm):
    Barcode = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True, max_length=16)
    Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True, max_length=100)
    Catagory = forms.ModelChoiceField(widget=autocomplete.ModelSelect2(attrs={'class':'form-control'}),queryset=catagory.objects.all())
    Sub_Catagory= forms.ModelChoiceField(widget=autocomplete.ModelSelect2(attrs={'class':'form-control'}),queryset=subcatagory.objects.all())
    Sale_Price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Numbers only'}),required=True)
    Stock = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Numbers only'}),required=True,)
    Warehouse = forms.ModelChoiceField(widget=autocomplete.ModelSelect2(attrs={'class':'form-control'}),queryset=warehouse.objects.all())
    Rack = forms.ModelChoiceField(widget=autocomplete.ModelSelect2(attrs={'class':'form-control'}),queryset=rack.objects.all())

    class Meta:
        model = item
        fields = '__all__'

class RackForm(forms.ModelForm):
    Rack = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True, max_length=100)

    class Meta:
        model = rack
        fields = '__all__'

class WarehouseForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True, max_length=100)

    class Meta:
        model = warehouse
        fields = ('Name',)

class CatagoryForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True, max_length=100)

    class Meta:
        model = catagory
        fields = ('Name',)

class SubcatagoryForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True, max_length=100)

    class Meta:
        model = subcatagory
        fields = ('Name',)


class Expensesform(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":40,'class':'form-control','placeholder':'Enter Detail here...'}),required=True)
    expenses_value = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Amount here...'}),required=True)

    class Meta:
        model  = Expenses
        fields = ("description", "expenses_value")

class Incomeform(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":40,'class':'form-control','placeholder':'Enter Detail here...'}),required=True)
    income_value = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Amount here...'}),required=True)

    class Meta:
        model  = Income
        fields = ("description", "income_value")

class ContactForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name here'}),required=True, max_length=100)
    Mobile = forms.CharField(widget=forms.TextInput(attrs={'intial ': '0' ,'class':'form-control','placeholder':'Enter Mobile here...'}),required=True)
    Address = forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":40,'class':'form-control','placeholder':'Enter Address here...'}),required=True)
    class Meta:
        model = Contacts
        fields = ["Name","Mobile","Address"]

    def clean_Mobile(self):
        n = self.cleaned_data.get('Mobile')
        allowed_characters = '0123456789'
        for char in n:
            if char not in allowed_characters:
                raise forms.ValidationError("Please only use digits, spaces, dots, slash and dash characters")
        return n

class listform(forms.ModelForm):
    class Meta:
        model = list
        fields = ("item","completed")
