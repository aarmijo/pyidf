import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.plant import PlantEquipmentOperationUncontrolled

log = logging.getLogger(__name__)

class TestPlantEquipmentOperationUncontrolled(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_plantequipmentoperationuncontrolled(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PlantEquipmentOperationUncontrolled()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_equipment_list_name = "object-list|Equipment List Name"
        obj.equipment_list_name = var_equipment_list_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.plantequipmentoperationuncontrolleds[0].name, var_name)
        self.assertEqual(idf2.plantequipmentoperationuncontrolleds[0].equipment_list_name, var_equipment_list_name)