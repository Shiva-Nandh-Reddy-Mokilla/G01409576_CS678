# pdf_reader.py
import PyPDF2
from gentopia.tools.basetool import BaseTool

class PdfReaderTool(BaseTool):
    name = "pdf_reader"
    description = ("Read a PDF file, extract text content, and provide summarization.")

    def _run(self, pdf_path: str) -> str:
        with open(pdf_path, "rb") as pdf_file:
            reader = PyPDF2.PdfFileReader(pdf_file)
            num_pages = reader.numPages
            text_content = ""
            for page_num in range(num_pages):
                page = reader.getPage(page_num)
                text_content += page.extractText()
            # Perform summarization on text_content if needed
            summary = self.summarize_text(text_content)
            return summary

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

    def summarize_text(self, text: str) -> str:
        # Add your summarization logic here
        # This could be simple extractive summarization or more advanced techniques
        # For example, using NLP libraries like Gensim or SpaCy
        # Here's a simple example using the first 300 characters as the summary
        summary = text[:300]
        return summary
