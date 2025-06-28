from django.db import models

class Pitch(models.Model):
    seller_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    pitch_text = models.TextField()
    ai_feedback = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.seller_name} - {self.product_name}"
