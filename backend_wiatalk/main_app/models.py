from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=25)
    sipIdentifier = models.CharField(max_length=200)
    online = models.BooleanField()
    classe = models.CharField(max_length=255)
    photoUrl = models.ImageField(null = True)

    def __str__(self):
        return self.username


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class GroupChat(models.Model):
    title = models.CharField(max_length=50)
    users = models.ManyToManyField(User, related_name="users")

    def __str__(self):
        return self.title

class AbstractMessage(models.Model):
    timestamp = models.DateTimeField()
    messageText = models.TextField(null = True)
    video = models.FileField(null = True)
    photo = models.ImageField(null = True)
    audio = models.FileField(null = True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.messageText

class Message(AbstractMessage):
    received = models.BooleanField()
    seen = models.BooleanField()
    message_user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_user_1')
    message_user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_user_2')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

class GroupMessage(AbstractMessage):
    groupChat = models.ForeignKey(GroupChat, on_delete=models.CASCADE)
    users_rec = models.ManyToManyField(User, related_name="users_rec")
    users_seen = models.ManyToManyField(User, related_name="users_seen")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "A message of the group"

class Call(models.Model):
    duration = models.TimeField()
    timestamp = models.DateTimeField()
    videoCall = models.BooleanField()
    call_user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='call_user_1')
    call_user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='call_user_2')

class GroupCall(models.Model):
    duration = models.TimeField()
    timestamp = models.DateTimeField()
    videoCall = models.BooleanField()
    participants = models.ManyToManyField(User, related_name='participants')




