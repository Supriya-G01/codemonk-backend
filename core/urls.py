from django.urls import path
from .views import SomeProtectedView, ParagraphUploadView, WordSearchView

urlpatterns = [
    path('test/', SomeProtectedView.as_view(), name='test'),
    path('upload/', ParagraphUploadView.as_view(), name='upload'),
    path('search/', WordSearchView.as_view(), name='search'),
]
