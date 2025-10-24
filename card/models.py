from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория меню"
        verbose_name_plural = "Категории меню"

class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class Location(models.Model):
    address = models.TextField(verbose_name="Адрес")
    map_link = models.URLField(verbose_name="Ссылка на карту")
    phone = models.CharField(max_length=20, verbose_name="Телефон", default="+7 XXX XXX-XX-XX")
    working_hours = models.CharField(max_length=100, verbose_name="Часы работы", default="18:00 - 02:00")
    
    def __str__(self):
        return self.address
    
    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

class Review(models.Model):
    author = models.CharField(max_length=100, verbose_name="Автор")
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="Рейтинг")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return f"{self.author} - {self.rating}/5"
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"