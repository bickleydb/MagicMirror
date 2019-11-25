from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from statements.shared.repositories.IStatementRepo import IStatementRepo
from statements.shared.repositories.StatementRepo import StatementRepo


class StatementView:

    def __init__(self):
        self.statementRepo = StatementRepo()

    def update_database(self, request):
        self.statementRepo.update_groups()
        return HttpResponse([])

    def get_random_value(self, request):
        value = self.statementRepo.get_random_val()
        returnValue = {
            "text": value.statement_text,
            "sourceName": value.statement_author
        }
        return HttpResponse(json.dumps(returnValue))

    def index(self, request):
        template = loader.get_template('statement/statements.html')
        return HttpResponse(template.render({
            "thread": StatementRepo().get_random_val()
        }, request))
