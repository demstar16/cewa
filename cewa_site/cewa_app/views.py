from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail

from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, "home.html")

def products(request):
    return render(request, "products.html")

def services(request):
    return render(request, "services.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            message = form.cleaned_data['content']
            
            send_mail(name, "From: " + email + "\n\nMessage: \n" +  message, email, ['cleaningequipmentwa@gmail.com'])
            
            return redirect('contact')
    else:
        form = ContactForm()
        
    return render(request, "contact.html", {
        'form': form
    })

def vacuums(request):
    return render(request, "machine-categories/vacuums.html")

def scrubbers(request):
    return render(request, "machine-categories/scrubbers.html")

def sweepers(request):
    return render(request, "machine-categories/sweepers.html")

def polishers(request):
    return render(request, "machine-categories/polishers.html")

def carpet_accessories(request):
    return render(request, "machine-categories/carpet-accessories.html")

def foggers(request):
    return render(request, "machine-categories/foggers.html")

def w36(request):
    return render(request, "machines/w36.html")

def w86(request):
    return render(request, "machines/w86.html")

def v20(request):
    return render(request, "machines/v20.html")

def i15b(request):
    return render(request, "machines/i15b.html")

def i35b(request):
    return render(request, "machines/i35b.html")

def i50b(request):
    return render(request, "machines/i50b.html")

def i50bt(request):
    return render(request, "machines/i50bt.html")

def i70bt(request):
    return render(request, "machines/i70bt.html")

def gm50b(request):
    return render(request, "machines/gm50b.html")

def gm56bt(request):
    return render(request, "machines/gm56bt.html")

def gm70bt(request):
    return render(request, "machines/gm70bt.html")

def gm65rbt(request):
    return render(request, "machines/gm65rbt.html")

def gm110(request):
    return render(request, "machines/gm110.html")

def i130(request):
    return render(request, "machines/i130.html")

def gm130(request):
    return render(request, "machines/gm130.html")

def gm160(request):
    return render(request, "machines/gm160.html")

def gm230(request):
    return render(request, "machines/gm230.html")

def s1500d(request):
    return render(request, "machines/s1500d.html")

def s1900d(request):
    return render(request, "machines/s1900d.html")

def isweep(request):
    return render(request, "machines/isweep.html")

def fc1517(request):
    return render(request, "machines/fc1517.html")

def fc2517(request):
    return render(request, "machines/fc2517.html")

def c1(request):
    return render(request, "machines/c1.html")

def c2(request):
    return render(request, "machines/c2.html")

def b3(request):
    return render(request, "machines/b3.html")

def x5(request):
    return render(request, "machines/x5.html")

