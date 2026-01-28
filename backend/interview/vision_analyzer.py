import random

def analyze_interview(duration=15):
    """
    Simulated eye-contact analysis.
    In real-time system, MediaPipe FaceMesh is used.
    """
    eye_contact_percent = random.uniform(55, 85)
    return round(eye_contact_percent, 2)
