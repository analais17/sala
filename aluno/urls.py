from django.urls import path
from.import views

urlpatterns = [
    path('alunos/', views.aluno_list),
    path('aluno/create/', views.aluno_form),
    path('aluno/<int:aluno_id>/', views.aluno_show),
    path('excluir/<int:aluno_id>/' ,views.excluir_aluno),    
    path('editar/<int:aluno_id>/' ,views.editar_aluno)





]
