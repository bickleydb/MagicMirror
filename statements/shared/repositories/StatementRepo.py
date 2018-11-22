import random
from datetime import datetime, timedelta
from statements.models.TextStatementModel import TextStatementModel
from statements.models.TextStatementSourceModel import TextSatementSourceModel


from statements.shared.reddit_adapter.SubredditRequest import SubredditRequest
from statements.shared.twitter_adapter import twitter_request

from . import IStatementRepo

class StatementRepo(IStatementRepo.IStatementRepo):

    def get_lookback_time(self):
        return datetime.now() - timedelta(days=2)

    def get_all_groups(self):
        group_manager = TextSatementSourceModel.get_manager()
        return group_manager.all()

    def delete_existing_statements(self, groups_to_delete):
        statement_manager = TextStatementModel.get_manager()
        for group in groups_to_delete:
            statement_set = statement_manager.all().filter(statement_source=group)
            for statement in statement_set:
                statement.delete() 

    def delete_existing_groups(self, group_list):
        for group in group_list:
            group.delete()
   
    def get_random_val(self):
        statement_manager = TextStatementModel.get_manager()
        statements = list(statement_manager.all())
        return random.choice(statements)


    def get_all_groups_to_update(self):
        time = self.get_lookback_time()
        return self.get_all_groups().filter(last_update_date_time__lt=time)

    def update_groups(self):
        groups_to_update = self.get_all_groups_to_update()
        self.delete_existing_statements(groups_to_update)
        for group in groups_to_update:
            if group.source_site == TextSatementSourceModel.REDDIT:
                request_data = SubredditRequest(
                    subreddit=group.source_name
                ).get_data()
                for request in request_data:
                    self.save_request(request)
            if group.source_site == TextSatementSourceModel.TWITTER:
                request_data = twitter_request.twitter_request(
                    twitter_id=group.source_name
                ).get_data()
                for request in request_data:
                    self.save_request(request)

    def save_request(self, responseValue):
        statement_source = self.get_source(responseValue.get_site(), responseValue.get_source())
        new_statement = TextStatementModel(
            statement_text=responseValue.get_text(),
            statement_author=responseValue.get_author(),
            statement_source=statement_source
        )
        new_statement.save()

    def get_source(self, source_type, source_name):
        source_manager = TextSatementSourceModel.get_manager()
        print(source_type + ";     " + source_type)
        source_inst, _ = source_manager.get_or_create(
            source_name=source_name,
            source_site=source_type,
            defaults={
                "last_update_date_time" : datetime.now()
            }
        )
        return source_inst