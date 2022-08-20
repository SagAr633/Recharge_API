from rest_framework.serializers import ModelSerializer
from Plans.models import Plans


class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plans
        fields = [
            'Operator',
            'Circle',
            'Plan_type',
            'Data',
            'Validity',
            'Description',
            'Price'
        ]
