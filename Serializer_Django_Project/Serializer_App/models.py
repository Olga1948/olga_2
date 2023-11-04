from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Rating(models.Model):
    STAR_CHOICES = (
        (1, '★'),
        (2, '★★'),
        (3, '★★★')
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rating = models.CharField(max_length=3, choices=STAR_CHOICES)

    def __str__(self):
        return f'{self.product.name} - {self.rating}'


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий к товару {self.product.name} ({self.created_at})'
