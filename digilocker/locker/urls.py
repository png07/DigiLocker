from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),
    path('upload/', views.upload_document, name='upload_document'),
    path('documents/', views.view_documents, name='view_documents'),
    path('documents/download/<int:document_id>/', views.download_document, name='download_document'),
    path('documents/delete/<int:document_id>/', views.delete_document, name='delete_document'),
    path('aboutus/', views.aboutus, name='aboutus'),
]
