from rest_framework import serializers
from .models import SampleData
 
class SampleDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = SampleData
    fields = '__all__' # field = ['name', 'title'] 등으로 작업가능.
    # 모델 User의 모든 field를 serializer함.
 