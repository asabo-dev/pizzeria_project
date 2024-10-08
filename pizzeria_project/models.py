from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A pizza the user can make."""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Topping(models.Model):
    """Toppings for the pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name