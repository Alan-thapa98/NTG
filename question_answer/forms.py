from django import forms
from .models import answer_question

class answer_questionForm (forms.ModelForm):
    answer = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    tags = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        model= answer_question
        fields =  ('author','question','content','tags','types','grade','language','subject_category')
