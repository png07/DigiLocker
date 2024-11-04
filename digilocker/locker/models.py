import secrets
import os
from random import randint
from django.core.files.storage import default_storage
from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link documents to users
    file_name = models.CharField(max_length=255)
    file_extension = models.CharField(max_length=10)  # Store the file extension (e.g., .pdf, .txt)
    encrypted_file = models.FileField(upload_to='media/encrypted_documents/')  # Path to store encrypted files
    encryption_key = models.CharField(max_length=255)  # Store the encryption key in the database

    def __str__(self):
        return self.file_name

    def generate_key(self):
        """Generate a Fernet encryption key."""
        return Fernet.generate_key().decode()  # Generate a key and decode to string

    def encrypt_file(self, file):
        """Encrypt the uploaded file and save it."""
        key = self.generate_key()  # Generate a new key
        fernet = Fernet(key.encode())  # Create a Fernet instance with the key

        original = file.read()  # Read the file's original content
        encrypted = fernet.encrypt(original)  # Encrypt the original content

        # Save the encrypted file with dynamic path
        file_extension = os.path.splitext(file.name)[1]  # Extract the original file extension
        encrypted_file_path = default_storage.get_valid_name(f"encrypted_documents{randint(1,100000)}/{os.path.basename(file.name)}")
        with default_storage.open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        self.encrypted_file.name = encrypted_file_path  # Set the path for the encrypted file
        self.encryption_key = key  # Store the key as a string+63
        self.file_extension = file_extension  # Store the file extension
        self.save()  # Save the instance to the database

        return encrypted_file_path

    def decrypt_file(self):
        """Decrypt the file when downloading."""
        fernet = Fernet(self.encryption_key.encode())  # Create a Fernet instance with the stored key

        with default_storage.open(self.encrypted_file.path, 'rb') as file:
            encrypted_data = file.read()  # Read the encrypted file's content

        decrypted = fernet.decrypt(encrypted_data)  # Decrypt the content
        return decrypted  # Return decrypted content
