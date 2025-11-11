from django import forms
from .models import Eleicao, Chapa

class EleicaoForm(forms.ModelForm):
    class Meta:
        model = Eleicao
        fields = ["titulo", "descricao", "status", "data_termino"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título da eleição"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Descrição breve"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "data_termino": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
        }

class ChapaForm(forms.ModelForm):
    class Meta:
        model = Chapa
        fields = ["nome", "coordenador", "descricao", "eleicao"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome da chapa"}),
            "coordenador": forms.TextInput(attrs={"class": "form-control", "placeholder": "Coordenador"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Descrição breve"}),
            "eleicao": forms.Select(attrs={"class": "form-select"}),
        }