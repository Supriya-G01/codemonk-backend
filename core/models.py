from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class CustomUser(AbstractUser):
    dob = models.DateField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username   # or self.email


# --- NEW: Paragraph and WordIndex models ----------------
class Paragraph(models.Model):
    """
    Stores each paragraph of text.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # show first 50 chars for quick admin preview
        return self.text[:50]


class WordIndex(models.Model):
    """
    Fast reverse‑index: word ➜ paragraph(s).
    """
    word = models.CharField(max_length=255, db_index=True)
    paragraph = models.ForeignKey(
        Paragraph,
        related_name="word_indexes",
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("word", "paragraph")   # avoid duplicates
        indexes = [
            models.Index(fields=["word"]),
        ]

    def __str__(self):
        return f"{self.word} → {self.paragraph_id}"
