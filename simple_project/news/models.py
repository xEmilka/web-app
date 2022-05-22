from django.db import models
from django.urls import reverse

# Create your models here.
class Articles(models.Model):
    title =  models.CharField('Название', max_length= 250,)
    slug = models.SlugField('URL',max_length=250, unique= True, db_index=True,)
    anons = models.CharField('Анонс', max_length=250, )
    full_text = models.TextField('Статья',)
    date = models.DateTimeField('Дата публикации')
    cat = models.ForeignKey('Category',on_delete=models.PROTECT, null = True) #Класс в строке тк класс определен после класса Articles
    photo = models.ImageField(default='пусто',upload_to="photos/%y%m/%d",)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name ='Новость'
        verbose_name_plural = 'Новости'
        ordering = ['date','title']

class Category(models.Model):
        name = models.CharField("Жанр", max_length=100, db_index=True)
        slug = models.SlugField('URL', max_length=250, unique=True, db_index=True, )

        def __str__(self):
            return self.name


        def get_absolute_url(self):
            return reverse('category_show', kwargs={'cat_slug':self.slug})

