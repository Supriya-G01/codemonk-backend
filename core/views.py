from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .utils import tokenize_and_store, search_paragraphs


class SomeProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hello from a protected view!"})


class ParagraphUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        text = request.data.get("text", "")
        ids = tokenize_and_store(text)
        return Response({"paragraph_ids": ids})


class WordSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        word = request.query_params.get("word")
        if not word:
            return Response({"error": "Missing 'word' parameter"}, status=400)

        paragraphs = search_paragraphs(word)
        return Response({"results": [p.text for p in paragraphs]})
