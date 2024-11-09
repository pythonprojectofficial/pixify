from django.db import models

class Message_Reaction(models.Model):
    reacted_by=models.ForeignKey('users', on_delete=models.CASCADE,blank=False, related_name='fk_reacted_messagereactions_users_id')
    message_id=models.ForeignKey('messages', on_delete=models.CASCADE,blank=False, related_name='fk_reacted_messagereactions_messages_id')
    reaction_type=models.CharField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default= True)
    created_by=models.ForeignKey('users', on_delete=models.CASCADE,blank=False, related_name='fk_created_messagereactions_users_id')
    updated_by = models.ForeignKey('users', on_delete=models.CASCADE, blank=True, related_name='fk_updated_messagereactions_users_id')
    
    class Meta:
        db_table = 'messagereactions'

    def __str__(self):
        return f"ID: {self.id}, Created at: {self.created_at}, Active: {self.is_active}"
