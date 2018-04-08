from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json

from statements.shared.repositories.IStatementRepo import IStatementRepo
from statements.shared.repositories.StatementRepo import StatementRepo

def updateDatabase(request): 
    statementRepo = StatementRepo()
    dbRef.update_groups()
    return HttpResponse([])

def get_random_value(request):
    dbRef = StatementRepo()
    value = dbRef.get_random_val()

    returnValue = {
        "text" : value.statement_text,
        "sourceName" : value.statement_author
    }

    return HttpResponse(json.dumps(returnValue))


def index(request):
    template = loader.get_template('statement/statements.html')
    return HttpResponse(template.render({
        "thread":StatementRepo().get_random_val()
    },request))