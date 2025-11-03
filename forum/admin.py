#This imports Django’s admin module, which is the system that generates the admin panel.
# Without this, you can’t tell Django to show your models in the admin interface.
from django.contrib import admin

# from .models → the . means “look in this app folder” (here, forum)
# import Section, Post, Reply → brings in the models you defined so you can register them
from .models import Section, Post, Reply

# Register models so they show up in the admin panel
# This allows models to be edited in the admin GUI later
# It isn't necessary, but it can be very helpful
admin.site.register(Section)
admin.site.register(Post)
admin.site.register(Reply)
