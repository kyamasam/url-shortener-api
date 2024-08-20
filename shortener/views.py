from django.shortcuts import redirect
from rest_framework import viewsets, serializers
from rest_framework.response import Response

from shortener.models import Url
from shortener.serializers import UrlSerializer


# Create your views here.
class UrlViewSet(viewsets.ModelViewSet):
    serializer_class = UrlSerializer
    queryset = Url.objects.all()
    def retrieve(self, request, pk=None):
        try:
            url = Url.objects.get(short_code=pk)
        except Url.DoesNotExist:
            raise serializers.ValidationError("could not find this url on the server")

        if url.is_expired:
            raise serializers.ValidationError("Url is expired")

        # increase visit count
        url.visits_count = url.visits_count+1
        url.save()
        serializer = UrlSerializer(url)
        return Response(serializer.data)
        # return redirect(url.long_url)
