from django.db import models
import datetime


class Category (models.Model):
    title = models.CharField('Название категории', max_length = 100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self): 
        return self.title

class Section (models.Model):
    title = models.CharField('Название раздела', max_length = 100)
    section_category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=1)

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self): 
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    text = models.TextField()
    data = models.DateField(auto_now=True)
    img = models.ImageField('Изображение', blank=True, upload_to='blog/')
    categories = (
        ('R', 'Важно'),
        ('O', 'Срочно'),
    )
    categories_type = models.CharField('Метки', choices=categories, max_length=1, blank=True)
    category_post = models.ManyToManyField(Category)
    section_post = models.ManyToManyField(Section)

    def statusPost(self):
        if (datetime.date.today()-self.data).days<=1:
            return True
        else:
            return False   

    def __str__(self): 
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    author = models.TextField('Автор', blank=False)
    textComment = models.TextField('Текст комментария', blank=False)
    
    def __str__(self):
        return f'Комментарий от {self.author} для {self.post}'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
