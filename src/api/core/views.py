from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class BaseAPIView(APIView):
    """
    Intermediate placeholder layer for custom project-wide methods and attributes
    """
    pass


class GenericAPIListView(BaseAPIView):
    """
    Generic List View for CRUD using Services abstraction
    """

    serializer_class = None
    service_class = None

    def get(self, request, format=None):
        obj_list = self.service_class.get_list()
        response_serializer = self.serializer_class(obj_list, many=True)
        return Response(response_serializer.data)

    def post(self, request, format=None):
        request_serializer = self.serializer_class(data=request.data)

        if not request_serializer.is_valid():
            return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        obj = self.service_class.create_object(request_serializer.validated_data)
        response_serializer = self.serializer_class(obj)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class GenericAPIView(BaseAPIView):
    """
    Generic View for CRUD using Services abstraction
    """

    serializer_class = None
    service_class = None

    def get(self, request, pk, format=None):
        try:
            obj = self.service_class.get_object(pk)
        except KeyError:
            raise Http404
        response_serializer = self.serializer_class(obj)
        return Response(response_serializer.data)

    def put(self, request, pk, format=None):
        request_serializer = self.serializer_class(data=request.data)

        if not request_serializer.is_valid():
            return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            obj = self.service_class.update_object(pk, request_serializer.validated_data)
        except KeyError:
            raise Http404
        response_serializer = self.serializer_class(obj)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        try:
            self.service_class.delete_object(pk)
        except KeyError:
            raise Http404
        return Response({"message": "Deleted"}, status=status.HTTP_200_OK)
