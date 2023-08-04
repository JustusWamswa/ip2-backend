from django.urls import path
# from .views import ContactView, BlogView
from . import views

urlpatterns = [
    # path("contact/", ContactView.as_view()),
    # path("blog/create/", BlogView.as_view()),
    path("contact/", views.get_contacts, name="contacts"),
    path("blog/", views.get_blogs, name="blogs"),
    path("blog/<int:id>/", views.get_blog, name="blog"),
    path("contact/add/", views.add_contacts, name="add_contacts"),
]