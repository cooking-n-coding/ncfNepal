from django.shortcuts import render, redirect
from myapp.models import contactEnquiry

def index(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def ministries(request):
    return render(request, "ministries.html")

def impactstories(request):
    return render(request, "impactstories.html")

def journey(request):
    return render(request, "journey.html")

def contact(request):
    age_range = range(18, 61)
    return render(request, 'contact.html', {'age_range': age_range})

def blog(request):
    return render(request, "blog.html")
def article(request):
    return render(request, "article.html")

def womenministryblog(request):
    return render(request, "womenministryblog.html")

def churchleadershipblog(request):
    return render(request, "churchleadershipblog.html")

def familyministryblog(request):
    return render(request, "familyministryblog.html")

def communityministryblog(request):
    return render(request, "communityministryblog.html")

def saveEnquiry(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        occupation = request.POST.get('occupationInput')
        message = request.POST.get('message')

        en = contactEnquiry(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone=phone,
            age=age,
            occupation=occupation,
            message=message
        )
        en.save()
        return render(request, 'contact.html', {'age_range': range(18, 61), 'success': True})

    return render(request, 'contact.html', {'age_range': range(18, 61)})
