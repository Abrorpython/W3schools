from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,ListView
from django.views.generic.edit import UpdateView
from .models import Coursers,Section,Subject,ThemeAbout


def index(request):
    return render(request, 'index.html')

class CoursersCreateView(CreateView):
    model = Coursers
    template_name = 'courserscreate.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


class SectionCreatView(CreateView):
    model = Section
    template_name = 'sectioncreate.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


def cours(request):
    curs = Coursers.objects.all()

    ctx = {
        "curs":curs
    }

    return render(request,'list.html',ctx)


def section(request,pk):
    section = Section.objects.all().filter(course_id=pk)

    ctx = {
        'section':section
    }
    return render(request,'section.html',ctx)

def subjects(request,n):
    subjects = Subject.objects.get()

    ctx = {
        'subjects':subjects
    }

    return render(request,'subjects.html',ctx)