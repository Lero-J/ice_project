from django.contrib import admin

from icecream.models import IceCream, Child, IceCreamStore, Father, Mother

# Register your models here.
admin.site.register(IceCream)
admin.site.register(Child)
admin.site.register(IceCreamStore)
admin.site.register(Father)
admin.site.register(Mother)