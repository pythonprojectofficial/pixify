from django.db import models
from constants import ChatType
from django.contrib.postgres.fields import ArrayField



class Chat(models.Model):
    title = models.CharField(null = True, blank = True)
    member_id =ArrayField( models.ForeignKey('users', on_delete=models.CASCADE, blank=False, related_name='fk_member_chats_users_id'))
    type = models.IntegerField(
        choices=[(type.value, type.name) for type in ChatType],
        blank=False
    )
    is_active = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('users', on_delete=models.CASCADE, blank=True, related_name='fk_create_chats_users_id')
    updated_by = models.ForeignKey('users', on_delete=models.CASCADE, blank=True, related_name='fk_update_chats_users_id')
    
    class Meta:
        db_table = 'chats'

    def __str__(self):
        return f"ID: {self.id}, Created at: {self.created_at}, Active: {self.is_active}"
    




    