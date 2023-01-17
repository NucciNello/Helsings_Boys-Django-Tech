from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
# from rest_framework import status
# from rest_framework import permissions
from .serializers import ProfileSerializers
from .models import Profile


class ProfilesList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers

    # def get(self, request):
    #     profiles = Profile.objects.all()[:5]
    #     data = ProfileSerializers(profiles, many = True).data
    #     return Response(data)


class ProfileList(generics.RetrieveDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers

    # def get(self, request, pk):
    #     profile = get_object_or_404(Profile, pk=pk)
    #     data = ProfileSerializers(profile).data
    #     return Response(data)

