from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from api.serializers import ApiSerializers
from api.models import ApiModel
from rest_framework.response import Response


@api_view(['GET'])
def api_list(request):
    """
    List all api, and  create a new api instance.
    """
    if request.method == 'GET':
        api_create = ApiModel()
        # create an instance of the api
        api_create.save()
        # save it, we set default for the two fields already in the model

        api = ApiModel.objects.all()
        serializer = ApiSerializers(api, many=True)
        return Response(serializer.data)



# class ApiViewSet(viewsets.ModelViewSet):
#     queryset = ApiModel.objects.all()
#     serializer_class = ApiSerializers
