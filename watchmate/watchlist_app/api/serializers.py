from rest_framework import serializers
from ..models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"
        
    

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        
    
   
            
        


# Using serializers.Serializer
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
  
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Name and Description must be different!")
#         return data
      
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     if len(value) > 30:
    #         raise serializers.ValidationError("Name is too long!")
    #     else:
    #         return value

    
    
    
    # WatchListSerializer's MethodField
    # name_length = serializers.SerializerMethodField()
    
    # WatchListSerializer's validators
    # def validate(self, data):
    #     if data["title"] == data["storyline"]:
    #         raise serializers.ValidationError("Title and Storyline must be different!")
    #     return data
      
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     if len(value) > 30:
    #         raise serializers.ValidationError("Name is too long!")
    #     else:
    #         return value
    
    # def get_name_length(self, obj):
    #     return len(obj.title)
    
    
    # StreamPlatformSerializer's validators
    # def validate(self, data):
    #     if data["name"] == data["about"]:
    #         raise serializers.ValidationError("Name and About info must be different!")
        
    #     if len(data["about"]) < 5:
    #         raise serializers.ValidationError("About info is too short!")
        
    #     return data
    
    # def name_length(value):
    #     if len(value) < 2:
    #             raise serializers.ValidationError("Name is too short!")
    #     if len(value) > 30:
    #         raise serializers.ValidationError("Name is too long!")