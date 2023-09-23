from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from GameStats.Common.forms import ReportProblemForm, StaffNotesForm, DeleteStaffNoteForm
from GameStats.Common.models import Problem, StaffNotes


class HomePageView(TemplateView):
    template_name = "Common/home-page.html"


class NoAccessView(TemplateView):
    template_name = 'no_access.html'


class ReportProblemView(LoginRequiredMixin, CreateView):
    template_name = "Common/report-problem.html"
    form_class = ReportProblemForm
    success_url = reverse_lazy("problems")

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['creator'].initial = self.request.user.get_username()
        return form


class ProblemsView(LoginRequiredMixin, ListView):
    context_object_name = "problems"
    model = Problem
    template_name = "Common/problems.html"


class EditProblemView(LoginRequiredMixin, UpdateView):
    template_name = "Common/edit-problem.html"
    form_class = ReportProblemForm
    model = Problem
    context_object_name = "problem"
    success_url = reverse_lazy("problems")

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['creator'].initial = self.request.user.get_username()
        return form


class DeleteProblemView(LoginRequiredMixin, DeleteView):
    template_name = "Common/delete-problem.html"
    model = Problem
    context_object_name = "problem"
    success_url = reverse_lazy("problems")


class StaffView(LoginRequiredMixin, ListView):
    template_name = "Common/staff.html"
    model = StaffNotes
    context_object_name = "notes"


class AddStaffNote(LoginRequiredMixin, CreateView):
    template_name = "Common/staff-note.html"
    form_class = StaffNotesForm
    success_url = reverse_lazy("staff")

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_staff and not self.request.user.is_superuser:
            return redirect("no-access")
        return super().get(request, *args, **kwargs)


class EditStaffNote(LoginRequiredMixin, UpdateView):
    template_name = "Common/edit-note.html"
    form_class = StaffNotesForm
    model = StaffNotes
    context_object_name = "note"
    success_url = reverse_lazy("staff")

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_staff and not self.request.user.is_superuser:
            return redirect("no-access")
        return super().get(request, *args, **kwargs)


@login_required
def delete_staff_note_view(request, pk):
    note = StaffNotes.objects.get(pk=pk)

    if not request.user.is_staff and not request.user.is_superuser:
        return redirect("no-access")

    if request.method == "POST":
        note.delete()
        return redirect("staff")

    form = DeleteStaffNoteForm(instance=note)
    return render(request, "Common/delete-note.html", {"form": form, "note": note})
