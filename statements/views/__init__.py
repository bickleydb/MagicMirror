from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json

import statements.shared.statement_db as statement_db

def updateDatabase(request): 
    dbRef = statement_db.statement_repository()
    dbRef.update_groups()
    return HttpResponse([])

def get_random_value(request):
    dbRef = statement_db.statement_repository()
    value = dbRef.get_random_val()

    returnValue = {
        "statement_text" : value.statement_text,
        "statement_author" : value.statement_author
    }

    return HttpResponse(json.dumps(returnValue))


def index(request):
    template = loader.get_template('reddit/index.html')
    return HttpResponse(template.render({
        "thread":statement_db.statement_repository().get_random_val()
    },request))