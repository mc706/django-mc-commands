import unittest
import shutil
import os

from mc_commands.management.commands.helpers._update_changelog import generate_assets
from mc_commands.management.commands.helpers._generate_debugger import generate_debugger


class GenerateDebuggerTest(unittest.TestCase):
    def setUp(self):
        self.BASE_DIR = os.path.dirname(__file__)
        if os.path.exists(os.path.join(self.BASE_DIR, 'assets')):
            shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))
        generate_assets(self.BASE_DIR, 'test-app')

    def test_debugger(self):
        generate_debugger(self.BASE_DIR, 'Password1')
        self.assertTrue(os.path.exists(os.path.join(self.BASE_DIR, 'assets', 'app', 'config', 'logger.js')))
        self.assertTrue(os.path.exists(os.path.join(self.BASE_DIR, 'docs', 'logging.md')))

    def tearDown(self):
        shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))

