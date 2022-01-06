from django.db import models
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete, m2m_changed
from django.dispatch import receiver


class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return f'{self.title}'


@receiver(post_save, sender=Post)
def notify_user(sender, instance, created, **kwargs):
    print('Post is created')


class Inventory(models.Model):
    item = models.CharField(max_length=20)
    item_quantity = models.IntegerField()

    def __str__(self):
        return f'{self.item}'


class Order(models.Model):
    order_item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    order_placed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


@receiver(pre_save, sender=Order)
def validate_quantity(sender, instance, **kwargs):
    if instance.order_item.item_quantity > instance.quantity and not instance.order_placed:
        instance.order_placed = True

        item = Inventory.objects.get(item=instance.order_item)
        item.item_quantity = instance.order_item.item_quantity - instance.quantity
        item.save()
        instance.save()
        print('Order is placed')
    else:
        print('Not enough items available')


@receiver(post_delete, sender=Order)
def reset_inventory(sender, instance, **kwargs):
    if instance.order_placed:
        item = Inventory.objects.get(item=instance.order_item)
        item.item_quantity = instance.order_item.item_quantity + instance.quantity
        item.save()
    print("The order is deleted")
