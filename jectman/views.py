from django.shortcuts import render
from .models import Project, Backlog
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def funcProject(request):
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
    elif request.method == 'DELETE':
        list_data = json.loads(request.body)        
        data = Project.objects.get(id=list_data['id'])
        data.delete()
        output = {"message": "Success","status": 200}    
        return JsonResponse(output,safe=False) 
    else:
        output = {"data": [], "message": "Method Not Allowed","status": 405}
        return JsonResponse(output,status=405)

@csrf_exempt
def funcBacklog(request,idProject):
    if request.method == 'GET':
        backlog = list(Backlog.objects.filter(id_project=idProject).values())                      
        output = {"data": backlog, "message": "Success","status": 200}
        return JsonResponse(output,safe=False)
    elif request.method == 'POST':        
        list_data = json.loads(request.body)        
        data = Backlog(id=list_data['id'],id_project_id=list_data['id_project_id'],name=list_data['name'],status=list_data['status'],begindate=list_data['begindate'],enddate=list_data['enddate'],description=list_data['description'])
        data.save()
        output = {"message": "Success","status": 200}                
        return JsonResponse(output,safe=False)    
    elif request.method == 'DELETE':
        list_data = json.loads(request.body)        
        data = Backlog.objects.get(id=list_data['id'])
        data.delete()
        output = {"message": "Success","status": 200}    
        return JsonResponse(output,safe=False) 
    else:
        output = {"data": [], "message": "Method Not Allowed","status": 405}
        return JsonResponse(output,status=405)

