from rest_framework import serializers
from .models import User,Influencer, Advertiser, ChatRoom, Message, Rate

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'is_influencer', 'is_advertiser']

class InfluencerSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    class Meta:
        models = Influencer
        fields = ['user', 'description', 'bio', 'followers', 'following']
class AdvertiserSerializers(serializers.ModelSerializer):
    user = UserSerializers()

    class Meta:
        models = Advertiser
        fields = ['user', 'description', 'website', 'followers', 'following', 'website']

class RateSerializers(serializers.ModelSerializer):
    influencer = InfluencerSerializers()
    class Meta:
        models = Rate
        fields = ['influencer', 'rate', 'created_at', 'updated_at']

class ChatRoomSerializers(serializers.ModelSerializer):
    members = UserSerializers(many=True)
    class Meta:
        models = ChatRoom
        fields = ['name', 'members', 'created_at']    

class MessageSerializers(serializers.ModelSerializer):
    chat_room = ChatRoomSerializers()
    sender = UserSerializers()
    class Meta:
        models = Message
        fields = ['chat_room', 'sender', 'time_stamp', 'message', 'image', 'is_read', 'is_deleted']

    
  