from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ProductView.as_view(),name='home'),
    path('product-detail/<int:id>', views.ProductDetailView.as_view(), name='product-detail'),

    path('add-to-cart/', views.AddToCartView.as_view(), name='add-to-cart'),
    path('cart/', views.ShowCartView.as_view(), name='cart'),
    path('pluscart/', views.PlusCartView.as_view(),name="pluscart"),
    path('minuscart/', views.MinusCartView.as_view(),name="minuscart"),
    path('removecart/', views.RemoveCartView.as_view(),name="removecart"),

    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('paymentdone/', views.PaymentDoneView.as_view(), name='paymentdone'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.AddressView.as_view(), name='address'),
    path('orders/', views.OrdersView.as_view(), name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/',views.MobileView.as_view(), name='mobile'),
    path('mobile/<slug:data>/', views.MobileView.as_view(), name='mobiledata'),
    path('laptop/', views.LaptopView.as_view(), name='laptop'),
    path('laptop/<slug:data>/', views.LaptopView.as_view(), name='laptopdata'),

    path('bottom/', views.BottomView.as_view(), name='bottom'),
    path('bottom/<slug:data>/', views.BottomView.as_view(), name='bottomdata'),
    path('topwear/', views.TopwearView.as_view(), name='topwear'),
    path('topwear/<slug:data>/', views.TopwearView.as_view(), name='topweardata'),
    path('login/', views.login_attempt, name='login'),
    path("logout", views.logout_request, name='logout'),
    path('register/' ,views.register , name="register"),
    path('otp/' , views.otp , name="otp"),
    path('login-otp/', views.login_otp , name="login_otp"),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    # path('faltu/', views.faltu_function, name='faltu_function'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
