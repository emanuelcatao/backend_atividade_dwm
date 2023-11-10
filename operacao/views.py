from rest_framework import viewsets, serializers
from rest_framework.response import Response

from .models import Operacao
import json

class OperacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operacao
        fields = '__all__'


class OperacaoApiView(viewsets.ModelViewSet):
    serializer_class = OperacaoSerializer

    def get_queryset(self):
        queryset = Operacao.objects.all()

        return queryset
    

    def create(self, request, *args, **kwargs):
        print(f'Data: {request.data}')
        num1 = float(request.data.get('num1'))
        num2 = float(request.data.get('num2'))
        op = request.data.get('op')

        novo_item = Operacao()

        novo_item.num1 = num1
        novo_item.num2 = num2
        novo_item.op = op

        if(novo_item.num2 != 0):
            match op:
                case '+':
                    result = num1 + num2
                case '-':
                    result = num1 - num2
                case '/':
                    result = num1 / num2
                case '*':
                    result = num1 * num2
        else:
            result = 'NaN'

        novo_item.result = result

        novo_item.save()

        responseData = {
            'id': novo_item.id,
            'num1': novo_item.num1,
            'num2': novo_item.num2,
            'op': novo_item.op,
            'result': novo_item.result,
            'data': novo_item.data.isoformat(),
        }

        print(f'Response: {responseData}')
        
        return Response(responseData,status=200)

    