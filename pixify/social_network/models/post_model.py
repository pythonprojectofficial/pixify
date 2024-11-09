from django.db import models
from constants import PostType, AccessLevel, PostContentType, SpecificUserTreatment
from django.contrib.postgres.fields import ArrayField


class Post(models.Model):
    posted_by = models.ForeignKey('users', on_delete=models.CASECADE, blank=True, related_name='fk_post_posts_users_id')
    type = models.IntegerField(
        choices=[(type.value, type.name) for type in PostType],
        blank=False
    )
    content_type = models.IntegerField(
        choices=[(type.value, type.name) for type in PostContentType],
        blank=False
    )
    media_url = models.URLField(max_length=200) 
    title = models.CharField(max_length=50)
    description = models.TextField
    
    accessability = models.IntegerField(
        choices=[(level.value, level.name) for level in AccessLevel],
        blank=False
    )
    specific_users = ArrayField(models.IntegerField(blank=True))
    treat_as = models.IntegerField(
        choices=[(type.value, type.name) for type in SpecificUserTreatment],
        blank=False
    )

    is_active = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('users', on_delete=models.CASECADE, blank=True, related_name='fk_create_users_users_id')
    updated_by = models.ForeignKey('users', on_delete=models.CASECADE, blank=True, related_name='fk_update_users_users_id')
    
    class Meta:
        db_table = 'posts'

    def __str__(self):
        return f"ID: {self.id}, Created at: {self.created_at}, Active: {self.is_active}"