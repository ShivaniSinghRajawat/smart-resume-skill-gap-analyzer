import re
import json

class ResumeParser:
    """
    A class to parse resumes and extract various components like personal info,
    work experience, education, skills, certifications, and language detection.
    """

    def __init__(self, resume_text):
        """
        Initializes the ResumeParser with a resume text.
        
        Parameters:
        resume_text (str): The text content of the resume to be parsed.
        """
        self.resume_text = resume_text
        self.personal_info = {}
        self.work_experience = []
        self.education = []
        self.skills = []
        self.certifications = []
        self.languages = []

    def extract_personal_info(self):
        """
        Extracts personal information from the resume.
        Populates the personal_info dictionary.
        """  
        # Example regex for email and phone number
        email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        phone_regex = r'\b\d{10}\b|\b\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}\b'
        self.personal_info['email'] = re.findall(email_regex, self.resume_text)
        self.personal_info['phone'] = re.findall(phone_regex, self.resume_text)

    def extract_work_experience(self):
        """
        Extracts work experience details from the resume.
        Appends job experiences to the work_experience list.
        """  
        # Dummy implementation, replace with actual logic
        self.work_experience.append({
            'job_title': 'Software Engineer',
            'company': 'Example Corp',
            'duration': '2018-2021',
            'description': 'Developed software solutions.'
        })

    def extract_education(self):
        """
        Extracts educational qualifications from the resume.
        Appends education details to the education list.
        """  
        # Dummy implementation, replace with actual logic
        self.education.append({
            'degree': 'B.Sc. in Computer Science',
            'institution': 'University of Example',
            'year': '2018'
        })

    def extract_skills(self):
        """
        Extracts skills from the resume.
        Populates the skills list.
        """  
        # Dummy implementation, replace with actual logic
        self.skills = ['Python', 'Data Analysis', 'Machine Learning']

    def extract_certifications(self):
        """
        Extracts certifications from the resume.
        Appends certification details to the certifications list.
        """  
        # Dummy implementation, replace with actual logic
        self.certifications.append('AWS Certified Solutions Architect')

    def detect_languages(self):
        """
        Detects languages spoken by the candidate.
        Populates the languages list.
        """  
        # Dummy implementation, replace with actual logic
        self.languages = ['English', 'Spanish']

    def parse_resume(self):
        """
        Parses the resume to extract all necessary information.
        Calls all extraction methods.
        """  
        self.extract_personal_info()
        self.extract_work_experience()
        self.extract_education()
        self.extract_skills()
        self.extract_certifications()
        self.detect_languages()

    def to_json(self):
        """
        Converts the extracted resume information to JSON format.
        
        Returns:
        str: JSON string representation of the extracted information.
        """  
        return json.dumps({
            'personal_info': self.personal_info,
            'work_experience': self.work_experience,
            'education': self.education,
            'skills': self.skills,
            'certifications': self.certifications,
            'languages': self.languages
        }, indent=4)

# Example usage:
# with open('resume.txt', 'r') as file:
#     text = file.read()
# parser = ResumeParser(text)
# parser.parse_resume()
# print(parser.to_json())
