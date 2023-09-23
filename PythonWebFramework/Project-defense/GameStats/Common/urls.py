from django.urls import path
from GameStats.Common import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('access/denied/', views.NoAccessView.as_view(), name="no-access"),
    path('problems/', views.ProblemsView.as_view(), name="problems"),
    path('problems/report-problem/', views.ReportProblemView.as_view(), name='report-problem'),
    path('problems/edit/<int:pk>/problem/', views.EditProblemView.as_view(), name='edit-problem'),
    path('problems/<int:pk>/report/problem/delete/', views.DeleteProblemView.as_view(), name="delete-problem"),
    path('staff/private/notes/', views.StaffView.as_view(), name='staff'),
    path('staff/private/add-note/', views.AddStaffNote.as_view(), name='staff-note'),
    path('staff/private/notes/edit/<int:pk>/note/', views.EditStaffNote.as_view(), name="edit-note"),
    path('staff/private/notes/delete/<int:pk>/note/', views.delete_staff_note_view, name="delete-note")
]