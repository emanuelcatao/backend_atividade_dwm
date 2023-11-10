from rest_framework import viewsets
from rest_framework.response import Response

from .models import Log
import json

class LogSerializer():
    class Meta:
        model = Log
        fields = '__all__'

class LogApiView(viewsets.ModelViewSet):
    serializer_class = LogSerializer

    def get_queryset(self):
        queryset = None

        return queryset
    
    def create(self, request, *args, **kwargs):
        print(f'Data: {request.data}')
        num1 = float(request.data.get('num1'))
        num2 = float(request.data.get('num2'))
        op = request.data.get('op')

        novo_item = Log()

        novo_item.num1 = num1
        novo_item.num2 = num2
        novo_item.op = op

        match op:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '/':
                result = num1 / num2
            case '*':
                result = num1 * num2
        
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

    