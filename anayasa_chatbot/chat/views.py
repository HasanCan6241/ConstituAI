# chat/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import uuid
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import Conversation, Message, Feedback
from .forms import ChatForm, FeedbackForm
from .chatbot import AnayasaChatBot


def home(request):
    return render(request, 'chat/home.html')


def about(request):
    return render(request, 'chat/about.html')

@login_required
def chat(request):
    # Session ID oluştur veya al
    if 'session_id' not in request.session:
        request.session['session_id'] = str(uuid.uuid4())

    session_id = request.session['session_id']

    # Kullanıcı oturum açtıysa onunla ilişkilendir, yoksa sadece session id ile kaydet
    if request.user.is_authenticated:
        conversation, created = Conversation.objects.get_or_create(
            user=request.user,
            session_id=session_id
        )
    else:
        conversation, created = Conversation.objects.get_or_create(
            session_id=session_id
        )

    # Konuşma geçmişini al
    messages = conversation.messages.all()

    form = ChatForm()

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']

            # Kullanıcı mesajını kaydet
            Message.objects.create(
                conversation=conversation,
                sender='user',
                content=user_message
            )

            # Chatbot yanıtını al
            bot_response = AnayasaChatBot.get_response(user_message)

            # Bot mesajını kaydet
            bot_message = Message.objects.create(
                conversation=conversation,
                sender='bot',
                content=bot_response
            )

            # AJAX isteği ise JSON yanıt döndür
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'message': bot_response,
                    'message_id': bot_message.id
                })

            return redirect('chat')

    context = {
        'messages': messages,
        'form': form,
    }

    return render(request, 'chat/chat.html', context)


@csrf_exempt  # AJAX için
@require_POST
def submit_feedback(request):
    message_id = request.POST.get('message_id')
    rating = request.POST.get('rating')
    comment = request.POST.get('comment', '')

    try:
        message = Message.objects.get(id=message_id)
        Feedback.objects.create(
            message=message,
            rating=rating,
            comment=comment
        )
        return JsonResponse({'status': 'success'})
    except Message.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Mesaj bulunamadı'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


@login_required
def history(request):
    conversations = Conversation.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'chat/history.html', {'conversations': conversations})


@login_required
def conversation_detail(request, conversation_id):
    try:
        conversation = Conversation.objects.get(id=conversation_id, user=request.user)
        messages = conversation.messages.all()
        return render(request, 'chat/conversation_detail.html', {
            'conversation': conversation,
            'messages': messages
        })
    except Conversation.DoesNotExist:
        return redirect('history')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Profil yerine chat sayfasına yönlendir
            return redirect('chat')
        else:
            # Hatalı giriş
            return render(request, 'chat/login.html', {'form': {'errors': True}})
    return render(request, 'chat/login.html')

# chat/views.py dosyasına ekleyin
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Kullanıcıyı doğrudan giriş yaptır
            return redirect('chat')
    else:
        form = CustomUserCreationForm()
    return render(request, 'chat/register.html', {'form': form})