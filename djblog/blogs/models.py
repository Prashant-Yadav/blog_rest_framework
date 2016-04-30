from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(TimeStampedModel):
    title = models.CharField(max_length=40, default=None)
    text = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='blogs')

    class Meta:
        ordering = ('-created',)


class Comment(TimeStampedModel):
    text = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='comments')
    blog = models.ForeignKey(Blog, related_name='comments')

    class Meta:
        ordering = ('-created',)
