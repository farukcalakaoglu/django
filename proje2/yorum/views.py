from django.shortcuts import render
from rest_framework import generics
from .models import Yorum
from .serializers import YorumSerializers,YorumListSerializers,YorumDetailsSerializers
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser
#admin liste
@api_view(["GET"])
@permission_classes([IsAdminUser])
def admin_liste(request):
    yy=Yorum.objects.all()
    serialisers=YorumListSerializers(yy,many=True)
    return Response(serialisers.data)
#------------------------------------------------------------------------------------------------

#yorum listele
@api_view(["GET"])
def yorum_liste(request):
    yorum=Yorum.objects.all()
    serializers=YorumListSerializers(yorum,many=True)
    return Response(serializers.data)

 #------------------------------------------------------------------------------------------------

#yorum id göre
@api_view(["GET"])
def yorum_id(request,pk):
    try:
        yorum=Yorum.objects.get(pk=pk)
    except Yorum.DoesNotExist:
        return Response({"error":"verilen id yorum yok"})
    
    serializers=YorumDetailsSerializers(yorum)
    return Response(serializers.data)
#------------------------------------------------------------------------------------------------

#admin yorum guncelleme
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def admin_guncelleme(request,pk):
    yorum=Yorum.objects.get(pk=pk)
    serializers=YorumSerializers(yorum,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    else:
        return Response(serializers.errors)
    
#------------------------------------------------------------------------------------------------
#yorum olusturma 
@api_view(["POST"])
def  create_yorum(request):
 serializers=YorumSerializers(data=request.data)
 if serializers.is_valid():
     serializers.save()
     return Response(serializers.data,status=status.HTTP_201_CREATED)
 else:
     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
 
#------------------------------------------------------------------------------------------------
@api_view([ "DELETE"])
def yorum_sil(request,pk):
    try:
        yorum=Yorum.objects.get(pk=pk)
    except yorum.DoesNotExist:
        return Response({"error":"yorum bulunamadı"},status=404)
    yorum.delete()
    return Response({"message":"yorum silindi.."})
    