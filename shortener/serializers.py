from rest_framework import serializers

from shortener.models import Url, generate_code


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = "__all__"

    def create(self, validated_data):
        short_code = validated_data.pop('short_code', None)

        if Url.objects.filter(long_url=validated_data.get("long_url")).exists():
            return Url.objects.filter(long_url=validated_data.get("long_url")).first()

        if short_code is None:
            short_code = generate_code()
        else:
            if Url.objects.filter(short_code=short_code).exists():
                raise serializers.ValidationError("Short code already exists")
        obj = Url.objects.create(short_code=short_code, **validated_data)
        return obj

