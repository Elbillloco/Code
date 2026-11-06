from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from hello_api.entities.user import User
from hello_api.entities.animals import Animal
import json

# Create your views here.
def index(request):
    return JsonResponse({
        "message" : "Hello world"
    })

@csrf_exempt
def user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_user = User(
                id=data.get('id'),
                name=data.get('name'),
                account=data.get('account')
            )
            return JsonResponse({
                "message": "User created successfully",
                "user": {
                    "id": new_user.id,
                    "name": new_user.name,
                    "account": new_user.account
                }
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON body"}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def animals(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_animal = Animal(
                id=data.get('id'),
                name=data.get('name'),
                species=data.get('species')
            )
            return JsonResponse({
                "message": "Animal created successfully",
                "animal": {
                    "id": new_animal.id,
                    "name": new_animal.name,
                    "species": new_animal.species
                }
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON body"}, status=400)
    return JsonResponse({"error": "Method not allowed"}, status=405)
