import re


def clean_text(text):
    """
    Clean and normalize extracted document text.
    """

    if not text:
        return ""

    # Convert to lowercase
    text = text.lower()

    # Replace common separators with spaces
    text = re.sub(r"[\r\n\t]+", " ", text)

    # Keep useful technical characters such as +, # and .
    text = re.sub(
        r"[^a-z0-9+#.\-/ ]",
        " ",
        text
    )

    # Remove repeated whitespace
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def normalize_text(text):
    """
    Normalize text for semantic comparison.
    """

    text = clean_text(text)

    # Normalize common variations
    replacements = {
        "machine-learning": "machine learning",
        "deep-learning": "deep learning",
        "natural-language-processing":
            "natural language processing",
        "artificial-intelligence":
            "artificial intelligence",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def split_into_sections(text):
    """
    Attempt to identify common resume sections.
    """

    sections = {}

    section_patterns = {
        "skills": r"\bskills?\b",
        "experience": r"\b(experience|work experience|employment)\b",
        "education": r"\b(education|academic background)\b",
        "projects": r"\b(projects?|academic projects)\b",
        "certifications": r"\b(certifications?|certificates?)\b",
        "summary": r"\b(summary|profile|objective)\b",
    }

    lines = [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

    current_section = "general"

    sections[current_section] = []

    for line in lines:

        matched_section = None

        for section, pattern in section_patterns.items():

            if re.search(pattern, line, re.IGNORECASE):
                matched_section = section
                break

        if matched_section:

            current_section = matched_section

            if current_section not in sections:
                sections[current_section] = []

        else:

            sections[current_section].append(line)

    # Convert lists to strings
    for section in sections:
        sections[section] = " ".join(
            sections[section]
        )

    return sections
