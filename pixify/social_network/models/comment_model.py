from django.db import models
from constants import PostType, AccessLevel, PostContentType, SpecificUserTreatment
from django.contrib.postgres.fields import ArrayField


class Comment(models.Model):
    comment_by = models.ForeignKey('users', on_delete=models.CASECADE, blank=True, related_name='fk_comment_comments_users_id')
    post_id = models.ForeignKey('posts', on_delete=models.CASECADE, blank=False, related_name='fk_post_comments_post_id')
    comment = models.CharField(max_length=100)
    reply_for = models.ForeignKey('self', on_delete=models.CASECADE, blank=True, related_name='fk_reply_comments_comment_id')

    is_active = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('users', on_delete=models.CASECADE, blank=True, related_name='fk_create_users_users_id')
    updated_by = models.ForeignKey('users', on_delete=models.CASECADE, blank=True, related_name='fk_update_users_users_id')
    
    class Meta:
        db_table = 'posts'

    def __str__(self):
        return f"ID: {self.id}, Created at: {self.created_at}, Active: {self.is_active}"