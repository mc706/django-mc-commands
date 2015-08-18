import unittest
import shutil
import os

from mc_commands.management.commands.helpers._update_changelog import generate_assets
from mc_commands.management.commands.helpers._generate_limiter import generate_limiter


class GenerateLimiterTest(unittest.TestCase):
    def setUp(self):
        self.BASE_DIR = os.path.dirname(__file__)
        if os.path.exists(os.path.join(self.BASE_DIR, 'assets')):
            shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))
        generate_assets(self.BASE_DIR, 'test-app')

    def test_debugger(self):
        generate_limiter(self.BASE_DIR)
        self.assertTrue(os.path.exists(os.path.join(self.BASE_DIR, 'assets', 'app', 'config', 'limiter.js')))
        self.assertTrue(os.path.exists(os.path.join(self.BASE_DIR, 'docs', 'limiter.md')))

    def tearDown(self):
        shutil.rmtree(os.path.join(self.BASE_DIR, 'assets'))

