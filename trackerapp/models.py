from django.db import models
class Tracker(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('shopping', 'Shopping'),
        ('rent', 'Rent'),
        ('other', 'Other'),
    ]
    
    amount = models.IntegerField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)  # Use choices
    description = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    receipts = models.ImageField(upload_to='receipts/', blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"
