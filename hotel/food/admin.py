from django.contrib import admin

from food.models import Burger
from food.models import chef
from food.models import dish,dish1,dish2,contact,comment

admin.site.register(Burger)
admin.site.register(chef)
admin.site.register(dish)
admin.site.register(dish1)
admin.site.register(dish2)
admin.site.register(contact)
admin.site.register(comment)