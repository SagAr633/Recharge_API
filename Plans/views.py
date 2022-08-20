from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from Plans.serializers import PlanSerializer
from Plans.models import Plans


class PlansViewSet(ViewSet):
    model = Plans
    serializer_class = PlanSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def list(self,request,*args,**kwargs):
        qs = Plans.objects.all()
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data)

    def retrieve(self,request,*args,**kwargs):
        id = kwargs.get('pk')
        plan = Plans.objects.get(id=id)
        serializer = self.serializer_class(instance=plan, data=request.data)
        return Response(serializer.data)