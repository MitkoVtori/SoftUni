from django import forms
from GameStats.Common.models import Problem, StaffNotes


class ReportProblemForm(forms.ModelForm):
    video_image = forms.URLField(widget=forms.URLInput(attrs={
        "placeholder": "Please submit a link to a video and/or image that shows the problem, if you have one."
    }),
        required=False,
        label="URL")

    creator = forms.CharField(disabled=True)

    class Meta:
        model = Problem
        fields = "__all__"


class StaffNotesForm(forms.ModelForm):
    class Meta:
        model = StaffNotes
        fields = '__all__'


class DeleteStaffNoteForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label="Note", disabled=True)

    class Meta:
        model = StaffNotes
        fields = '__all__'
