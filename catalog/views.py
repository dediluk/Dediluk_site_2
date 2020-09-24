from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# @login_required
def mainPage(request):
    return render(request, 'Dediluk/main_page.html')


def aboutMe(request):
    return render(request, 'Dediluk/about.html')
