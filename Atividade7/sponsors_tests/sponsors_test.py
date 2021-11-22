import json
import unittest
import requests
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "features", "steps", "json_scenarios")
sys.path.append(path_dir)

from json_utils import *

class Sponsors(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_sponsors(self):
         auth = get_token()
         header = {'authorization': auth}

         response = requests.get(f"{self.url}/sponsors", headers=header)

         json_data = json.loads(response.text)

         for data in json_data:
             self.assertIn('id', data)
             self.assertEqual(type(data['id']), int)

             self.assertIn('name', data)
             self.assertEqual(type(data['name']), str)

             self.assertIn('cnpj', data)
             self.assertEqual(type(data['cnpj']), str)

             self.assertIn('phone', data)
             self.assertEqual(type(data['phone']), str)

             self.assertIn('email', data)
             self.assertEqual(type(data['email']), str)

             self.assertIn('contactPerson', data)
             self.assertEqual(type(data['contactPerson']), str)

             self.assertIn('country', data)
             self.assertEqual(type(data['country']), dict)

             self.assertIn('state', data)
             self.assertEqual(type(data['state']), dict)

             #self.assertIn('description', data)
             #self.assertEqual(type(data['description']), str)

             #self.assertIn('logoPath', data)
             #self.assertEqual(type(data['logoPath']), str)

             self.assertIn('deleted', data)
             self.assertEqual(type(data['deleted']), bool)


         print()

