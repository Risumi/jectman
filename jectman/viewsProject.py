from .models import Project
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def Project(request):
    if request.method == 'GET':
        project = list(Project.objects.all().values())                
        output = {"data": project, "message": "Success","status": 200}
        return JsonResponse(output,safe=False)
    elif request.method == 'POST':        
        list_data = json.loads(request.body)        
        data = Project(id=list_data['id'],name=list_data['name'])
        data.save()
        output = {"message": "Success","status": 200}                
        return JsonResponse(output,safe=False)
    else:
        output = {"data": [], "message": "Method Not Allowed","status": 405}
        return JsonResponse(output,status=405)