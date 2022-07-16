from django.http import JsonResponse
from django.shortcuts import render
from .models import Todo, AppUser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
import json
from django.http import HttpResponse

@csrf_exempt
def log_in(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        email = body['email']
        password = body['password']
        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                try:
                    login(request, user)
                except Exception as e:
                    print('Error message below!')
                    print(str(e))
                return JsonResponse({'Status': 'Succesfully logged in'})    
            else:
                return HttpResponse('Account not active!')
        else:
            return HttpResponse('no user!')
    return render(request, 'pages/log_in.html')        

@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        try:        
            data = json.loads(request.body)
            print(data)
            AppUser.objects.create_user(username=data['email'], email=data['email'], password=data['password'])
        except Exception as e:
            print('Error message below!')
            print(str(e))
        return JsonResponse({'Status': 'Account created succesfully'})
    return render(request, 'pages/sign_up.html')

@csrf_exempt
def log_out(request):
    logout(request)
    return render(request, 'pages/index.html')

def get_details(id):
    single_todo_details = Todo.objects.get(id=id)
    return single_todo_details

def index(request):
    if request.method == 'POST':

        title = request.POST['title']
        description = request.POST['description']
        new_to_do = {'title': title, 'description': description}
        my_data = {'new_to_do': new_to_do}
        new_item = Todo(user = request.user, title = title, description = description)
        new_item.full_clean()
        new_item.save()
        return render(request, 'pages/view_to_do.html', my_data)
    if request.user.is_authenticated:
        user_id = request.user.id
        print('>>>>>>>>>>>>>>>>>>>>>>', request.user.email)
        database_list = Todo.objects.filter(user=user_id).values()
        print(database_list)
        my_db_data = {'database_list': database_list}
        return render(request, 'pages/index.html', my_db_data)
    else:
        return render(request, 'pages/index.html')

def to_do(request):
    return render(request, 'pages/to_do.html')

def view_details(request, id):
    details = get_details(id)
    my_data = {'details': details}
    return render(request, 'pages/view_details.html', my_data)

def edit_details(request, id):
    if request.method == 'POST':
        new_title = request.POST['title']
        new_description = request.POST['description']
        
        details = get_details(id)
        details.title = new_title
        details.save()
        details.description = new_description
        details.save()

        return render(request, 'pages/index.html')
    details = get_details(id)
    my_data = {'details': details}
    return render(request, 'pages/edit_details.html', my_data)

def delete(request, id):
    if request.method == 'POST':
        details = get_details(id)
        print(details)
        details.delete()
    return render(request, 'pages/index.html')
