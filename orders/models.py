from django.db import models

class Flavors(models.Model):
    typeof_flavor = models.CharField(max_length=64)
    decriptionof_flavor = models.TextField(max_length=512, default='')

    def __str__(self):
        return f"{self.typeof_flavor}: {self.decriptionof_flavor}"

class Crusts(models.Model):
    typeof_crust = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.typeof_crust}"

class Sizes(models.Model):
    typeof_size = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.typeof_size}"

class Pizzas(models.Model):
    pizza_flavor = models.ForeignKey(
        Flavors, on_delete=models.CASCADE, related_name="pizzas_flavor")
    pizza_crust = models.ForeignKey(
        Crusts, on_delete=models.CASCADE, related_name="pizzas_crust")
    pizza_size = models.ForeignKey(
        Sizes, on_delete=models.CASCADE, related_name="pizzas_size")
    quantity = models.IntegerField()

    def __str__(self):
        return f"Pizza: {self.pizza_flavor}, {self.pizza_crust}, {self.pizza_size}"

class Extras(models.Model):
    typeof_extra = models.CharField(max_length=64, blank=True, default='')
    pizzas_extra = models.ManyToManyField(
        Pizzas, blank=True, related_name="pizzas_extra")

    def __str__(self):
        return f"{self.typeof_extra}"
