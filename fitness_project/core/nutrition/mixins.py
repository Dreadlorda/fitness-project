from django.db import models
from django.utils.text import slugify

class SlugMixin(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(SlugMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True