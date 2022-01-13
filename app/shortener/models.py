import uuid
from django.db import models


class ShortenLink(models.Model):
    key = models.CharField(
        max_length=5,
        primary_key=True,
        editable=False
    )
    link = models.URLField(
        max_length=1000
    )

    def __str__(self):
        return self.key

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls) -> str:
        key = uuid.uuid4().hex[:5]
        count = 0
        while cls.objects.filter(key=key).exists() or count > 5:
            key = uuid.uuid4().hex[:5]
            count += 1
        return key

    @property
    def shorten_link(self):
        return f"http://localhost:8000/{self.key}"
