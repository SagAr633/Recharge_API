from Recharge.models import Recharge
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class RechargeSerializer(ModelSerializer):
    user = serializers.CharField(read_only=True)
    id = serializers.CharField(read_only=True)
    depth = 2

    class Meta:
        model = Recharge
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('user')
        return Recharge.objects.create(**validated_data, user=user)
