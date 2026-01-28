def generate_questions(role, skills):
    questions = []

    if role == "SDE":
        if skills:
            for skill in skills:
                questions.append(f"Explain {skill} and where you used it.")
        else:
            questions.append("Explain your technical background.")

        questions += [
            "Explain OOPS concepts.",
            "What is time complexity?"
        ]

    elif role == "HR":
        questions = [
            "Tell me about yourself.",
            "What are your strengths?",
            "Why should we hire you?"
        ]

    elif role == "Analyst":
        questions = [
            "What is data preprocessing?",
            "Explain a data analysis project.",
            "What tools do you use?"
        ]

    return questions
