from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from refactor_project.model_runner import run_refactor_model  # ← actual model logic

class RefactorCodeView(APIView):
    def post(self, request):
        code = request.data.get("code")
        if not code:
            return Response({"error": "Code input is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            config = {
                "num_beams": request.data.get("num_beams", 5),
                "max_length": request.data.get("max_length", 512),
                "temperature": request.data.get("temperature", 1.0),
                "top_k": request.data.get("top_k", 50),
                "top_p": request.data.get("top_p", 0.95)
            }

            refactored_code = run_refactor_model(code, config)
            return Response({"refactored_code": refactored_code}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
