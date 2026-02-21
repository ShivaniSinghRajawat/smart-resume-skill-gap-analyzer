import re
import nltk

# Ensure you have installed nltk and downloaded the necessary resources
# nltk.download('punkt')

class SkillExtractor:
    def __init__(self, text):
        self.text = text
        self.skills = []

    def extract_skills(self):
        # This is a simple regex for demonstration purposes
        skill_keywords = ['Python', 'Java', 'Excel', 'Data Analysis', 'Machine Learning', 'NLP', 'Communication', 'Teamwork']
        for skill in skill_keywords:
            if re.search(r'\b' + re.escape(skill) + r'\b', self.text, re.IGNORECASE):
                self.skills.append(skill)
        return self.skills

# Sample usage
if __name__ == '__main__':
    sample_text = "I have experience in Python and Machine Learning."
    extractor = SkillExtractor(sample_text)
    found_skills = extractor.extract_skills()
    print(f'Extracted skills: {found_skills}')