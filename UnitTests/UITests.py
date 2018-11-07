from unittest import TestCase
from UI import UI
from TextFileInterface import TextFileInterface
from Environment import Environment


class CommandTests(TestCase):
    def setUp(self):
        tfi = TextFileInterface(relative_directory="TestDB/")
        self.environment = Environment(tfi)
        self.environment.database.clear_database()

    def test_parse_commands(self):
        self.assertTrue(self.environment.parse_commands("command1 command2 command3"),
                        {"command1", "command2", "command2"})

    def test_command(self):
        self.assertEquals(self.environment.command("invalid_arg arg arg arg"), "Invalid Command")
