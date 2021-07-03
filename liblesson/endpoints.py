from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from liblesson.serializers import ChangeEmailSerializer, UserSerializer


class ChangePasswordEndpoint(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangeEmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        request.user.email = email
        request.user.save()
        return Response({'data': UserSerializer(request.user).data})
