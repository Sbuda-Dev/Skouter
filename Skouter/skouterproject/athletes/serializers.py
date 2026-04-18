from rest_framework import serializers
from .models import Athlete, AthleteMedia
from datetime import date

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ['id', 
                  'name',
                  'surname',
                  'date_of_birth',
                  'nationality',
                  'location',
                  'height',
                  'weight',
                  'position',
                  'school_team',
                  'club',
                  'bio', 
                  'sport', 
                  'location', 
                  'media',
                  'created_at']

    def get_age(self, obj):
        today = date.today()
        age = today.year - obj.date_of_birth.year - ((today.month, today.day) < (obj.date_of_birth.month, obj.date_of_birth.day))
        return age

class AthleteMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteMedia
        fields = ['id', 'file', 'media_type', 'uploaded_at']

        read_only_fields = ['uploaded_at']

class AthleteMediaUploaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteMedia
        fields = ['id', 'file', 'media_type', 'athlete']

        def validate_file(self, file):

            allowed_image = ['jpeg', 'png', 'jpg']
            allowed_video = ['mp4', 'avi', 'mov']

            ext = file.name.split('.')[-1].lower()

            if ext not in allowed_image + allowed_video:
                raise serializers.ValidationError("Unsupported file type.")
            
            return file

        def validate(self, data):

            file = data.get('file')
            media_type = data.get('media_type')

            ext = file.name.split('.')[-1].lower()

            if media_type == 'photo' and ext not in ['jpeg', 'png', 'jpg']:
                raise serializers.ValidationError("File type does not match media type.")
            
            if media_type == 'video' and ext not in ['mp4', 'avi', 'mov']:
                raise serializers.ValidationError("File type does not match media type.")
            
            return data