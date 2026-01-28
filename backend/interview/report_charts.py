import matplotlib.pyplot as plt
import os
'''
def generate_score_chart(eye_contact, confidence, session_id):
    labels = ['Eye Contact', 'Confidence']
    scores = [eye_contact, confidence * 10]  # scale confidence to 100

    plt.figure()
    plt.bar(labels, scores)
    plt.ylim(0, 100)
    plt.title('Mock Interview Performance')

    os.makedirs("reports", exist_ok=True)
    chart_path = f"reports/session_{session_id}_scores.png"

    plt.savefig(chart_path)
    plt.close()

    return chart_path
'''
import matplotlib.pyplot as plt
import os

def generate_score_chart(eye_contact, confidence, session_id):
    labels = ['Eye Contact', 'Confidence']
    scores = [eye_contact, confidence * 10]  # scale confidence to 100

    plt.figure()
    plt.bar(labels, scores)
    plt.ylim(0, 100)
    plt.title('Mock Interview Performance')

    os.makedirs("reports", exist_ok=True)
    chart_path = f"reports/session_{session_id}_scores.png"

    plt.savefig(chart_path)
    plt.close()

    return chart_path
