from django.urls import path
from .views import TopicListAPIView

urlpatterns = [
    path("", TopicListAPIView.as_view(), name='topic'),
]
