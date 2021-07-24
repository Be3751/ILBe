from django import forms
from listitems.models import Item, Owner

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['founder', 'name', 'left_or_unknown', 'photo', 'comment']
        labels={
           'founder':'発見者名',
           'name':'物品名',
           'left_or_unknown':'廃棄可否',
           'photo':'写真',
           'comment':'コメント',
           }
        
        widgets = {
            'comment': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }

class RequestForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'number', 'comment']
        labels={
           'name':'持ち主名',
           'number':'学籍番号',
           'comment':'コメント',
           }
        
        widgets = {
            'comment': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }