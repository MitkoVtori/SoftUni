from django.contrib import admin
from GameStats.Common.models import Problem, StaffNotes


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ("problem_type", "title", "creator")
    list_filter = ("problem_type", "date_reported")

    def get_form(self, request, obj=None, *args, **kwargs):
        form = super(ProblemAdmin, self).get_form(request, *args, **kwargs)
        form.base_fields['creator'].initial = request.user
        form.base_fields['creator'].disabled = True
        form.base_fields['creator'].readonly = True
        return form

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None and obj.creator != request.user.get_username():
            return False
        return True


@admin.register(StaffNotes)
class StaffNotesAdmin(admin.ModelAdmin):
    list_display = ("date", "id")
    list_filter = ("date", "id")
