from django.core.exceptions import ValidationError

from .models import Articles
from django.forms import ModelForm,TextInput,DateTimeInput,Textarea,FileInput,Select

class ArticlesForm(ModelForm):
    def __int__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Articles
        fields = ['title','anons','full_text','date','photo','cat',]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонас статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            "photo": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Добавь фото'

            }),
            "cat": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Категория не выбрана'

            }),


        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 10:
            raise ValidationError('Длина превышает 200 символов')
        return title