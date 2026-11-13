from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from hello_api.entities.user import User
from hello_api.entities.animals import Animal
from hello_api.storage import JsonStorageError, append_json_record
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
            if not isinstance(data, dict):
                return JsonResponse({"error": "JSON body must be an object"}, status=400)

            new_user = User(
                id=data.get('id'),
                name=data.get('name'),
                account=data.get('account')
            )
            user_data = {
                "id": new_user.id,
                "name": new_user.name,
                "account": new_user.account
            }
            append_json_record("users.json", user_data)
            return JsonResponse({
                "message": "User created successfully",
                "user": user_data
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON body"}, status=400)
        except JsonStorageError:
            return JsonResponse({"error": "Could not save user"}, status=500)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def animals(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if not isinstance(data, dict):
                return JsonResponse({"error": "JSON body must be an object"}, status=400)

            new_animal = Animal(
                id=data.get('id'),
                name=data.get('name'),
                species=data.get('species'),
                description=data.get('description')
            )
            animal_data = {
                "id": new_animal.id,
                "name": new_animal.name,
                "species": new_animal.species,
                "description": new_animal.description
            }
            append_json_record("animals.json", animal_data)
            return JsonResponse({
                "message": "Animal created successfully",
                "animal": animal_data
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON body"}, status=400)
        except JsonStorageError:
            return JsonResponse({"error": "Could not save animal"}, status=500)
    return JsonResponse({"error": "Method not allowed"}, status=405)
