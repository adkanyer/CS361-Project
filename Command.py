import abc


class Command(abc.ABC):

    @abc.abstractmethod
    def action(self, args, user):
        pass
