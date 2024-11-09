from django.db import models
from django.contrib.postgres.fields import ArrayField

class Message(models.Model):

    text=models.CharField(max_length=200)
    media_url= models.CharField(max_length=200)
    sender_id = models.ForeignKey('users', on_delete=models.CASCADE,blank=False, related_name='fk_sender_messages_users_id')
    chat_id= models.ForeignKey('chats', on_delete=models.CASCADE,blank=False, related_name='fk_chat_messages_chats_id')
    reply_for_user_ids= ArrayField(models.ForeignKey('users', on_delete=models.CASCADE,blank=True,related_name='fk_reply_messages_users_id'))
    reply_for_message_id=models.ForeignKey('messages', on_delete=models.CASCADE,blank=True,related_name='fk_reply_messages_messages_id')
    send_at=models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default= True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('users', on_delete=models.CASCADE, blank=True, related_name='fk_create_messages_users_id')
    updated_by = models.ForeignKey('users', on_delete=models.CASCADE, blank=True, related_name='fk_update_messages_users_id')
    
    class Meta:
        db_table = 'messages'

    def __str__(self):
        return f"ID: {self.id}, Created at: {self.created_at}, Active: {self.is_active}"