import os
import sys
import fitz  # PyMuPDF
import docx
from pptx import Presentation
from util.fileTypes import FileTypeClassifier

def classify(self, file_path):
    ext = os.path.splitext(file_path)[1].lower()
    return self.file_types.get(ext, "unknown")

classifier = FileTypeClassifier()

def extract_text_from_docx(file_path):
    docx.opendocx(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_xlsx(file_path):
    df = pd.read_excel(file_path, engine="openpyxl")
    return df.to_string(index=False)

def extract_text_from_pptx(file_path):
    prs = Presentation(file_path)
    text = []
    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text.append(shape.text)
    return "\n".join(text)

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = "\n".join([page.get_text() for page in doc])
    return text if text else "No extractable text found."

def extract_text(file_path):
    file_type = classifier.classify(file_path)

    if file_type == "word":
        return extract_text_from_docx(file_path)
    elif file_type == "excel":
        return extract_text_from_xlsx(file_path)
    elif file_type == "powerpoint":
        return extract_text_from_pptx(file_path)
    elif file_type == "pdf":
        return extract_text_from_pdf(file_path)
    else:
        return "Unsupported file format."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print("File not found.")
        sys.exit(1)

    extracted_text = extract_text(file_path)
    print("\nExtracted Content:\n")
    print(extracted_text)