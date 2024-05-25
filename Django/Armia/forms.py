from django import forms
from django.core.validators import MaxLengthValidator

from .models import *


class WeaponModelForm(forms.ModelForm):
    class Meta:
        model = WeaponModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        max_length_validator = MaxLengthValidator(limit_value=99)
        self.fields['name'].validators.append(max_length_validator)

class EnginiryTypeForm(forms.ModelForm):
    class Meta:
        model = EnginiryType
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        max_length_validator = MaxLengthValidator(limit_value=98)
        self.fields['name'].validators.append(max_length_validator)

class MilitaryBaseForm(forms.ModelForm):
    class Meta:
        model = MilitaryBase
        fields = ['id', 'base_type']

        widgets = {
            'id': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super(MilitaryBaseForm, self).__init__(*args, **kwargs)
        self.fields['id'].widget.attrs.update({'name': 'location'})
        self.fields['id'].label = 'Локация, ее нельзя изменить!'






class MilitaryBaseFormAdd(forms.ModelForm):
    class Meta:
        model = MilitaryBase
        fields = ['id', 'base_type']

        def __init__(self, *args, **kwargs):
            super(MilitaryBaseForm, self).__init__(*args, **kwargs)
            self.fields['id'].widget.attrs.update({'name': 'location'})





class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ammo_amount'].widget = forms.TextInput(attrs={'placeholder': 'Введите количество боеприпасов'})

    def clean_ammo_amount(self):
        ammo_amount = self.cleaned_data.get('ammo_amount')
        try:
            ammo_amount = int(ammo_amount)
            if ammo_amount <= 0:
                raise forms.ValidationError('Количество боеприпасов должно быть положительным числом.')
        except ValueError:
            raise forms.ValidationError('Введите корректное число для боеприпасов')
        return ammo_amount


class SoldierForm(forms.ModelForm):
    class Meta:
        model = Soldier
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['full_name'].widget = forms.TextInput(attrs={'placeholder': 'Введите полное имя'})

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        words = full_name.split()
        if len(words) not in [2, 3]:
             raise forms.ValidationError('Поле "Полное имя" должно содержать ровно 2 или 3 слова.')
        return full_name




class EnginiryForm(forms.ModelForm):
    class Meta:
        model = Enginiry
        fields = '__all__'



class BaseCodesForm(forms.ModelForm):
    class Meta:
        model = BaseCodes
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BaseCodesForm, self).__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['readonly'] = True
        self.fields['id'].label = 'Шифр базы, его изменить нельзя!'


class BaseCodesFormAdd(forms.ModelForm):
    class Meta:
        model = BaseCodes
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BaseCodesFormAdd, self).__init__(*args, **kwargs)
        self.fields['id'].label = 'Шифр базы'





class ArmyForm(forms.ModelForm):
    class Meta:
        model = Army
        fields = '__all__'