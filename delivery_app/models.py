from django.db import models

# Create your models here.
class DeliverySlot(models.Model):
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    delivery_address = models.TextField()
    delivery_time_slot = models.CharField(
        max_length=50,
        choices=[
            ('Morning', 'Morning (8 AM - 12 PM)'),
            ('Afternoon', 'Afternoon (12 PM - 4 PM)'),
            ('Evening', 'Evening (4 PM - 8 PM)'),
        ],
        default='Morning'
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('In Transit', 'In Transit'),
            ('Delivered', 'Delivered'),
            ('Cancelled', 'Cancelled'),
        ],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.sender_name} to {self.receiver_name} - {self.delivery_time_slot}"
