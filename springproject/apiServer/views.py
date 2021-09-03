from rest_framework import views, response, permissions, status

from .models import SampleData
from .serializers import SampleDataSerializer

# Create your views here.
# REST API 로 구성해보자.
class SampleDataView(views.APIView):
  def get(self, request, **kwargs):
    datum_id = kwargs.get('datum_id')
    serializer = SampleDataSerializer
    if datum_id is None:
      serializer = SampleDataSerializer(SampleData.objects.all(), many=True)
      
    else:
      serializer = serializer(SampleData.objects.get(id=datum_id))

    return response.Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request):
    serializer = SampleDataSerializer(data=request.data)

    if(serializer.is_valid()):
      serializer.save() # serializer 에서 저장을 그냥 때려버리는구나
      return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self, request, **kwargs):
    datum_id = kwargs.get('datum_id')

    if datum_id is None:
      return response.Response("invalid requests", status=status.HTTP_400_BAD_REQUEST)
    else:
      # 정말 직관적이지 않은 update 방식인데...?
      # Serialzer 란 hibernate 의 entity manager 이자 object mapper 이냐?
      serializer = SampleDataSerializer(SampleData.objects.get(id=datum_id), data=request.data)
      if serializer.is_valid():
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK)
      else:
        return response.Response("invalid requests", status=status.HTTP_400_BAD_REQUEST)
  def delete(self, request, **kwargs):
    datum_id = kwargs.get('datum_id')

    if datum_id is None:
      return response.Response("invalid requests", status=status.HTTP_400_BAD_REQUEST)
    else:
      SampleData.objects.get(id=datum_id).delete()
      return response.Response("invalid requests", status=status.HTTP_200_OK)