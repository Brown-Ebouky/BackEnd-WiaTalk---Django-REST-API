from django.contrib import admin
from .models import User
from .models import Message
from .models import GroupMessage
from .models import Chat
from .models import GroupChat
from .models import Call
from .models import GroupCall

# Register your models here.
admin.site.register(User)
admin.site.register(Message)
admin.site.register(GroupMessage)
admin.site.register(Chat)
admin.site.register(GroupChat)
admin.site.register(Call)
admin.site.register(GroupCall)
