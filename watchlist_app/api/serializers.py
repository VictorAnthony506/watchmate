from wsgiref.validate import validator
from rest_framework import serializers
from tables import Description
from watchlist_app.models import StreamPlatform, WatchList


class WatchListSerializer(serializers.ModelSerializer):   
                    
    class Meta:
        model = WatchList
        fields = "__all__"
        
        
class StreamPlatformSerializer (serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True) # I have to use watchlist here, if i use like watch or any other name it won't show.
    # many=True, because we want wach list to be able to have one or more movies
    # One platform can have many movies (watchlist) but a movie can only have one platform
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        
    



       


'''Using Model Serializers'''

# class ModelSerializer(serializers.ModelSerializer):   
#     """fields = "__all__ is for all the fields in our Movie 
#         (ie., id, name, description, active) to be included and mapped. We can also include some and exclude some if we want.
#         For example if I do fields = ["id", "name", "description"], my active would be hidden.
#         Someone can use just exclude = ["id"] for instance to hide the id. """
        
        
#     class Meta:
#         model = Movie
#         fields = "__all__"
#         fields = ["id", "name", "description"]
#         exclude = ['id']
        
        
#     len_name = serializers.SerializerMethodField()
    
    
#     def get_len_name(self, object):
#         """The object can access each element of our fields ["id", "name", "description", "active].
        
#         get_['method'] in our case it is get_len_name"""
        
#         return len(object.name)
    
    
#     def validate(self, data):
#         if (data['name']).lower() == (data['description']).lower():
#             raise serializers.ValidationError("Name and Descrption should be diferent")
#         else:
#             return data        
        
        
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is too short')
#         return value
        
        
        
    


'''Using serializers.Serializers'''
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name is too short')
    
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    
#     def create(self, validated_data):
#         """
#         Create and return a new `Movie` instance, given the validated data.
#         """
#         return Movie.objects.create(**validated_data)
    
    
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Movie` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if (data['name']).lower() == (data['description']).lower():
#             raise serializers.ValidationError("Name and Descrption should be diferent")
#         else:
#             return data        
        
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short')
    #     return value
