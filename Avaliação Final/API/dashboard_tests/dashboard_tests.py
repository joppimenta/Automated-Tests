import json
import unittest
import requests
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "steps", "json_scenarios")
sys.path.append(path_dir)

from json_utils import *

class Companies(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_companies(self):
        auth = get_token()
        header = {'authorization': auth}

        response = requests.get(f"{self.url}/companies", headers=header)

        json_data = json.loads(response.text)
        print()
