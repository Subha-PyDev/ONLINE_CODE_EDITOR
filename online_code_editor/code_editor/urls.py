from django.urls import path
from .views import RegisterView, CodeSnippetListCreate, RunCodeView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('snippets/', CodeSnippetListCreate.as_view(), name='snippets'),
    path('run-code/', RunCodeView.as_view(), name='run_code'),
]
