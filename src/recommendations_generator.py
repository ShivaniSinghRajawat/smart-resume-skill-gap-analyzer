def generate_recommendations(skills_needed, skills_acquired):
    """
    Generate recommendations based on needed skills and acquired skills.
    
    Args:
    skills_needed (list): A list of skills required for a role.
    skills_acquired (list): A list of skills the user has acquired.
    
    Returns:
    list: A list of recommendations for skills to focus on.
    """
    recommendations = []
    
    for skill in skills_needed:
        if skill not in skills_acquired:
            recommendations.append(f"Consider developing your {skill} skills.")
    
    if not recommendations:
        recommendations.append("You have all the necessary skills!")
    
    return recommendations

if __name__ == '__main__':
    needed_skills = ['Python', 'Data Analysis', 'Machine Learning']
    acquired_skills = ['Python', 'SQL']
    
    recommendations = generate_recommendations(needed_skills, acquired_skills)
    print(recommendations)