from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import InputTask
from django.urls import reverse
from .models import Task
from django.views import generic


def index(request):
    context = {}
    form = InputTask(request.POST or None)
    context['form'] = form
    # # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = InputTask(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         return HttpResponseRedirect('')
    # else:
    #     form = InputTask()
    return render(request, 'index.html', context)

def list(request):
    list = {}
    print(request.POST)
    message = request.POST.get('message', 'task')
    list['message'] = message
    return render(request, 'HVACtodo/list.html', list)

def status(request):
    form = InputTask(request.POST)
    return render(request, 'HVACtodo/status.html', {'form' : form})
    



# def index(request):
#     form = InputTask(request)
#     task_list = Task.objects
#     context_dict = {'tasks' : task_list}
#     l1 = context_dict.items()
#     l2 = list(l1)
#     return render('HVACtodo/index.html', l2, form)

# class IndexView(generic.ListView):
#     model = Task
#     template_name = 'HVACtodo/index.html'

#     def get_queryset(self):
#         return Task.objects.all()