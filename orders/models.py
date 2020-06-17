from django.db import models

class Flavor(models.Model):
    typeof_flavor = models.CharField(max_length=64)
    decriptionof_flavor = models.TextField(max_length=512, default='')

    def __str__(self):
        return f"{self.typeof_flavor}: {self.decriptionof_flavor}"

class Crust(models.Model):
    typeof_crust = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.typeof_crust}"

class Size(models.Model):
    typeof_size = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.typeof_size}"

class Pizza(models.Model):

    pizza_flavor = models.ForeignKey(
        Flavor, on_delete=models.CASCADE, related_name="pizzas_flavor")
    pizza_crust = models.ForeignKey(
        Crust, on_delete=models.CASCADE, related_name="pizzas_crust")
    pizza_size = models.ForeignKey(
        Size, on_delete=models.CASCADE, related_name="pizzas_size")
    quantity = models.IntegerField()
    price= models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Pizza: {self.pizza_flavor}, {self.pizza_crust}, {self.pizza_size}, {self.price}"

class Extra(models.Model):
    typeof_extra = models.CharField(max_length=64, blank=True, default='')
    pizzas_extra = models.ManyToManyField(
        Pizza, blank=True, related_name="pizzas_extra")

    def __str__(self):
        return f"{self.typeof_extra}"
