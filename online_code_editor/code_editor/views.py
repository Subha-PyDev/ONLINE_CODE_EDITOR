from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.contrib.auth.models import User

from .models import CodeSnippet
from .serializers import CodeSnippetSerializer, UserSerializer

import subprocess
import json

# User Registration API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# List & Create Code Snippets (authenticated)
class CodeSnippetListCreate(generics.ListCreateAPIView):
    serializer_class = CodeSnippetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CodeSnippet.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        code = self.request.data.get("code")
        output = execute_python_code(code)
        serializer.save(user=self.request.user, output=output)

# Safe code execution logic
def execute_python_code(code):
    try:
        result = subprocess.run(
            ['python', '-c', code],  # Use 'python' on Windows
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=5,
            text=True
        )
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return "Execution timed out!"
    except Exception as e:
        return f"Error: {str(e)}"


# Serve frontend template
class IndexView(TemplateView):
    template_name = "index.html"

# API to execute code without saving it
@method_decorator(csrf_exempt, name="dispatch")
class RunCodeView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            code = data.get("code", "")
            output = execute_python_code(code)
            return Response({"output": output}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
