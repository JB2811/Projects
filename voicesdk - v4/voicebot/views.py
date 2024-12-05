from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import UserForm, Question, Answer
import json
from django.core.files.base import ContentFile
from django.conf import settings
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
from io import BytesIO
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib import colors
import json
import requests
from django.views.decorators.csrf import csrf_exempt
import base64
from django.utils import timezone
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import (
    DetectionModel,
    RecognitionModel,
)

FACE_API_KEY = '6vFAbJW01YLzGfbiqJJFWOUtk4Ve53HFUdH9CiqjJjzrtxjcLxBTJQQJ99AJACGhslBXJ3w3AAAKACOG7cXC'
FACE_API_URL = 'https://facevoicesdk.cognitiveservices.azure.com/'  

face_client = FaceClient(FACE_API_URL, CognitiveServicesCredentials(FACE_API_KEY))

@csrf_exempt
def face_detection(request):
    if request.method == 'POST':
        try:
            # Decode base64 image data to binary
            image_data = base64.b64decode(request.body)
            image_stream = BytesIO(image_data)

            # Perform face detection
            detected_faces = face_client.face.detect_with_stream(
                image=image_stream,
                detection_model="detection_03",  # Use model as a string
                return_face_id=False
            )

            # Check if any faces were detected
            if not detected_faces:
                return JsonResponse({'faceDetected': False, 'message': 'No faces detected'}, status=200)

            # Return face data if detected
            #face_data = [{'faceId': face.face_id, 'rect': face.face_rectangle} for face in detected_faces]
            return JsonResponse({'faceDetected': True})#, 'faceData': face_data})

        except Exception as e:
            print(f"Error in face detection: {e}")
            return JsonResponse({'error': 'Face detection failed'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def log_event(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))
            event_message = data.get('event', 'No event message provided')

            # Log the event (print here, could be saved to DB)
            log_data = {
                'event': event_message,
                'timestamp': timezone.now()
            }
            print(f"Log Event: {log_data}")  # Replace with actual logging as needed

            return JsonResponse({'success': True, 'message': 'Event logged successfully'})

        except json.JSONDecodeError as e:
            # Error decoding JSON
            return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)

        except Exception as e:
            print(f"Error logging event: {e}")
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)

def home_page(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if not user_id:
            return JsonResponse({'success': False, 'message': 'User ID is missing.'}, status=400)
        return render(request, 'home_page.html', {'user_id': user_id})

def camera_feed(request):
    return render(request, 'camera_feed.html')

def mcq_exam_page(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if not user_id:
            return JsonResponse({'success': False, 'message': 'User ID is missing.'}, status=400)
        
        # Load MCQ questions from the database
        questions = list(Question.objects.filter(question_type='MC').values(
            'id', 'question_text','question_type','options'))

        user = get_object_or_404(UserForm, id=user_id)

        # Get or create an Answer entry for the user
        answer, created = Answer.objects.get_or_create(user=user)
        
        # Initialize answers for MCQ questions if not present
        for question in questions:
            q_id = str(question['id'])
            if q_id not in answer.answers:
                answer.answers[q_id] = ""
        answer.save()
        
        return render(request, 'exam_page.html', {'questions': json.dumps(questions),'user_id': user_id})

def tf_exam_page(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if not user_id:
            return JsonResponse({'success': False, 'message': 'User ID is missing.'}, status=400)
        
        # Load True/False questions from the database
        questions = list(Question.objects.filter(question_type='TF').values(
            'id', 'question_text','question_type','options'))
      
        user = get_object_or_404(UserForm, id=user_id)

        # Get or create an Answer entry for the user
        answer, created = Answer.objects.get_or_create(user=user)
        
        # Initialize answers for TF questions if not present
        for question in questions:
            q_id = str(question['id'])
            if q_id not in answer.answers:
                answer.answers[q_id] = ""
        answer.save()
        
        return render(request, 'exam_page.html', {'questions': json.dumps(questions),'user_id': user_id})

def essay_exam_page(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if not user_id:
            return JsonResponse({'success': False, 'message': 'User ID is missing.'}, status=400)
        
        # Load Essay questions from the database
        questions = list(Question.objects.filter(question_type='ESSAY').values(
            'id', 'question_text','question_type','options'))
        print(questions);
        user = get_object_or_404(UserForm, id=user_id)

        # Get or create an Answer entry for the user
        answer, created = Answer.objects.get_or_create(user=user)
        
        # Initialize answers for Essay questions if not present
        for question in questions:
            q_id = str(question['id'])
            if q_id not in answer.answers:
                answer.answers[q_id] = ""
        answer.save()
        
        return render(request, 'exam_page.html', {'questions': json.dumps(questions),'user_id': user_id})

def fib_exam_page(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if not user_id:
            return JsonResponse({'success': False, 'message': 'User ID is missing.'}, status=400)
        
        # Load Fill in the Blanks questions from the database
        questions = list(Question.objects.filter(question_type='FIB').values(
            'id', 'question_text','question_type','options'))
      
        user = get_object_or_404(UserForm, id=user_id)

        # Get or create an Answer entry for the user
        answer, created = Answer.objects.get_or_create(user=user)
        
        # Initialize answers for FIB questions if not present
        for question in questions:
            q_id = str(question['id'])
            if q_id not in answer.answers:
                answer.answers[q_id] = ""
        answer.save()
        
        return render(request, 'exam_page.html', {'questions': json.dumps(questions),'user_id': user_id})

def thankyou(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        return render(request, 'thankyou.html', {})

def guidelines(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        return render(request, 'guidelines.html', {})


def exam(request):
    if request.method == 'POST':
        questions = list(Question.objects.all().values('id', 'question_text','options','question_type'))
        return JsonResponse(questions, safe=False)

def submit_answer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        question_id = data.get('question_id')
        answer_text = data.get('answer_text')

        user = get_object_or_404(UserForm, id=user_id)
        question = get_object_or_404(Question, id=question_id)

        # Get or create an Answer entry for the user
        answer, created = Answer.objects.get_or_create(user=user)
        
        # Update the answer JSON field
        answers = answer.answers
        answers[str(question_id)] = answer_text
        answer.answers = answers
        answer.save()

        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=400)

def generate_pdf(answers):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    style = styles['Normal']

    # Add a title to the PDF
    title = Paragraph("Exam Answers", styles['Title'])
    elements.append(title)
    elements.append(Paragraph("<br/><br/>", style))  # Add spacing after the title

    # Retrieve all questions from the database and create a dictionary for easy access
    questions = list(Question.objects.all().values(
        'id', 'question_text', 'question_type', 'options'))
    questions_dict = {str(q['id']): q for q in questions}

    # Create a mapping of question IDs to their respective question numbers for sorting
    question_number_map = {str(q['id']): q['id'] for q in questions}

    # Sort the answers based on the question number to maintain order in the PDF
    sorted_answers = sorted(
        answers.items(),
        key=lambda x: question_number_map.get(x[0], 0)
    )

    for question_id, answer_text in sorted_answers:
        question = questions_dict.get(question_id)
        if not question:
            continue  # Skip if the question is not found

        question_number = question['id']
        question_text = question['question_text']
        question_type = question['question_type']
        options = question.get('options', [])

        # Format the answer based on the question type
        if question_type == 'MC':
            try:
                # Find the index of the selected option to determine its letter (A, B, C, ...)
                option_index = options.index(answer_text)
                option_letter = chr(65 + option_index)  # 65 is the ASCII code for 'A'
                formatted_answer = f"{option_letter}. {answer_text}"
            except ValueError:
                # If the answer_text is not found in options, use it as is
                formatted_answer = answer_text
            answer_display = formatted_answer

        elif question_type == 'TF':
            # For True/False questions, the answer is either 'True' or 'False'
            answer_display = answer_text

        elif question_type == 'FIB':
            # For Fill in the Blanks, display the user's input
            answer_display = answer_text

        elif question_type == 'ESSAY':
            # For Essay questions, display the user's input
            answer_display = answer_text

        else:
            # Default case for any other question types
            answer_display = answer_text

        # Create Paragraph objects for the question and its answer
        question_para = Paragraph(f"<b>Question {question_number}:</b> {question_text}", style)
        answer_para = Paragraph(f"<b>Answer:</b> {answer_display}", style)

        # Append the question and answer to the PDF elements
        elements.append(question_para)
        elements.append(answer_para)
        elements.append(Paragraph("<br/><br/>", style))  # Add spacing between questions

    # Build the PDF with the accumulated elements
    doc.build(elements)
    
    buffer.seek(0)
    return buffer.getvalue()

def end_exam(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        try:
            user = get_object_or_404(UserForm, id=user_id)
            answer_record, created = Answer.objects.get_or_create(user=user)
            
            # Generate the PDF with answers
            answers = answer_record.answers  # This should be a dictionary
            pdf_content = generate_pdf(answers)
            # Save the PDF to the database
            if not answer_record.pdf_file:
                answer_record.pdf_file.save(f"answers_{user.name}_{user.registration_number}_{user_id}.pdf", ContentFile(pdf_content))
            
            # Return the PDF file as a response
            response = HttpResponse(pdf_content, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="answers.pdf"'
            
            return response

        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=400)

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        registration_number = request.POST.get('registrationNumber')

        # Save the data to the database
        user_form = UserForm(name=name, registration_number=registration_number)
        user_form.save()

        # Return the primary key of the saved instance
        print('lop')
        return JsonResponse({'success':True,'pk':user_form.pk})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=400)

def form(request):
    return render(request, 'form.html',{})
