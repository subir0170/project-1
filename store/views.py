from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'store/index.html')

def about_us(request):
    return render(request, 'store/aboutUs.html')

def cart(request):
    return render(request, 'store/cart.html')

def checkOut(request):
    return render(request, 'store/checkout.html')

def compare(request):
    return render(request, 'store/compare.html')

def contactUs(request):
    return render(request, 'store/contact-us.html')

def faq(request):
    return render(request, 'store/faq.html')

def login(request):
    return render(request, 'store/login.html')

def privacyPolicy(request):
    return render(request, 'store/privacy-policy.html')

def register(request):
    return render(request, 'store/register.html')

def termsCondition(request):
    return render(request, 'store/terms-condition.html')

def thisParams(request):
    return render(request, 'store/this.params.html')

def trackOrder(request):
    return render(request, 'store/track-order.html')

def wishList(request):
    return render(request, 'store/wishlist.html')