import pandas as pd

def analyze_skill_gaps(user_skills, job_requirements):
    """
    Analyzes the skill gaps between user skills and job requirements.

    Parameters:
    user_skills (list): A list of skills the user possesses.
    job_requirements (list): A list of skills required for the job.

    Returns:
    dict: A dictionary containing skills user has, skills required, and skill gaps.
    """
    user_set = set(user_skills)
    job_set = set(job_requirements)

    skills_user_has = user_set.intersection(job_set)
    skills_required = job_set
    skill_gaps = job_set - user_set

    return {
        "skills_user_has": list(skills_user_has),
        "skills_required": list(skills_required),
        "skill_gaps": list(skill_gaps)
    }

# Example usage:
if __name__ == '__main__':
    user_skills = ['Python', 'Data Analysis', 'Machine Learning']
    job_requirements = ['Python', 'Data Analysis', 'Deep Learning']
    result = analyze_skill_gaps(user_skills, job_requirements)
    print(result)