from django.shortcuts import render, redirect
from questions import models
from .forms import AskForm
from django.conf import settings
import os.path
from django.http import Http404

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
            # print(request.POST, request.FILES)
            upload_image_for_question(request.FILES['photo'])
            # question.author = request.user
            # url = question.get_url()
            return success(request)
    else:
        form = AskForm()
    return render(request, 'questions/ask.html', {'form': form})

def upload_image_for_question(f):
    with open(os.path.join(settings.MEDIA_ROOT, f'media/trial.jpg'), 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def success(request):
    return render(request, 'questions/success.html')

def question(request, id):
    try:
        question = models.Question.objects.get(pk=id)
        return render(request, 'questions/question.html', { 'question': question })
    except models.Question.DoesNotExist:
        raise Http404(f'No such id question: {id}')

def login(request):
    return render(request, 'questions/login.html')

def paginate(objects_list, request):
    paginator = Paginator(objects_list, 3) 

    page = request.GET.get('page')
    objects = paginator.get_page(page)
    return objects_page, paginator
