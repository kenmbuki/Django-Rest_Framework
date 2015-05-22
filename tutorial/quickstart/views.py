from quickstart.models import Quickstart
from quickstart.serializers import QuickstartSerializer
from rest_framework import generics


class QuickstartList(generics.ListCreateAPIView):
    queryset = Quickstart.objects.all()
    serializer_class = QuickstartSerializer

class QuickstartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quickstart.objects.all()
    serializer_class = QuickstartSerializer








"""
@api_view(['GET', 'PUT', 'DELETE'])
def quickstart_detail(request, pk, format=None):
    try:
        quickstart = Quickstart.objects.get(pk=pk)
    except Quickstart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuickstartSerializer(quickstart)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuickstartSerializer(quickstart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        quickstart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def quickstart_list(request, format=None):

 #List all or create new
    if request.method == 'GET':
        quickstart = Quickstart.objects.all()
        serializer = QuickstartSerializer(quickstart, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuickstartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""


"""
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def quickstart_list(request):
    #List all code, or create a new  snippet
    if request.method == 'GET':
      quickstart = Quickstart.objects.all()
      serializers = QuickstartSerializer(quickstart, many=True)
      return JSONResponse(serializers.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuickstartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def quickstart_detail(request, pk):
    try:
        quickstart = Quickstart.objects.get(pk=pk)
    except Quickstart.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuickstartSerializer(quickstart)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuickstartSerializer(quickstart, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        quickstart.delete()
        return HttpResponse(status=204)
"""