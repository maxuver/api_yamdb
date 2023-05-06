from rest_framework import mixins, viewsets


class ListCreateDeleteViewSet(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    """
    A viewset that provides `list`, `create`, and `delete` actions.

    Inherits from:
      - `mixins.ListModelMixin`: Provides `list` action.
      - `mixins.CreateModelMixin`: Provides `create` action.
      - `mixins.DestroyModelMixin`: Provides `delete` action.
      - `viewsets.GenericViewSet`: Provides basic viewset functionality.

    Example usage:
      class MyModelViewSet(ListCreateDeleteViewSet):
          queryset = MyModel.objects.all()
          serializer_class = MyModelSerializer
    """
    pass
