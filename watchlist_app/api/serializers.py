from wsgiref.validate import validator
from rest_framework import serializers
from tables import Description
from watchlist_app.models import Movie

'''Using Model Serializers'''

class MovieSerializer(serializers.ModelSerializer):
    """fields = "__all__ is for all the fields in our Movie 
        (ie., id, name, description, active) to be included and mapped. We can also include some and exclude some if we want."""
        
    class Meta:
        model = Movie
        fields = "__all__"
        
    def validate(self, data):
        if (data['name']).lower() == (data['description']).lower():
            raise serializers.ValidationError("Name and Descrption should be diferent")
        else:
            return data        
        
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short')
        return value
        
        
        
    


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
