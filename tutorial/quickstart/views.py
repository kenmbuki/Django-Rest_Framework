from quickstart.models import Quickstart
from quickstart.serializers import QuickstartSerializer
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from quickstart.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from quickstart.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import detail_route


class QuickstartViewSet(viewsets.ModelViewSet):
    queryset = Quickstart.objects.all()
    serializer_class = QuickstartSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        quickstart = self.get_object()
        return Response(quickstart.highlighted)

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'quickstart': reverse('quickstart-list', request=request, format=format)
        })


"""
class QuickstartList(generics.ListCreateAPIView):
    queryset = Quickstart.objects.all()
    serializer_class = QuickstartSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class QuickstartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quickstart.objects.all()
    serializer_class = QuickstartSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
class QuickstartHighlight(generics.GenericAPIView):
    queryset = Quickstart.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(quickstart.highlighted)

"""


"""
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
"""

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