from rest_framework import serializers
from .models import Notice, Subscribers

class NoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice 
        fields = ('title', 'detail', 'published_on', 'fb_link', 'attachment', 'category')

class SubscribersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribers
        fields = ('phone',)