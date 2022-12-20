from django.contrib import admin
from app.models import Customer,Product,Cart,OrderPlace,Profile
class CustomerAdmin(admin.ModelAdmin):
    model=Customer
    list_display=['id','user','name','locality','city','zipcode','state']

admin.site.register(Customer,CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    model=Product
    list_display=['title','selling_price','discount_price','discription','brand','categary','product_image']

admin.site.register(Product,ProductAdmin)


class CartAdmin(admin.ModelAdmin):
    model=Cart
    list_display=['user','product','quantity']

admin.site.register(Cart,CartAdmin)


class OrderPlaceAdmin(admin.ModelAdmin):
    model=OrderPlace
    list_display=['user','customer','product','quantity','ordered_date','status']

admin.site.register(OrderPlace,OrderPlaceAdmin)

class ProfileAdmin(admin.ModelAdmin):
    model=Profile
    list_display=['user','mobile','otp']
admin.site.register(Profile,ProfileAdmin)