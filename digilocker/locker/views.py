from django.core.files.storage import default_storage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError

from .forms import UserSignupForm
from .models import Document
from django.http import HttpResponse

def aboutus(request):
    return render(request, 'about.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    documents = Document.objects.filter(user=request.user)  # Fetch documents for the logged-in user
    return render(request, 'home.html', {'documents': documents})

@login_required
def upload_document(request):
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['document']  # Access the uploaded file
        except MultiValueDictKeyError:
            return render(request, 'upload.html', {'error': 'No document uploaded'})

        document = Document(user=request.user)  # Create a new Document instance
        document.file_name = request.POST['file_name']  # Get the file name from the form
        encrypted_file_path = document.encrypt_file(uploaded_file)  # Encrypt the uploaded file
        document.encrypted_file = encrypted_file_path  # Save the encrypted file path
        document.save()  # Save the Document instance
        return redirect('home')  # Redirect to the home page

    return render(request, 'upload.html')

@login_required
def view_documents(request):
    documents = Document.objects.filter(user=request.user)  # Fetch user's documents
    return render(request, 'document_list.html', {'documents': documents})

@login_required
def download_document(request, document_id):
    # Retrieve the document object based on the provided document_id
    document = get_object_or_404(Document, id=document_id)

    # Decrypt the file
    decrypted_content = document.decrypt_file()

    # Create an HTTP response with the decrypted content
    response = HttpResponse(decrypted_content, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename={document.file_name}{document.file_extension}'
    return response

@login_required
def delete_document(request, document_id):
    # Retrieve the document object based on the provided document_id
    document = get_object_or_404(Document, id=document_id, user=request.user)

    # Delete the encrypted file from the media folder
    if document.encrypted_file:
        default_storage.delete(document.encrypted_file.path)

    # Delete the document instance from the database
    document.delete()

    return redirect('view_documents')  # Redirect back to the documents list