from rest_framework import serializers
from .models import Topic


class TopicSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    time_created = serializers.DateTimeField()

    class Meta:
        model = Topic
        fields = ["title", "description", "time_created"]
