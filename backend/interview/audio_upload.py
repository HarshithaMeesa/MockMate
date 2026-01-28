from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os

class AudioUploadView(APIView):
    def post(self, request):
        audio = request.FILES.get("audio")
        if not audio:
            return Response({"error": "No audio"}, status=400)

        os.makedirs("media/audio", exist_ok=True)

        path = f"media/audio/{audio.name}"
        with open(path, "wb+") as f:
            for chunk in audio.chunks():
                f.write(chunk)

        return Response({"message": "Audio saved", "path": path})
