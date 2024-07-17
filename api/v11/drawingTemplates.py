from django.http import HttpResponse
import json
import time
from datetime import datetime

from model import models
from api.v11 import common


def processRequest(request):
    parsedRequest = common.parseRequest(request)

    if parsedRequest['error'] is not None:
        return parsedRequest['error']

    if parsedRequest['response'] is not None:
        return parsedRequest['response']

    clientId = parsedRequest["clientId"]
    userId = parsedRequest['userId']
    name = request.GET.get('name', '')
    tool = request.GET.get('tool', '')

    if request.method == 'GET':
        if name == '':
            return getTemplates(clientId, userId, tool)
        else:
            return getTemplate(clientId, userId, tool, name)

    elif request.method == 'POST':
        content = request.POST.get('content', '')
        return createOrUpdateTemplate(clientId, userId, name, tool, content)

    elif request.method == 'DELETE':
        return removeTemplate(clientId, userId, tool, name)

    else:
        return common.error('Wrong request')


#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------


def getTemplates(clientId, userId, tool):
    items = models.DrawingTemplate.objects.defer('content').filter(ownerSource=clientId, ownerId=userId, tool=tool)
    result = map(lambda x: x.name, items)
    return common.response(json.dumps({'status': "ok", 'data': list(result)}))


def getTemplate(clientId, userId, tool, name):
    item = models.DrawingTemplate.objects.get(ownerSource=clientId, ownerId=userId, tool=tool, name=name)
    result = json.dumps({'status': 'ok', 'data': {'name': item.name, 'content': item.content}})
    return common.response(result)


def removeTemplate(clientId, userId, tool, name):
    item = models.DrawingTemplate.objects.get(ownerSource=clientId, ownerId=userId, tool=tool, name=name)
    item.delete()
    return common.response(json.dumps({'status': 'ok'}))


def createOrUpdateTemplate(clientId, userId, name, tool, content):
    if not content:
        return common.error('No content to save')

    if not name:
        return common.error('Name of template should not be empty')

    newItem, created = models.DrawingTemplate.objects.get_or_create(ownerSource=clientId, ownerId=userId, name=name, tool=tool)
    newItem.content = content
    newItem.save()
    return common.response(json.dumps({'status': 'ok'}))
