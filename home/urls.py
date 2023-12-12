from django.urls import path, re_path
from home.views import *

urlpatterns = [
    path("", index),
    path("cats/<slug:cat_slug>/", cat),
    
]

#re_path(r"^archive/(?P<year>[0-9]{4})", archive)