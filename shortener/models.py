from django.db import models


# Create your models here.

from django.utils.crypto import get_random_string

def generate_code():
    while True:
        str = get_random_string(4)
        if not Url.objects.filter(short_code=str).exists():
            return str
class Url(models.Model):
    short_code = models.CharField( max_length=255, blank=True, unique=True,)
    long_url = models.CharField(max_length=500)
    visits_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    is_expired= models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     if kwargs["do_not"]:
    #         pass
    #     if not self.short_code:
    #         self.short_code = generate_code()
    #     super(Url, self).save(*args, **kwargs)

    class Meta:
        ordering =['-created_at']
    def __str__(self):
        return f"url {self.short_code}"
