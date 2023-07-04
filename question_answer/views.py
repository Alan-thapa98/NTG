from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import authenticate,  login, logout
from essay_and_bio.models import essay_and_bio
from .models import *
from django.db import IntegrityError
from django.core.paginator import Paginator
import datetime
from games.models import all_game_info
from django.urls import reverse_lazy
from profiles.models import Profile
from .forms import answer_questionForm
from django.views.generic import UpdateView, DeleteView
year = datetime.datetime.now().year
# questions answer section



def all_questions_answers(request):
    try:
            suggestios_of_answer_question = answer_question.objects.order_by("-views") 
            Clouds_tags =which_subject.objects.all() 
            read_essays =essay_and_bio.objects.all()[:6]  
            profile = Profile.objects.get(user=request.user)                    
            b_allanswer_question = answer_question.objects.all()
            b_all_class = which_grade.objects.all()
            b_all_subjects = which_subject.objects.all()
            b_all_sub_subjects = which_subject_category.objects.all()
            qanda = answer_question.objects.all()
            paginator = Paginator(b_allanswer_question, 40)
            page_number = request.GET.get('page')
            queston_list = paginator.get_page(page_number)
            new_question = answer_question.objects.order_by('-timeStamp')[0:40]
            top_essays = essay_and_bio.objects.order_by('-timeStamp')[0:8]
            top_games = all_game_info.objects.order_by('-timeStamp')[0:4]

            param = {"suggestios_of_answer_question":suggestios_of_answer_question,"Clouds_tags":Clouds_tags,"read_essays":read_essays,                'profile':profile,'qanda': qanda, "b_allanswer_question": b_allanswer_question,
                    "b_all_class": b_all_class, "b_all_sub_subjects": b_all_sub_subjects, "b_all_subjects": b_all_subjects, "queston_list": queston_list, "new_question": new_question, "top_essays": top_essays, "top_games": top_games ,"year": year }        
            return render(request, 'question_answer/all_questions_answers.html', param)
    except Exception as e:
        return render(request, 'home/page_not_found.html')


def read_all_questions_answers(request, slug):
    try:                
            Clouds_tags =which_subject.objects.all() 
            read_essays =essay_and_bio.objects.all()[:6]  
            profile = Profile.objects.get(user=request.user)
            quizs = answer_question.objects.filter(slug=slug).first()
            quizs.views = quizs.views + 1
            quizs.save()
            b_allanswer_question = answer_question.objects.all()
            b_all_class = which_grade.objects.all()
            b_all_subjects = which_subject.objects.all()
            b_all_sub_subjects = which_subject_category.objects.all()

            new_question = answer_question.objects.order_by('-timeStamp')[0:25]
            top_essays = essay_and_bio.objects.order_by('-timeStamp')[0:8]
            top_games = all_game_info.objects.order_by('-timeStamp')[0:4]

            params = {"profile":profile,'quizs': quizs, "b_all_sub_subjects": b_all_sub_subjects, "b_allanswer_question": b_allanswer_question, "b_all_class": b_all_class, "b_all_subjects": b_all_subjects,
            "new_question": new_question, "top_essays": top_essays, "top_games": top_games ,"year": year }
        
    
            params = {"Clouds_tags":Clouds_tags,"read_essays":read_essays,'quizs': quizs, "b_all_sub_subjects": b_all_sub_subjects, "b_allanswer_question": b_allanswer_question, "b_all_class": b_all_class, "b_all_subjects": b_all_subjects,
            "new_question": new_question, "top_essays": top_essays, "top_games": top_games ,"year": year }

            return render(request, 'question_answer/readqanda.html', params)
    except Exception as e:
        return render(request, 'home/page_not_found.html')


# upoad section
# Answer Questions, Different Between, Quiz, Technical term, Full Forms
@login_required
def upload_qanda_on_getanswr_9813587726(request):
    all_authors = which_author.objects.all()
    all_sujects = which_subject.objects.all()
    all_sub_subjects = which_subject_category.objects.all()
    all_category = which_type.objects.all()
    all_class = which_grade.objects.all()
    all_language = which_language.objects.all()
    # try:
    if request.method == "POST":
        # Get the post parameters
        user = Profile.objects.get(user=request.user)
        author = request.POST['author']
        question = request.POST['question']
        content = request.POST['content']
        tags = request.POST['tags']
        types = request.POST['types']
        grade = request.POST['grade']
        language = request.POST['language']
        subject = request.POST['subject']
        subject_category = request.POST['subject_category']
        qanda_model = answer_question(user=user,language=language, author=author, question=question, content=content, tags=tags,
          types=types, grade=grade, subject=subject, subject_category=subject_category)
        qanda_model.save()
        uploaded_question =answer_question.objects.order_by('-timeStamp')[0:1]
        print(uploaded_question)
        messages.success(
            request, ("Successfully uploaded!",uploaded_question))

    params = {"all_category": all_category, "all_language": all_language, "all_authors": all_authors, "all_sujects": all_sujects,
                  "all_sub_subjects": all_sub_subjects, "all_class": all_class ,"year": year}

    return render(request, 'question_answer/upload_qanda_on_getanswr.html', params)
    # except Exception as e:
    #     return render(request, 'home/page_not_found.html')


# Management section 
@login_required
def dashboard_ans(request):
    all_ans = answer_question.objects.all()
    profile = Profile.objects.get(user=request.user)
    param={"all_ans":all_ans,"profile":profile ,"year": year}
    return render(request, "question_answer/dashboard_ans.html",param)

class question_ansewr_UpdateView(LoginRequiredMixin, UpdateView ):
    form_class = answer_questionForm
    model = answer_question
    template_name = 'question_answer/update_ans.html'
    success_url = reverse_lazy('question_answer:dashboard_ans')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if form.instance.user == profile:
            return super().form_valid(form)
        else:
            form.add_error(None, "You need to be the author of the post in order to update it")
            return super().form_invalid(form)
   

@login_required
def delete_ans(request,slug):
    all_ans =answer_question.objects.get(slug=slug)  
    all_ans.delete()
    return redirect('question_answer:dashboard_ans')

