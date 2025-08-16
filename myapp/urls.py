from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('ministries/', views.ministries, name='ministries'),
    path('impactstories/', views.impactstories, name='impactstories'),
    path('journey/', views.journey, name='journey'),
    path('contact/', views.contact, name='contact'),
    path('save-enquiry/', views.saveEnquiry, name='saveEnquiry'),
    path('blog/', views.blog, name='blog'),
    path('article/', views.article, name='article'),
    path('womenministryblog/', views.womenministryblog, name='womenministryblog'),
    path('churchleadershipblog/', views.churchleadershipblog, name='churchleadershipblog'),
    path('familyministryblog/', views.familyministryblog, name='familyministryblog'),
    path('communityministryblog/', views.communityministryblog, name='communityministryblog'),
]
