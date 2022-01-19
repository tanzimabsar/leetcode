import unittest
import logging, sys

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)

class TestProgram(unittest.TestCase):
    def setUp(self):
        logger.addHandler(stream_handler)

    def tearDown(self) -> None:
        logger.removeHandler(stream_handler)
        return super().tearDown()