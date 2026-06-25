
from functions.utils import log_event
import unittest

class MyTestCasePositive(unittest.TestCase):

    def setUp(self):
        with open("login_system.log", "w") as f:
            pass

    def test_log_event_success(self):
        test_user = "user1"
        test_status = "success"
        log_event(test_user, test_status)
        with open("login_system.log", "r") as f:
            file_content = f.read()
        self.assertIn(f"Login event - Username: {test_user}, Status: {test_status}", file_content)

    def test_log_event_expired(self):
        test_user = "user2"
        test_status = "expired"
        log_event(test_user, test_status)
        with open("login_system.log", "r") as f:
            file_content = f.read()
        self.assertIn(f"Login event - Username: {test_user}, Status: {test_status}", file_content)

    def test_log_event_failed(self):
        test_user = "user3"
        test_status = "failed"
        log_event(test_user, test_status)
        with open("login_system.log", "r") as f:
            file_content = f.read()
        self.assertIn(f"Login event - Username: {test_user}, Status: {test_status}", file_content)
