def analyze_behavior(eye_contact, transcript):
    """
    Simulated behavioral analysis based on:
    - eye contact score
    - length and clarity of speech
    """

    # Confidence based on speech length
    word_count = len(transcript.split())
    confidence_score = min(word_count / 50, 1.0) * 100

    return {
        "eye_contact_score": eye_contact,
        "confidence_score": round(confidence_score, 2)
    }
