from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api'
        'GET http://192.168.31.157:8000/api/room/',
        'GET /api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    room = Room.objects.all()
    serializer = RoomSerializer(room,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request,pk):
    rooms = Room.objects.get(id=pk)
    serializer = RoomSerializer(rooms,many=False)
    return Response(serializer.data)