from django.shortcuts import render, redirect
from questions import models, utils
from .forms import QuestionForm

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
        form = QuestionForm(request.POST, request.FILES)

        if form.is_valid():
            question = form.save()
            # question.author = request.user
            question.save()
            return success(request)
    else:
        form = QuestionForm()
    return render(request, 'questions/new_question.html', {'form': form})


def success(request):
    return render(request, 'questions/success.html')