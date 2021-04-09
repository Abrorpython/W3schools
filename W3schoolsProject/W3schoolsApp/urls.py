from django.urls import path
from . import views
from .views import CoursersCreateView,SectionCreatView


urlpatterns = [
    path('',views.index,name='index'),
    path('curs/',views.cours,name = 'curs'),
    path('curs/<int:pk>/',views.section,name='section'),
    path('curs/<int:pk>/',views.subjects,name='subjects'),
    path('creatC/',CoursersCreateView.as_view(),name= 'courscreate'),
    path('creatS/',SectionCreatView.as_view(),name='sectioncreate')
]