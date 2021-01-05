from django.conf.urls import url

from .views import (
search_collision,
user
)



urlpatterns = [
    url(r"^(?P<token>[\w|\d]+?)/collision$", search_collision),
    url(r"^(?P<token>[\w|\d]+?)/users$", user)

]
