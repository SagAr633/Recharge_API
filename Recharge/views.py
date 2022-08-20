from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from Recharge.serializers import RechargeSerializer
from Recharge.models import Recharge
from rest_framework import permissions
from rest_framework import status


class RechargeViewSet(ModelViewSet):
    model = Recharge
    serializer_class = RechargeSerializer
    queryset = Recharge.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Recharge.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Recharge successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'Recharge failed'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request, *args, **kwargs):
        qs = Recharge.objects.filter(user=request.user)
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)
