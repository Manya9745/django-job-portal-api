# from django.urls import path
# from .views import JobListAPI, JobCreateAPI, UserTestAPI

# urlpatterns = [
#     path('jobs/', JobListAPI.as_view()),
#     path('jobs/create/', JobCreateAPI.as_view()),
#     path('test/', UserTestAPI.as_view()),
# ]

from django.urls import path
from .views import JobListCreateAPI

urlpatterns = [
    path('jobs/', JobListCreateAPI.as_view(), name='jobs'),
]