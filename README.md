Django DRF проект с использованием Insomnia

Этот проект написан с использованием классов GenericAPIView и mixins.

Использованы следующие mixins:
- RetrieveModelMixin (получение одной записи)
- UpdateModelMixin (обновление записи)
- DestroyModelMixin (удаление записи)
- ListModelMixin (получение списка записей)
- CreateModelMixin (создание новой записи)
__________________________________________________________________________
Так же использованы Viewset's

-Accounts:
    - SignUpView, with POST request true INSOMNIA 
    - Django Adminsite - checking
    - SignUpSerializer 

```python
from rest_framework import generics
from rest_framework.mixins import (RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
                                   ListModelMixin, CreateModelMixin)

class YourModelViewSet(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin,
                       ListModelMixin, CreateModelMixin):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer

    # Дополнительные методы и настройки



