from django.db import models

# Create your models here.


class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    # The __str__ method pretty prints the obj.
    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.title
