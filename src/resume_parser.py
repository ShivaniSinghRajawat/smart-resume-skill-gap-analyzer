import pdfplumber
import os

class ResumeParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = self.extract_text()

    def extract_text(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("Resume file does not exist.")
        with pdfplumber.open(self.file_path) as pdf:
            text = ''.join(page.extract_text() for page in pdf.pages)
        return text

    def get_skills(self):
        # Placeholder method for extracting skills
        # Implement logic to parse self.text and extract skills
        pass

    def get_experience(self):
        # Placeholder method for extracting experience
        # Implement logic to parse self.text and extract experience
        pass

# Example usage:
# parser = ResumeParser('path/to/resume.pdf')
# print(parser.get_skills())
# print(parser.get_experience())
