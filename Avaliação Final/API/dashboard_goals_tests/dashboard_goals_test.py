import json
import unittest
import requests
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "features", "steps", "json_scenarios")
sys.path.append(path_dir)

from json_utils import *

class Goals(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_dashboard_goals(self):
        company_id = get_company_id()

        token = get_token()
        header = {'authorization': token}

        response = requests.get(f'{self.url}/dashboard/goals/{company_id}', headers=header)

        assert response.status_code == 200

        json_data = json.loads(response.text)

        self.assertIn('breakevenPoint', json_data)
        self.assertEqual(type(json_data['breakevenPoint']), float)

        self.assertIn('salesGoal', json_data)
        self.assertEqual(type(json_data['salesGoal']), float)

        self.assertIn('totalTaxForSale', json_data)
        self.assertEqual(type(json_data['totalTaxForSale']), float)

        self.assertIn('unitBP', json_data)
        self.assertEqual(type(json_data['unitBP']), float)

        self.assertIn('unitSG', json_data)
        self.assertEqual(type(json_data['unitSG']), float)

        print()