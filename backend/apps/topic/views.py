
from .serializers import TopicSerializer
from rest_framework import views, viewsets, status
from .models import Topic

class TopicListAPIView(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
