import fitz


def extract_pdf_text(uploaded_file):
    """
    Extract text from an uploaded PDF resume.
    """

    document = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


def extract_pdf_from_path(file_path):
    """
    Extract text from a PDF using its file path.
    """

    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text
