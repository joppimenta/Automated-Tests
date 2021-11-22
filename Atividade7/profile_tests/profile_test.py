import json
import unittest
import requests
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))

path_dir = os.path.join(current_dir, "features", "steps", "json_scenarios")
sys.path.append(path_dir)

from json_utils import *

class Profiles(unittest.TestCase):
    def setUp(self):
        self.url = get_url()

    def test_1_get_profiles(self):

        auth = get_token()
        header = {'authorization': auth}

        response = requests.get(f"{self.url}/profiles", headers=header)

        json_data = json.loads(response.text)

        item0 = json_data[0]

        self.assertIn('id', item0)
        self.assertEqual(type(item0['id']), int)


        self.assertIn('name', item0)
        self.assertEqual(type(item0['name']), str)

        self.assertIn('type', item0)
        self.assertEqual(type(item0['type']), str)


        item1 = json_data[1]

        self.assertIn('id', item1)
        self.assertEqual(type(item1['id']), int)

        self.assertIn('name', item1)
        self.assertEqual(type(item1['name']), str)

        self.assertIn('type', item1)
        self.assertEqual(type(item1['type']), str)

        item2 = json_data[2]

        self.assertIn('id', item2)
        self.assertEqual(type(item2['id']), int)

        self.assertIn('name', item2)
        self.assertEqual(type(item2['name']), str)

        self.assertIn('type', item2)
        self.assertEqual(type(item2['type']), str)

        item3 = json_data[3]

        self.assertIn('id', item3)
        self.assertEqual(type(item3['id']), int)

        self.assertIn('name', item3)
        self.assertEqual(type(item3['name']), str)

        self.assertIn('type', item3)
        self.assertEqual(type(item3['type']), str)

        print()