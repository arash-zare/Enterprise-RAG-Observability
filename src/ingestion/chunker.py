
from __future__ import annotations
from dataclasses import dataclass


# چانکینگ ساده بر اساس تعداد کاراکتر + overlap:

@dataclass
class Chunk:
    source: str
    chunk_id: int
    text: str

def chunk_text(source: str, text: str, chunk_size: int = 800, overlap: int = 120) -> list[Chunk]:
    text = text.strip()
    if not text:
        return []

    chunks: list[Chunk] = []
    start = 0
    cid = 0

    while start < len(text):
        end = min(len(text), start + chunk_size)
        chunk_str = text[start:end].strip()

        if chunk_str:
            chunks.append(Chunk(source=source, chunk_id=cid, text=chunk_str))
            cid += 1

        if end == len(text):
            break

        start = max(0, end - overlap)

    return chunks
