def analyze_behavior(transcript):
    filler_words = ["um", "uh", "like"]
    count = sum(transcript.lower().count(w) for w in filler_words)

    confidence = max(0.5, 1 - count * 0.05)

    return {
        "confidence": round(confidence, 2),
        "clarity": round(confidence * 0.9, 2)
    }
