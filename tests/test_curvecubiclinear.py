import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.performance_curves import CurveCubicLinear

log = logging.getLogger(__name__)

class TestCurveCubicLinear(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_curvecubiclinear(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CurveCubicLinear()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_coefficient1_constant = 2.2
        obj.coefficient1_constant = var_coefficient1_constant
        # real
        var_coefficient2_x = 3.3
        obj.coefficient2_x = var_coefficient2_x
        # real
        var_coefficient3_x2 = 4.4
        obj.coefficient3_x2 = var_coefficient3_x2
        # real
        var_coefficient4_x3 = 5.5
        obj.coefficient4_x3 = var_coefficient4_x3
        # real
        var_coefficient5_y = 6.6
        obj.coefficient5_y = var_coefficient5_y
        # real
        var_coefficient6_xy = 7.7
        obj.coefficient6_xy = var_coefficient6_xy
        # real
        var_minimum_value_of_x = 8.8
        obj.minimum_value_of_x = var_minimum_value_of_x
        # real
        var_maximum_value_of_x = 9.9
        obj.maximum_value_of_x = var_maximum_value_of_x
        # real
        var_minimum_value_of_y = 10.1
        obj.minimum_value_of_y = var_minimum_value_of_y
        # real
        var_maximum_value_of_y = 11.11
        obj.maximum_value_of_y = var_maximum_value_of_y
        # real
        var_minimum_curve_output = 12.12
        obj.minimum_curve_output = var_minimum_curve_output
        # real
        var_maximum_curve_output = 13.13
        obj.maximum_curve_output = var_maximum_curve_output
        # alpha
        var_input_unit_type_for_x = "Dimensionless"
        obj.input_unit_type_for_x = var_input_unit_type_for_x
        # alpha
        var_input_unit_type_for_y = "Dimensionless"
        obj.input_unit_type_for_y = var_input_unit_type_for_y
        # alpha
        var_output_unit_type = "Dimensionless"
        obj.output_unit_type = var_output_unit_type

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.curvecubiclinears[0].name, var_name)
        self.assertAlmostEqual(idf2.curvecubiclinears[0].coefficient1_constant, var_coefficient1_constant)
        self.assertAlmostEqual(idf2.curvecubiclinears[0].coefficient2_x, var_coefficient2_x)
        self.assertAlmostEqual(idf2.curvecubiclinears[0].coefficient3_x2, var_coefficient3_x2)
        self.assertAlmostEqual(idf2.curvecubiclinears[0].coefficient4_x3, var_coefficient4_x3)
        self.assertAlmostEqual(idf2.curvecubiclinears[0].coefficient5_y, var_coefficient5_y)
        self.assertAlmostEqual(idf2.curvecubiclinears[0].coefficient6_xy, var_coefficient6_xy)
        self.assertAlmostEqual(idf2.curvecubiclinears[0].minimum_value_of_x, var_minimum_value_of_x)
        self.assertAlmostEqual(idf2.curvecubiclinears[0].maximum_value_of_x, var_maximum_value_of_x)
        self.assertAlmostEqual(idf2.curvecubiclinears[0].minimum_value_of_y, var_minimum_value_of_y)
        self.assertAlmostEqual(idf2.curvecubiclinears[0].maximum_value_of_y, var_maximum_value_of_y)
        self.assertAlmostEqual(idf2.curvecubiclinears[0].minimum_curve_output, var_minimum_curve_output)
        self.assertAlmostEqual(idf2.curvecubiclinears[0].maximum_curve_output, var_maximum_curve_output)
        self.assertEqual(idf2.curvecubiclinears[0].input_unit_type_for_x, var_input_unit_type_for_x)
        self.assertEqual(idf2.curvecubiclinears[0].input_unit_type_for_y, var_input_unit_type_for_y)
        self.assertEqual(idf2.curvecubiclinears[0].output_unit_type, var_output_unit_type)