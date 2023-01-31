from rest_framework import serializers 
from myapi.models import Mypost, Like
 
 
class MypostSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Mypost
        fields = (
                  'Pusername',
                    'id',
                  'title',
                  'description',
                  'like',
                  'TotalLike'
                  )

# class LikeSerializer(serializers.ModelSerializer):
 
#     class Meta:
#         model = Mypost
#         fields = ('like_id',
#                   'Lusername',
#                   'date',
#                   'time',
#                   'count')