from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dane/', views.dane),
    url(r'^loggedin/', views.add_user_to_database),
    url(r'^add/', views.fill_form)
]