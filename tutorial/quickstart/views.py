from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from quickstart.models import Quickstart
from quickstart.serializers import QuickstartSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def quickstart_list(request):
    """List all code, or create a new  snippet"""
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

