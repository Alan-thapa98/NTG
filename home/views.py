
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
# from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.core.paginator import Paginator
# from blog.models import Blog
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
import datetime
from question_answer.models import which_subject_category,which_subject, which_type ,answer_question,  which_grade
from essay_and_bio.models import  essay_and_bio
from games.models import all_game_info
from django.urls import reverse_lazy
from profiles.models import Profile
from question_answer.forms import answer_questionForm
from essay_and_bio.forms import essay_and_bioForm
from django.views.generic import UpdateView, DeleteView
year = datetime.datetime.now().year
from django.contrib.auth.decorators import login_required

def home(request):
    # try:
        if  request.user.is_authenticated: 
            Clouds_tags =which_subject.objects.all()      
            new_answers = answer_question.objects.order_by('-views')[:10]
            all_games = all_game_info.objects.all()[:6]
            b_all_subjects = which_subject.objects.all()
            read_essays =essay_and_bio.objects.all()[:6]
            param = {"read_essays": read_essays, "new_answers": new_answers,
                    "Clouds_tags":Clouds_tags,"year": year, "all_games": all_games, 
                     "b_all_subjects": b_all_subjects}                      
        else:   
            new_answers = answer_question.objects.order_by('-views')[:10]
            all_games = all_game_info.objects.all()[:6]
            b_all_subjects = which_subject.objects.all()
            read_essays =essay_and_bio.objects.all()[:6]
            param = {"read_essays": read_essays, "new_answers": new_answers,
                    "year": year, "all_games": all_games, "b_all_subjects": b_all_subjects}
        return render(request, "home/home.html", param)
    # except Exception as e:
    #     return render(request, 'home/page_not_found.html')


#  classses and sunbjects categoarys
def all_class(request, class_name):
    try:
        all_class = which_grade.objects.filter(class_name=class_name).first()
        new_question = answer_question.objects.order_by('-timeStamp')[0:25]
        top_essays =essay_and_bio.objects.order_by('-timeStamp')[0:8]
        top_games = all_game_info.objects.order_by('-timeStamp')[0:4]

        param = {"new_question": new_question, "top_essays": top_essays, "top_games": top_games, "all_class": all_class, "b_all_sub_subjects": b_all_sub_subjects, "all_class": all_class,
                 "year": year}
        return render(request, 'home/all_class.html', param, )
    except Exception as e:
        return render(request, 'home/page_not_found.html')


def search_qanda(request):
    # try:
        Clouds_tags =which_subject.objects.all() 
        read_essays =essay_and_bio.objects.all()[:6]
        query = request.GET['query']
        author = answer_question.objects.filter(author__icontains=query)
        question = answer_question.objects.filter(question__icontains=query)
        answers = answer_question.objects.filter(content__icontains=query)
        tags = answer_question.objects.filter(tags__icontains=query)
        types = answer_question.objects.filter(types__icontains=query)
        grade = answer_question.objects.filter(grade__icontains=query)
        language = answer_question.objects.filter(language__icontains=query)
        subject = answer_question.objects.filter(subject__icontains=query)
        subject_category = answer_question.objects.filter(
            subject_category__icontains=query)
        search_all_qanda = author.union(
            question, answers, tags, types, grade, language, subject, subject_category)
        new_question = answer_question.objects.order_by('-timeStamp')[0:25]
        top_essays =essay_and_bio.objects.order_by('-timeStamp')[0:8]
        top_games = all_game_info.objects.order_by('-timeStamp')[0:4]

        suggestios_of_answer_question = answer_question.objects.order_by("-views")

        params = {"Clouds_tags":Clouds_tags,"read_essays":read_essays,"new_question": new_question, "top_essays": top_essays, "top_games": top_games, "query": query,
                  "search_all_qanda": search_all_qanda,
                  "all_class": all_class, "suggestios_of_answer_question": suggestios_of_answer_question,
                  "year": year}
        return render(request, "home/search_qanda.html", params)
    
    # except Exception as e:
    #     return render(request, 'home/page_not_found.html')

            # suggestios_of_answer_question =answer_question.objects.all()
            # suggestios_of_essays_and_bios = essay_and_bio.objects.all()
            
def search_essays(request):
#  try:
    suggestios_of_essays_and_bios = essay_and_bio.objects.order_by('-views')
    Clouds_tags =which_subject.objects.all() 
    read_essays =essay_and_bio.objects.all()[:6]
    query = request.GET['query']
    author =essay_and_bio.objects.filter(author__icontains=query)
    essays_name =essay_and_bio.objects.filter(essay_or_bio_name__icontains=query)
    essays_dec =essay_and_bio.objects.filter(content__icontains=query)
    types = essay_and_bio.objects.filter(types__icontains=query)
    language = essay_and_bio.objects.filter(language__icontains=query)   
    tags =essay_and_bio.objects.filter(tags__icontains=query)
    search_essays = essays_name.union(author, essays_dec,  tags, types,language)
    new_question = answer_question.objects.order_by('-timeStamp')[0:25]
    top_essays =essay_and_bio.objects.order_by('-timeStamp')[0:8]
    top_games = all_game_info.objects.order_by('-timeStamp')[0:4]
    a = "my name is Alan Thapa."
    params = {"a":a,"search_essays":search_essays, "new_question": new_question, "top_essays": top_essays, "top_games": top_games, "query": query, "read_essays": read_essays,
    "all_class": all_class, "suggestios_of_essays_and_bios":suggestios_of_essays_and_bios,"tags":tags, 
    "year": year,"Clouds_tags":Clouds_tags}
    return render(request, "home/search_essays.html", params)
    # except Exception as e:
    # return render(request, 'home/page_not_found.html')


def dictionary(request):
    try:
        new_answers = answer_question.objects.all()
        new_question = answer_question.objects.order_by('-timeStamp')[0:25]
        top_essays =essay_and_bio.objects.order_by('-timeStamp')[0:8]
        top_games = all_game_info.objects.order_by('-timeStamp')[0:4]

        params = {"new_question": new_question, "top_essays": top_essays, "top_games": top_games,  "new_answers": new_answers,
                  "year": year}
        return render(request, "home/dictionary.html", params)
    except Exception as e:
        return render(request, 'home/page_not_found.html')


def about(request):
    try:
        new_answers = answer_question.objects.all()
        # b_all_class = which_grade.objects.all()
        # b_all_subjects = which_subject.objects.all()
        # b_all_sub_subjects = which_subject_category.objects.all()
        params = {"new_answers": new_answers, "year": year}
        return render(request, "home/about.html", params)
    except Exception as e:
        return render(request, 'home/page_not_found.html')

def handeLogin(request):
    try:
        if request.method == "POST":
            # Get the post parameters
            loginusername = request.POST['loginusername']
            loginpassword = request.POST['loginpassword']

            user = authenticate(username=loginusername, password=loginpassword)
            if user is not None:
                login(request, user)
                messages.success(
                    request, f"Successfully Logged In  {{request.user}}")
                return redirect("home")
            else:
                messages.error(request, "Invalid credentials! Please try again")
                return redirect("home")

        return HttpResponse("404- Not found")
        return HttpResponse("login")
    except Exception as e:
        return render(request, 'home/page_not_found.html')
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')





def error_404(request, exception):
    return render(request, "home/error_404.html")


def aboutus(request):
    try:
        params ={"year": year}
        return render(request, 'aboutus.html',params)
    except Exception as e:
        return render(request, 'home/page_not_found.html')


def contactus(request):
    try:    
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            content = request.POST['content']
            all_contact = Contact(name=name, email=email,
                                phone=phone, content=content)
            all_contact.save()
            messages.success(request, "Your message has been successfully sent")
        return render(request, "home/contactus.html",{"year": year})
    except Exception as e:
        return render(request, 'home/page_not_found.html')

def policy_privacy(request):
    try:
        param = {"year": year}
        return render(request, 'home/policy_privacy.html', param)
    except Exception as e:
        return render(request, '/home/page_not_found.html',{"year": year})


def termsandcontions(request):
    try:
        param = {"year": year}
        return render(request, 'home/termsandcontions.html', param)
    except Exception as e:
        return render(request, '/home/page_not_found.html')
    
    






# def all_subjects(request, subject_name):
#     try:
#         all_subjects = which_subject.objects.filter(
#             subject_name=subject_name).first()
#         # b_all_class = which_grade.objects.all()
#         # b_all_subjects = which_subject.objects.all()
#         # b_all_sub_subjects = which_subject_category.objects.all()
#         new_answers = answer_question.objects.all()
#         query = str(subject_name)

#         all_question = answer_question.objects.filter(
#             question__icontains=query)
#         all_answer = answer_question.objects.filter(answer__icontains=query)
#         all_tags = answer_question.objects.filter(tags__icontains=query)
#         all_subject_name = answer_question.objects.filter(
#             subject_name__icontains=query)
#         all_subject_category = answer_question.objects.filter(
#             subject_category__icontains=query)
#         all_subject = all_question.union(
#             all_answer, all_tags,  all_subject_category, all_subject_name)

#         paginator = Paginator(all_subject, 2)
#         page_number = request.GET.get('page')
#         subject_list = paginator.get_page(page_number)

#         new_question = answer_question.objects.order_by('-timeStamp')[0:25]
#         top_essays =essay_and_bio.objects.order_by('-timeStamp')[0:8]
#         top_games = all_game_info.objects.order_by('-timeStamp')[0:4]

#         param = {"new_question": new_question, "new_answers": new_answers, "top_essays": top_essays, "top_games": top_games, 'all_subjects': all_subjects, "b_all_sub_subjects": b_all_sub_subjects, "all_class": all_class,

#                  "query": query, "all_subject": all_subject, "year": year, "subject_list": subject_list, }
#         return render(request, 'home/all_subjects.html', param)
#     except Exception as e:
#         return render(request, 'home/page_not_found.html')


# def subject_categorys(request, subject_category):
    # try:
    #     all_subjects = which_subject_category.objects.filter(
    #         subject_category=subject_category).first()
    #     query = str(subject_category)

    #     all_question = answer_question.objects.filter(
    #         question__icontains=query)
    #     all_answer = answer_question.objects.filter(answer__icontains=query)
    #     all_tags = answer_question.objects.filter(tags__icontains=query)
    #     all_subject_name = answer_question.objects.filter(
    #         subject_name__icontains=query)
    #     all_subject_category = answer_question.objects.filter(
    #         subject_category__icontains=query)
    #     all_subjects_cats = all_question.union(
    #         all_answer, all_tags,  all_subject_category)

    #     paginator = Paginator(all_subjects_cats, 2)
    #     page_number = request.GET.get('page')
    #     cats_list = paginator.get_page(page_number)
    #     new_answers = answer_question.objects.all()
    # b_all_class = which_grade.objects.all()
    # b_all_subjects = which_subject.objects.all()
    # b_all_sub_subjects = which_subject_category.objects.all()
    #     new_question = answer_question.objects.order_by('-timeStamp')[0:25]
    #     top_essays =essay_and_bio.objects.order_by('-timeStamp')[0:8]
    #     top_games = all_game_info.objects.order_by('-timeStamp')[0:4]

    #     param = {"all_subjects_cats": all_subjects_cats, "new_answers": new_answers, "new_question": new_question, "top_essays": top_essays, "top_games": top_games, 'all_subjects': all_subjects, "b_all_sub_subjects": b_all_sub_subjects, "all_class": all_class,
    #
    #              "query": query, "year": year, "cats_list": cats_list}
    #     return render(request, 'home/all_subject_category.html', param)
    # except Exception as e:
    # return render(request, 'home/page_not_found.html')
