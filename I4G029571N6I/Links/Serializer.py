from rest_framework import serializers
from . models import Link

class LinkSerializer(serializers.modelSerializers):
    class meta:
        model = Link
        fields = "__all__"