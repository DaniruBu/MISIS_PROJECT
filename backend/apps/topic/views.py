from rest_framework import generics
from .serializers import TopicSerializer
from .models import Topic

class TopicListAPIView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
