from django.db import models

class Flavor(models.Model):
    typeof_flavor = models.CharField(max_length=64)
    description = models.TextField(max_length=512, default='')

    def __str__(self):
        return f"{self.typeof_flavor} ({self.description})"

class Crust(models.Model):
    typeof_crust = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.typeof_crust}"

class Size(models.Model):
    typeof_size = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.typeof_size}"

class Extra(models.Model):
    typeof_extra = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.typeof_extra}"

class Pizza(models.Model):

    pizza_flavor = models.ForeignKey(
        Flavor, on_delete=models.CASCADE, related_name="pizzas_flavor")
    pizza_crust = models.ForeignKey(
        Crust, on_delete=models.CASCADE, related_name="pizzas_crust")
    pizza_size = models.ForeignKey(
        Size, on_delete=models.CASCADE, related_name="pizzas_size")
    pizza_extra = models.ManyToManyField(Extra, blank=True)

    username = models.CharField(max_length=64, default='')
    price= models.DecimalField(max_digits=4, decimal_places=2, default=0)
    progress = models.CharField(max_length=256, choices=[('Buon Appetito!','Buon Appetito!'), ('In delivery','In delivery'), 
        ('We are preparing your order','We are preparing your order'), ('We are cooking your pizza','We are cooking your pizza'),
        ('We have received your order','We have received your order')],default='')

    def __str__(self):
        return "{} --- {} --- {} --- {} --- {}".format(self.pizza_size, self.pizza_crust, self.pizza_flavor,list(self.pizza_extra.all()), self.progress)