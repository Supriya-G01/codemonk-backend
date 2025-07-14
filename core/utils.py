from .models import Paragraph, WordIndex
from django.db import transaction


def tokenize_text(paragraph_text):
    """
    Tokenize the paragraph into words.
    - Converts to lowercase
    - Splits on whitespace
    """
    return paragraph_text.lower().split()


@transaction.atomic
def tokenize_and_store(paragraph_text):
    """
    Splits text by paragraphs, tokenizes, and stores in DB.
    A paragraph is defined by 2 newlines (`\n\n`)
    """
    paragraphs = [p.strip() for p in paragraph_text.strip().split("\n\n") if p.strip()]
    created = []

    for p_text in paragraphs:
        para = Paragraph.objects.create(text=p_text)
        words = set(tokenize_text(p_text))
        WordIndex.objects.bulk_create([
            WordIndex(word=word, paragraph=para)
            for word in words
        ])
        created.append(para.id)

    return created


def search_paragraphs(word):
    """
    Search for a word and return top 10 matching paragraphs.
    """
    word = word.lower()
    paragraph_ids = (
        WordIndex.objects.filter(word=word)
        .values_list("paragraph_id", flat=True)
        .distinct()[:10]
    )
    return Paragraph.objects.filter(id__in=paragraph_ids)
