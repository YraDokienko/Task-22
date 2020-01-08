from django.db import models


class Size(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Ingredient(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['name']


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)


class Pizza(models.Model):
    name = models.CharField('Название', max_length=40)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name='Размер')
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2, default=0)
    ingredient = models.ManyToManyField(Ingredient, verbose_name='Ингридиенты')
    description = models.CharField('Описание', max_length=300)
    image = models.ImageField(upload_to=image_folder)
    slug = models.SlugField()
    available = models.BooleanField('Наличие', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пиццу'
        verbose_name_plural = 'Пиццы'
        ordering = ['name']


class InstancePizza(models.Model):
    name = models.CharField('Название', max_length=40)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name='Размер')
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2, default=0)
    count = models.PositiveIntegerField('Количество', default=1)
    pizza_template = models.ForeignKey(Pizza, on_delete=models.CASCADE)


class Order(models.Model):
    pizzas = models.ManyToManyField(InstancePizza, blank=True)
    full_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def save_full_price(self):
        pizzas = self.pizzas.all()
        full_price = 0
        for pizza in pizzas:
            full_price += pizza.price * pizza.count
        self.full_price = full_price
        self.save()
