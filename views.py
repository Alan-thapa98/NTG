from django.shortcuts import render
import os
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import authenticate,  login, logout
from essay_and_bio.models import essay_and_bio

from question_answer.models import *
from django.db import IntegrityError
from django.core.paginator import Paginator
import datetime
from games.models import all_game_info
from django.urls import reverse_lazy
from profiles.models import Profile
from django.views.generic import UpdateView, DeleteView
from .forms import essay_and_bioForm
year = datetime.datetime.now().year



def all_essay_and_bio(request):
    try:
        suggestios_of_essays_and_bios = essay_and_bio.objects.order_by('-views')
        Clouds_tags =which_subject.objects.all() 
        read_essays =essay_and_bio.objects.all()[:6] 
        all_essay_and_bio = essay_and_bio.objects.all()
        new_question = answer_question.objects.order_by('-timeStamp')[0:25]
        top_essay_and_bio = essay_and_bio.objects.order_by('-timeStamp')[0:8]
        top_games = all_game_info.objects.order_by('-timeStamp')[0:4]

        paginator = Paginator(all_essay_and_bio, 15 )
        page_number = request.GET.get('page')
        eassay_list = paginator.get_page(page_number)
        param = {"Clouds_tags":Clouds_tags,"read_essays":read_essays,"suggestios_of_essays_and_bios":suggestios_of_essays_and_bios,"new_question": new_question, "top_essay_and_bio": top_essay_and_bio,
                 "top_games": top_games, 'all_essay_and_bio': all_essay_and_bio, 
                  "eassay_list": eassay_list ,"year": year}
        return render(request, 'essay_and_bio/all_essay_and_bio.html', param)
    except Exception as e:
        return render(request, 'home/page_not_found.html', param)


def read_essay_and_bio(request, slug):
    try:
        Clouds_tags =which_subject.objects.all() 
        read_essays =essay_and_bio.objects.all()[:6] 
        all_essay_and_bio = essay_and_bio.objects.filter(slug=slug).first()
        all_essay_and_bio.views = all_essay_and_bio.views + 1
        all_essay_and_bio.save() 
        new_question = answer_question.objects.order_by('-views')[0:11]
        top_essay_and_bio = essay_and_bio.objects.order_by('-views')[0:8]
        top_games = all_game_info.objects.order_by('-timeStamp')[0:4]
        param = {"Clouds_tags":Clouds_tags,"read_essays":read_essays,"new_question": new_question, "top_essay_and_bio": top_essay_and_bio, "top_games": top_games, 'all_essay_and_bio': all_essay_and_bio,
                "year": year }
        return render(request, 'essay_and_bio/read_essay_and_bio.html', param)
    except Exception as e:
        return render(request, 'home/page_not_found.html')

# New Pages of New Category - Anime, Biography 
# New Pages of New Category - Anime, Biography 
# New Pages of New Category - Anime, Biography 





# ---------------------------------------------------------------------------------------------------------- 
# ----------------------------------- Management section----------------------------------------------------- 
# ---------------------------------------------------------------------------------------------------------- 

@login_required
def upload_essay_and_bio_on_getanswr_9813587726(request):
    all_authors = which_author.objects.all()
    all_sujects = which_subject.objects.all()
    all_sub_subjects = which_subject_category.objects.all()
    all_class = which_grade.objects.all()
    all_language = which_language.objects.all()
    all_category = which_type.objects.all()
#     try:
    if request.method == "POST":
        user = Profile.objects.get(user=request.user)
        author = request.POST['author']
        essay_or_bio_name = request.POST['essay_or_bio_name']
        essay_or_bio_image = request.FILES['essay_or_bio_image']
        content = request.POST['content']
        tags = request.POST['tags']
        types = request.POST['types']
        language = request.POST['language']
        essay_and_bio_model = essay_and_bio(author=author, essay_or_bio_name=essay_or_bio_name, essay_or_bio_image=essay_or_bio_image, content=content, tags=tags, types=types,
     user=user, language=language)
        essay_and_bio_model.save()
        messages.success(
    request, "Successfully ! uploaded your data in Answrs.com thank-you for your cooperation")

    params = {"all_category": all_category, "all_language": all_language, "all_authors": all_authors, "all_sujects": all_sujects,
      "all_sub_subjects": all_sub_subjects, "all_class": all_class}
    return render(request, 'essay_and_bio/upload_essays_on_getanswr.html', params)
#     except Exception as e:
#     return render(request, 'home/page_not_found.html')


@login_required # not copletated yet!!!
def dashboard_essay(request):
    try:              
              all_essay_and_bio =essay_and_bio.objects.all()
              param={"all_essay_and_bio":all_essay_and_bio}
              return render(request, "essay_and_bio/dashboard_essay.html",param)
    except Exception as e:
        return render(request, 'home/page_not_found.html')    


class essay_UpdateView(LoginRequiredMixin, UpdateView):
    form_class = essay_and_bioForm
    model = essay_and_bio
    template_name = 'essay_and_bio/update_essays.html'
    success_url = reverse_lazy('essay_and_bio:dashboard_essay')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        print(profile)
        if form.instance.user == profile:
            return super().form_valid(form)
        else:
            form.add_error(None, "You need to be the author of the post in order to update it")
            return super().form_invalid(form)

@login_required            
def delete_essays(request,slug):  
    all_essays_and_bio =essay_and_bio.objects.get(slug=slug)  
    if len(all_essays_and_bio.essay_or_bio_image)>0:
        os.remove(all_essays_and_bio.essay_or_bio_image.path)
    all_essays_and_bio.delete()
    messages.success(
    request, "Successfully ! Deleted your data from getanswer.com thank-you for your cooperation")
    return redirect('essay_and_bio:dashboard_essay')
