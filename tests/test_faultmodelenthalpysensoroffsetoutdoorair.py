import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.operational_faults import FaultModelEnthalpySensorOffsetOutdoorAir

log = logging.getLogger(__name__)

class TestFaultModelEnthalpySensorOffsetOutdoorAir(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_faultmodelenthalpysensoroffsetoutdoorair(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FaultModelEnthalpySensorOffsetOutdoorAir()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_severity_schedule_name = "object-list|Severity Schedule Name"
        obj.severity_schedule_name = var_severity_schedule_name
        # alpha
        var_controller_object_type = "Controller:OutdoorAir"
        obj.controller_object_type = var_controller_object_type
        # object-list
        var_controller_object_name = "object-list|Controller Object Name"
        obj.controller_object_name = var_controller_object_name
        # real
        var_enthalpy_sensor_offset = 0.0
        obj.enthalpy_sensor_offset = var_enthalpy_sensor_offset

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.faultmodelenthalpysensoroffsetoutdoorairs[0].name, var_name)
        self.assertEqual(idf2.faultmodelenthalpysensoroffsetoutdoorairs[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.faultmodelenthalpysensoroffsetoutdoorairs[0].severity_schedule_name, var_severity_schedule_name)
        self.assertEqual(idf2.faultmodelenthalpysensoroffsetoutdoorairs[0].controller_object_type, var_controller_object_type)
        self.assertEqual(idf2.faultmodelenthalpysensoroffsetoutdoorairs[0].controller_object_name, var_controller_object_name)
        self.assertAlmostEqual(idf2.faultmodelenthalpysensoroffsetoutdoorairs[0].enthalpy_sensor_offset, var_enthalpy_sensor_offset)