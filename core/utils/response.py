from rest_framework import status
from rest_framework.response import Response


class CoreResponse:
    status_dict = {
        200: status.HTTP_200_OK,
        401: status.HTTP_401_UNAUTHORIZED,
        500: status.HTTP_500_INTERNAL_SERVER_ERROR,
        403: status.HTTP_403_FORBIDDEN,
        404: status.HTTP_404_NOT_FOUND
    }

    @classmethod
    def send(cls, data, status):
        return Response(data, status=cls.status_dict[status])
