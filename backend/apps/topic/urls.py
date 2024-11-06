from django.urls import path, include
from .views import TopicListAPIView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'topic', TopicListAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
