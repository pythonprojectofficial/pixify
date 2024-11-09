from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime
from constants import Gender, RelationShipStatus

class User(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.CharField(blank=True, null=True, max_length=100)
    hobbies = ArrayField(models.CharField(max_length=50,blank=True,null=True))
    bio = models.CharField(max_length=100)
    profile_photo_url = models.URLField(max_length=200)
    cover_photo_url = models.URLField(max_length=200)
    dob = models.DateField(blank=False,default=datetime.date(1950, 1, 1))
    gender = models.IntegerField(
        choices=[(gender.value, gender.name) for gender in Gender],
        blank=True
    )
    relationship_status = models.IntegerField(
        choices=[(status.value, status.name) for status in RelationShipStatus],
        blank=True
    )

    is_active = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('users', on_delete=models.CASECADE, blank=True, related_name='fk_create_users_users_id')
    updated_by = models.ForeignKey('users', on_delete=models.CASECADE, blank=True, related_name='fk_update_users_users_id')
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
         return f"ID: {self.id}, Created at: {self.created_at}, Active: {self.is_active}"