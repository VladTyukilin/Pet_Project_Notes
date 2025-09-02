import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from notes_app.models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'time_create', 'time_update']
        read_only_fields = ['time_create', 'time_update']


# def encode():
#     model = NoteModel('Angelina Jolie', 'Content: Angelina Jolie')
#     model_sr = NoteSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json, type(json), sep='\n')
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = NoteSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)