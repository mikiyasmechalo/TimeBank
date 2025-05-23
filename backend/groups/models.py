from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owned_groups', on_delete=models.CASCADE)
    members = models.ManyToManyField(
        User,
        related_name='custom_groups',
        through='GroupMembership',
        through_fields=('group', 'user')
    )
    
    
    
    image = models.ImageField(upload_to='group_images/', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 


    def __str__(self):
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['owner']), 
            models.Index(fields=['is_active']), 
        ]
        ordering = ['name'] 


class GroupMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True) 

    class Meta:
        unique_together = ('user', 'group')
        indexes = [
            models.Index(fields=['user', 'group']),
            models.Index(fields=['group', 'is_active']), 
        ]
        ordering = ['joined_at'] 

    def __str__(self):
        return f'{self.user.username} is a member of {self.group.name}'


class UserStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_stats') 
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='member_stats') 
    total_hours_given = models.FloatField(default=0)
    total_hours_received = models.FloatField(default=0)
    sessions_completed = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'group') 
        indexes = [
            models.Index(fields=['user', 'group']),
            models.Index(fields=['group']), 
        ]

    def __str__(self):
        return f'{self.user.username} - {self.group.name}'


class GroupAnnouncement(models.Model):
    group = models.ForeignKey('Group', related_name='announcements', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posted_announcements') 

    class Meta:
        ordering = ['-created_at'] 
        indexes = [
            models.Index(fields=['group', '-created_at']), 
        ]

    def __str__(self):
        return f"{self.title} in {self.group.name}"

