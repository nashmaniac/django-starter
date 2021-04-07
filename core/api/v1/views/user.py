from rest_framework.views import APIView
from core.utils import CoreResponse


class UserApiView(APIView):
    def get(self, request):
        try:
            return CoreResponse.send(dict(
                username=request.user.username
            ), 200)
        except Exception as exc:
            return CoreResponse.send(dict(
                status=500,
                message=str(exc)
            ), 500)
