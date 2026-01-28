from rest_framework.views import APIView
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .ai_avatar import start_avatar_interview
from .question_generator import generate_questions
from .models import Resume, InterviewSession
from .vision_analyzer import analyze_interview
from rest_framework.permissions import IsAuthenticated
from .report_charts import generate_score_chart
from .pdf_report import generate_pdf_report
from .whisper_service import speech_to_text
from rest_framework import status
from interview.report_charts import generate_score_chart
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .behavior_analyzer import analyze_behavior
from .resume_parser import parse_resume
from interview.whisper_service import speech_to_text
from interview.pdf_report import generate_pdf_report
class ResumeUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        pdf = request.FILES.get('resume')
        role = request.data.get('role')

        resume = Resume.objects.create(user=request.user, pdf=pdf)

        skills = parse_resume(resume.pdf.path)
        resume.skills = ", ".join(skills)
        resume.save()

        questions = start_avatar_interview(role)


        return Response({
            "skills": skills,
            "ai_avatar": "Mock Interviewer Bot",
            "questions_asked": questions,
        })

from .vision_analyzer import analyze_interview
from .models import InterviewSession

@method_decorator(csrf_exempt, name='dispatch')
class StartInterviewView(APIView):
    permission_classes = []

    def post(self, request):
        role = request.data.get("role", "SDE")
        audio_path = request.data.get("audio_path")

        if not audio_path:
            return Response(
                {"error": "audio_path is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # 1️⃣ Vision analysis
            # 1️⃣ Vision analysis
            eye_contact = analyze_interview()

            # 2️⃣ Speech-to-text
            transcript = speech_to_text(audio_path)

            # 3️⃣ Behavior analysis
            behavior_scores = analyze_behavior(eye_contact, transcript)

            eye_contact_score = behavior_scores["eye_contact_score"]
            confidence_score = behavior_scores["confidence_score"]

            # 2️⃣ Speech-to-text (Whisper)
            transcript = speech_to_text(audio_path)

            # 3️⃣ Create interview session
            session = InterviewSession.objects.create(
                user=request.user if request.user.is_authenticated else None,
                role=role,
                eye_contact_score=eye_contact_score,
                confidence_score=confidence_score
            )


            # 4️⃣ Generate chart
            chart_path = generate_score_chart(
                eye_contact_score,
                confidence_score,
                session.id
            )


            # 5️⃣ Generate PDF report
            pdf_path = generate_pdf_report(
                session=session,
                transcript=transcript,
                chart_path=chart_path
            )

            return Response({
                
                "eye_contact_score": eye_contact,
                "confidence_score": confidence_score,
                "transcript": transcript,
                "chart_path": chart_path,
                "pdf_path": pdf_path
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )