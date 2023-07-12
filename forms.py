from django import forms
from essay_and_bio.models import essay_and_bio

      
class essay_and_bioForm (forms.ModelForm):
    essay_dec = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    tags = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    class Meta:
        model= essay_and_bio
        fields = ('author','essay_or_bio_name','essay_or_bio_image','content','tags','types','language')


