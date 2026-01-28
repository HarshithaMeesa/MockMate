from ai_avatar import ask_and_record

questions = [
    "Tell me about yourself",
    "Explain your final year project",
    "What are your strengths?",
]

answers = []

for i, q in enumerate(questions):
    audio_file = f"answer_{i}.wav"
    ask_and_record(q, audio_file)
    answers.append(audio_file)

print("Interview completed")
