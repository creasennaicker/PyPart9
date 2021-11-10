import unittest
import json_helper

EXPECTED = [{'name': 'Mario', 'neutral_special': 'Fireball', 'side_special': 'Cape', 'up_special': 'Super Jump Punch', 'down_special': 'F.L.U.D.D.', 'final_smash': 'Mario Finale'}, {'name': 'Link', 'neutral_special': 'Bow and Arrows', 'side_special': ' Boomerang', 'up_special': ' Spin Attack', 'down_special': 'Remote Bomb', 'final_smash': 'Ancient Bow and Arrow'}, {'name': 'Spider Man', 'actual name': 'Peter Parker', 'job': 'Destroying Villains'}, {'name': 'Cell', 'species': 'Bio-Android', 'Origins': 'Dr. Gero'}]

class Test_Json_Helper(unittest.TestCase):


    def test_json_helper_load(self):
        x = json_helper.read_all_json_files('data')
        json_helper.write_pickle('testout', x)
        actual = json_helper.load_pickle('testout')
        self.assertEqual(EXPECTED, actual)