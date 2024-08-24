from django.db.models import F
from django.http import HttpResponseRedirect
from django.views import generic
from django.shortcuts import render , get_object_or_404 , redirect
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import CreateChoiceForm , CreateQuestionForm
from .models import Choice , Question

class IndexView(generic.ListView):
    template_name="index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Son yayınlanan 5 soruyu göster."""
        return Question.objects.order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "detail.html"


class ResultsView(generic.DetailView):
    model=Question
    template_name = "results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

@login_required
def create_view(request):
    if request.method == "POST":
        question_form = CreateQuestionForm(request.POST)

        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.pub_date = timezone.now() 
            question.published_user = request.user
            question.save()
            messages.success(request,"Your poll created successfully")
            return redirect(to="polls:index")
        
    else:
        question_form = CreateQuestionForm()

    
    return render(request , "create_poll.html" , {'question_form' : question_form})

@login_required
def create_choice_view(request,question_id):
    question = get_object_or_404(Question , id = question_id)
    if request.method == "POST":
        choice_form = CreateChoiceForm(request.POST)

        if choice_form.is_valid():
            choice = choice_form.save(commit=False)
            choice.question=question
            choice.save()
            messages.success(request,"Your poll created successfully")
            return redirect(to="polls:index")
        
    else:
        choice_form = CreateChoiceForm()

    
    return render(request , "create_choice.html" , {'choice_form' : choice_form})



def delete_poll(request , question_id):
    question = get_object_or_404(Question , id = question_id)
    question.delete()

    return redirect(to="polls:index")