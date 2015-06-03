from django.contrib import auth
from django.core import serializers
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Context, loader, RequestContext

from forms import RegistrationForm
from models import *
from datetime import datetime

# The Intro Page
def home(request):
    return render(request, 'task/home.html')

def groupView(request):
    if request.user.is_authenticated():
        userID = request.user.id
        user = User.objects.get(id=userID)
        tasks = Task.objects.filter(user=user).order_by('-startDateTime')
        pTasks = []
        wTasks = []
        sTasks = []
        Tasks = []
        count = 0.0
        doneTasks = 0.0
        for task in tasks:
            Tasks.append(task)
            count += 1
            if (task.done == True):
                doneTasks += 1
            if (task.taskType == 'Personal'):
                pTasks.append(task)
            elif(task.taskType == 'Work'):
                wTasks.append(task)
            elif(task.taskType == 'School'):
                sTasks.append(task)
        if (count == 0):
            taskPerc = 0
        else:
            taskPerc = int(doneTasks/count*100)
        context = {'taskPerc':taskPerc, 'count':count, 'doneTasks':doneTasks, 'Tasks':Tasks, 
        'pTasks':pTasks, 'wTasks':wTasks, 'sTasks':sTasks}
        return render(request, 'task/groupview.html', context)
    else:
        return HttpResponseRedirect('/accounts/login')

def detailView(request):
    if request.user.is_authenticated():
        userID = request.user.id
        user = User.objects.get(id=userID)


def addTask(request):
    if request.method == 'POST':
        if request.POST['method'] == 'add':
            taskName = request.POST['taskName']
            taskType = request.POST.get('taskType', '')
            description = request.POST['description']
            location = request.POST['location']
            startDateTime = request.POST['startDateTime']
            endDateTime = request.POST['endDateTime']
            done = request.POST['done']
            userID = request.user.id
            user = User.objects.get(id = userID)
            task = Task(taskName = taskName, taskType = taskType, description = description,
                location = location, startDateTime = startDateTime, endDateTime = endDateTime,
                done = done, user = user)
            task.save()
            return HttpResponseRedirect('/groupview')
    return HttpResponseRedirect('/groupview/add')

def editTask(request):
    if request.method == 'POST':
        if request.POST['method'] == 'edit':
            taskID = request.POST['taskID']
            target = Task.objects.get(taskID = taskID)
            target.taskName = request.POST['taskName']
            target.taskType = request.POST['taskType']
            target.description = request.POST['description']
            target.location = request.POST['location']
            target.startDateTime = request.POST['startDateTime']
            target.endDateTime = request.POST['endDateTime']
            target.done = request.POST['done']
            target.save()
            return HttpResponseRedirect('/groupview')
    return HttpResponseRedirect('/groupview')

def deleteTask(request):
    if request.method == 'DELETE':
        task = Task.objects.get(taskID=int(QueryDict(request.body).get('postpk')))
        task.delete()
        response_data = {}
        response_data['msg'] = 'Task is successfully deleted.'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
    # if request.method == 'POST':
    #     if request.POST['method'] == 'delete':
    #         taskID = request.POST['taskID']
    #         target = Task.objects.get(taskID = taskID)
    #         target.delete()
    #         return HttpResponseRedirect('/groupview')
    # return HttpResponseRedirect('/groupview')

def test(request):
    user = User.objects.get(id=1)
    print user.username
    for i in range(1,5):
        pTask = Task(taskName="Personal{0}".format(i), taskType="Personal", description="desc{0}".format(i),
            location="location", startDateTime=datetime.now(), endDateTime=datetime.now(),
            done=True, user=user)
        wTask = Task(taskName="Work{0}".format(i), taskType="Work", description="desc{0}".format(i),
            location="location", startDateTime=datetime.now(), endDateTime=datetime.now(),
            done=False, user=user)
        sTask = Task(taskName="School{0}".format(i), taskType="School", description="desc{0}".format(i),
            location="location", startDateTime=datetime.now(), endDateTime=datetime.now(),
            done=True, user=user)
        pTask.save()
        wTask.save()
        sTask.save()
    return HttpResponseRedirect('/')    


############################
# Login and Register
############################

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('task/account/login.html', c)

def auth_view(request):
    # GET username or if there is no valid data, return ''.
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid_login')

def loggedin(request):
    c = {}
    c.update(csrf(request))
    c['username'] = request.user.username
    test = request.POST.get('title', '')
    return HttpResponseRedirect('/groupview')

def invalid_login(request):
    return render_to_response('task/account/invalid_login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
    # return render_to_response('task/account/logout.html')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        else:
            return render_to_response('task/account/register.html', {'form': form})
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    return render(request, 'task/account/register.html', args)

def register_success(request):
    return render_to_response('task/account/register_success.html')