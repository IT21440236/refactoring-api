from django.urls import path
from .views import RefactorCodeView

urlpatterns = [
    path('refactor/', RefactorCodeView.as_view(), name='refactor-code'),
]
