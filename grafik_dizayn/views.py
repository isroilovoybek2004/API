from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from grafik_dizayn.models import Kurs
from grafik_dizayn.serializer import KursSerializer


# Create your views here.


# [generics]
# class KurslarAPIView(generics.ListAPIView):
#     serializer_class = KursSerializer
#     queryset = Kurs.objects.all()
#     lookup_field = 'pk'
#
#
# class KursDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = KursSerializer
#     queryset = Kurs.objects.all()
#     lookup_field = 'pk'


# #[APIView][CRUD]
# class KurslarAPIView(APIView):
#     def get(self, request):
#         kurs = Kurs.objects.all()
#         serializer = KursSerializer(kurs, many=True)
#         return Response(data=serializer.data)
#
#     def delete(self, request, pk):
#         kurs = Kurs.objects.get(pk=pk)
#         kurs.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def put(self, request, pk):
#         kurs = Kurs.objects.get(pk=pk)
#         serializer = KursSerializer(instance=kurs, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk):
#         kurs = Kurs.objects.get(pk=pk)
#         serializer = KursSerializer(instance=kurs, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# [viewsets]
# class KursCRUD(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated, ]
#     serializer_class = KursSerializer
#     queryset = Kurs.objects.all()
#     lookup_field = 'pk'







