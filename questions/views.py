from django.shortcuts import render, redirect
from questions import models, utils
from .forms import AskForm
from django.conf import settings
import os.path

def index(request):
    questions = models.Question.objects.published().order_by('datetime_published')
    return render(request, 'questions/index.html', {
        'questions': questions
    })


def new_question(request):
    return render(request, 'questions/new_question.html')


def ask(request):
    print(request.POST)

    if request.method == 'POST':
        form = AskForm(request.POST, request.FILES)

        if form.is_valid():
            question = form.save()
            print(request.POST, request.FILES)
            upload_image_for_question(request.FILES['photo'])
            # question.author = request.user
            # url = question.get_url()
            return success(request)
    else:
        form = AskForm()
    return render(request, 'questions/new_question.html', {'form': form})

def upload_image_for_question(f):
    with open(os.path.join(settings.MEDIA_ROOT, f'media/trial.jpg'), 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def success(request):
    return render(request, 'questions/success.html')
