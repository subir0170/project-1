from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('aboutUs',about_us,name="aboutUs"),
    path('cart',cart,name="cart"),
    path('checkout',checkOut,name="checkout"),
    path('compare',compare,name="compare"),
    path('contact-us',contactUs,name="contact-us"),
    path('faq',faq,name="faq"),
    path('login',login,name="login"),
    path('privacy-policy',privacyPolicy,name="privacy-policy"),
    path('register',register,name="register"),
    path('terms-condition',termsCondition,name="terms-condition"),
    path('this.params',thisParams,name="this.params"),
    path('track-order',trackOrder,name="track-order"),
    path('wishlist',wishList,name="wishlist")
]