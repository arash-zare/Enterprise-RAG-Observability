from dataclasses import dataclass
import os
from pathlib import Path
from typing import List
from pypdf import PdfReader


@dataclass
class Document:
    source: str
    text: str


class DocumentLoader:

    def __init__(self, directory_path: str = "data/sample_docs"):
        self.directory_path = Path(directory_path)

    def _load_pdf(self, file_path: Path) -> str:
        """استخراج متن تمام صفحات فایل PDF"""
        reader = PdfReader(str(file_path))
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text

    def _load_text_file(self, file_path: Path) -> str:
        """خواندن فایل‌های متنی و مارک‌داون"""
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def load(self) -> List[Document]:
        """پیمایش پوشه و استخراج متن تمام فایل‌های pdf, md, txt"""
        documents: List[Document] = []

        if not self.directory_path.exists():
            os.makedirs(self.directory_path, exist_ok=True)
            return documents

        for file_path in self.directory_path.glob("**/*"):
            if file_path.is_file():
                ext = file_path.suffix.lower()
                content = ""

                try:
                    if ext == ".pdf":
                        content = self._load_pdf(file_path)
                    elif ext in [".txt", ".md"]:
                        content = self._load_text_file(file_path)

                    if content.strip():
                        documents.append(
                            Document(source=str(file_path), text=content.strip())
                        )
                except Exception as e:
                    print(f"⚠️ Error loading file {file_path}: {e}")

        return documents


def load_documents(directory_path: str = "data/sample_docs") -> List[Document]:
    """تابع ورودی استاندارد برای خط لوله Ingestion"""
    loader = DocumentLoader(directory_path=directory_path)
    return loader.load()
