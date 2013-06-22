from django.db import models


class StateManager(models.Manager):
    def get_states(self):
        for state in self.all():
            yield state.code, state.name