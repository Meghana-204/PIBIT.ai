import re
import json

def parse_resume(resume_text):
    parsed_resume = {
        "name": "",
        "contactInformation": {
            "email": "",
            "phone": "",
            "address": ""
        },
        "professionalSummary": "",
        "skills": [],
        "workExperience": [],
        "education": [],
        "certifications": [],
        "projects": []
    }
    
    # Parse sections of the resume
    parsed_resume['name'] = re.search(r'Name:\s*(.*)', resume_text).group(1)
    parsed_resume['contactInformation']['email'] = re.search(r'Email:\s*(.*)', resume_text).group(1)
    parsed_resume['contactInformation']['phone'] = re.search(r'Phone:\s*(.*)', resume_text).group(1)
    parsed_resume['contactInformation']['address'] = re.search(r'Address:\s*(.*)', resume_text).group(1)
    parsed_resume['professionalSummary'] = re.search(r'Professional Summary:\s*(.*)', resume_text).group(1)
    
    # Parse skills
    skills = re.search(r'Skills:\s*(.*)', resume_text).group(1)
    parsed_resume['skills'] = [skill.strip() for skill in skills.split(',')]
    
    # Parse work experience
    work_experience_matches = re.findall(r'Job Title:\s*(.*?)\s*Company:\s*(.*?)\s*Location:\s*(.*?)\s*Start Date:\s*(.*?)\s*End Date:\s*(.*?)\s*Responsibilities:\s*(.*?)\s*(?=Job Title|Education|$)', resume_text, re.DOTALL)
    for match in work_experience_matches:
        parsed_resume['workExperience'].append({
            "jobTitle": match[0],
            "company": match[1],
            "location": match[2],
            "startDate": match[3],
            "endDate": match[4],
            "responsibilities": [resp.strip() for resp in match[5].split(',')]
        })
    
    # Parse education
    education_matches = re.findall(r'Degree:\s*(.*?)\s*Institution:\s*(.*?)\s*Location:\s*(.*?)\s*Graduation Year:\s*(.*?)\s*(?=Degree|Certifications|$)', resume_text, re.DOTALL)
    for match in education_matches:
        parsed_resume['education'].append({
            "degree": match[0],
            "institution": match[1],
            "location": match[2],
            "graduationYear": match[3]
        })
    
    # Parse certifications
    certification_matches = re.findall(r'Certification Name:\s*(.*?)\s*Institution:\s*(.*?)\s*Year:\s*(.*?)\s*(?=Certification Name|Projects|$)', resume_text, re.DOTALL)
    for match in certification_matches:
        parsed_resume['certifications'].append({
            "name": match[0],
            "institution": match[1],
            "year": match[2]
        })
    
    # Parse projects
    project_matches = re.findall(r'Project Title:\s*(.*?)\s*Description:\s*(.*?)\s*Technologies Used:\s*(.*?)\s*(?=Project Title|$)', resume_text, re.DOTALL)
    for match in project_matches:
        parsed_resume['projects'].append({
            "title": match[0],
            "description": match[1],
            "technologiesUsed": [tech.strip() for tech in match[2].split(',')]
        })
    
    return parsed_resume

resume_text = """
Name: John Doe
Email: john.doe@example.com
Phone: 123-456-7890
Address: 123 Main St, Anytown, USA

Professional Summary: Experienced AI/ML professional with a strong background in NLP and data analysis.

Skills: Python, Machine Learning, NLP, Data Analysis

Work Experience:
Job Title: AI Engineer
Company: TechCorp
Location: New York, NY
Start Date: January 2020
End Date: Present
Responsibilities: Developed AI models, Analyzed data sets, Collaborated with cross-functional teams

Education:
Degree: Bachelor of Science in Computer Science
Institution: University of Anytown
Location: Anytown, USA
Graduation Year: 2019

Certifications:
Certification Name: Prompt Engineering Specialist
Institution: Coursera
Year: 2023

Projects:
Project Title: NLP Chatbot
Description: Developed an NLP-based chatbot for customer service
Technologies Used: Python, spaCy, TensorFlow
"""

parsed_resume = parse_resume(resume_text)
print(json.dumps(parsed_resume, indent=4))
