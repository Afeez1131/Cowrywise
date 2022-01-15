from rest_framework import serializers

from api.models import ApiModel


class ApiSerializers(serializers.ModelSerializer):
    # timestamp = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    timestamp = serializers.DateTimeField(format="iso-8601",
                                          input_formats=None)

    class Meta:
        model = ApiModel
        fields = ('pk', 'timestamp', 'identifier')

