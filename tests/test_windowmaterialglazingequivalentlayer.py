import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.surface_construction_elements import WindowMaterialGlazingEquivalentLayer

log = logging.getLogger(__name__)

class TestWindowMaterialGlazingEquivalentLayer(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowmaterialglazingequivalentlayer(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowMaterialGlazingEquivalentLayer()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_optical_data_type = "Optical Data Type"
        obj.optical_data_type = var_optical_data_type
        # object-list
        var_window_glass_spectral_data_set_name = "object-list|Window Glass Spectral Data Set Name"
        obj.window_glass_spectral_data_set_name = var_window_glass_spectral_data_set_name
        # real
        var_front_side_beambeam_solar_transmittance = 0.5
        obj.front_side_beambeam_solar_transmittance = var_front_side_beambeam_solar_transmittance
        # real
        var_back_side_beambeam_solar_transmittance = 0.5
        obj.back_side_beambeam_solar_transmittance = var_back_side_beambeam_solar_transmittance
        # real
        var_front_side_beambeam_solar_reflectance = 0.5
        obj.front_side_beambeam_solar_reflectance = var_front_side_beambeam_solar_reflectance
        # real
        var_back_side_beambeam_solar_reflectance = 0.5
        obj.back_side_beambeam_solar_reflectance = var_back_side_beambeam_solar_reflectance
        # real
        var_front_side_beambeam_visible_solar_transmittance = 0.5
        obj.front_side_beambeam_visible_solar_transmittance = var_front_side_beambeam_visible_solar_transmittance
        # real
        var_back_side_beambeam_visible_solar_transmittance = 0.5
        obj.back_side_beambeam_visible_solar_transmittance = var_back_side_beambeam_visible_solar_transmittance
        # real
        var_front_side_beambeam_visible_solar_reflectance = 0.5
        obj.front_side_beambeam_visible_solar_reflectance = var_front_side_beambeam_visible_solar_reflectance
        # real
        var_back_side_beambeam_visible_solar_reflectance = 0.5
        obj.back_side_beambeam_visible_solar_reflectance = var_back_side_beambeam_visible_solar_reflectance
        # real
        var_front_side_beamdiffuse_solar_transmittance = 0.5
        obj.front_side_beamdiffuse_solar_transmittance = var_front_side_beamdiffuse_solar_transmittance
        # real
        var_back_side_beamdiffuse_solar_transmittance = 0.5
        obj.back_side_beamdiffuse_solar_transmittance = var_back_side_beamdiffuse_solar_transmittance
        # real
        var_front_side_beamdiffuse_solar_reflectance = 0.5
        obj.front_side_beamdiffuse_solar_reflectance = var_front_side_beamdiffuse_solar_reflectance
        # real
        var_back_side_beamdiffuse_solar_reflectance = 0.5
        obj.back_side_beamdiffuse_solar_reflectance = var_back_side_beamdiffuse_solar_reflectance
        # real
        var_front_side_beamdiffuse_visible_solar_transmittance = 0.5
        obj.front_side_beamdiffuse_visible_solar_transmittance = var_front_side_beamdiffuse_visible_solar_transmittance
        # real
        var_back_side_beamdiffuse_visible_solar_transmittance = 0.5
        obj.back_side_beamdiffuse_visible_solar_transmittance = var_back_side_beamdiffuse_visible_solar_transmittance
        # real
        var_front_side_beamdiffuse_visible_solar_reflectance = 0.5
        obj.front_side_beamdiffuse_visible_solar_reflectance = var_front_side_beamdiffuse_visible_solar_reflectance
        # real
        var_back_side_beamdiffuse_visible_solar_reflectance = 0.5
        obj.back_side_beamdiffuse_visible_solar_reflectance = var_back_side_beamdiffuse_visible_solar_reflectance
        # real
        var_diffusediffuse_solar_transmittance = 0.5
        obj.diffusediffuse_solar_transmittance = var_diffusediffuse_solar_transmittance
        # real
        var_front_side_diffusediffuse_solar_reflectance = 0.5
        obj.front_side_diffusediffuse_solar_reflectance = var_front_side_diffusediffuse_solar_reflectance
        # real
        var_back_side_diffusediffuse_solar_reflectance = 0.5
        obj.back_side_diffusediffuse_solar_reflectance = var_back_side_diffusediffuse_solar_reflectance
        # real
        var_diffusediffuse_visible_solar_transmittance = 0.5
        obj.diffusediffuse_visible_solar_transmittance = var_diffusediffuse_visible_solar_transmittance
        # real
        var_front_side_diffusediffuse_visible_solar_reflectance = 0.5
        obj.front_side_diffusediffuse_visible_solar_reflectance = var_front_side_diffusediffuse_visible_solar_reflectance
        # real
        var_back_side_diffusediffuse_visible_solar_reflectance = 0.5
        obj.back_side_diffusediffuse_visible_solar_reflectance = var_back_side_diffusediffuse_visible_solar_reflectance
        # real
        var_infrared_transmittance_applies_to_front_and_back = 0.5
        obj.infrared_transmittance_applies_to_front_and_back = var_infrared_transmittance_applies_to_front_and_back
        # real
        var_front_side_infrared_emissivity = 0.5
        obj.front_side_infrared_emissivity = var_front_side_infrared_emissivity
        # real
        var_back_side_infrared_emissivity = 0.5
        obj.back_side_infrared_emissivity = var_back_side_infrared_emissivity

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowmaterialglazingequivalentlayers[0].name, var_name)
        self.assertEqual(idf2.windowmaterialglazingequivalentlayers[0].optical_data_type, var_optical_data_type)
        self.assertEqual(idf2.windowmaterialglazingequivalentlayers[0].window_glass_spectral_data_set_name, var_window_glass_spectral_data_set_name)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].front_side_beambeam_solar_transmittance, var_front_side_beambeam_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].back_side_beambeam_solar_transmittance, var_back_side_beambeam_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].front_side_beambeam_solar_reflectance, var_front_side_beambeam_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].back_side_beambeam_solar_reflectance, var_back_side_beambeam_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].front_side_beambeam_visible_solar_transmittance, var_front_side_beambeam_visible_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].back_side_beambeam_visible_solar_transmittance, var_back_side_beambeam_visible_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].front_side_beambeam_visible_solar_reflectance, var_front_side_beambeam_visible_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].back_side_beambeam_visible_solar_reflectance, var_back_side_beambeam_visible_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].front_side_beamdiffuse_solar_transmittance, var_front_side_beamdiffuse_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].back_side_beamdiffuse_solar_transmittance, var_back_side_beamdiffuse_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].front_side_beamdiffuse_solar_reflectance, var_front_side_beamdiffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].back_side_beamdiffuse_solar_reflectance, var_back_side_beamdiffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].front_side_beamdiffuse_visible_solar_transmittance, var_front_side_beamdiffuse_visible_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].back_side_beamdiffuse_visible_solar_transmittance, var_back_side_beamdiffuse_visible_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].front_side_beamdiffuse_visible_solar_reflectance, var_front_side_beamdiffuse_visible_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].back_side_beamdiffuse_visible_solar_reflectance, var_back_side_beamdiffuse_visible_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].diffusediffuse_solar_transmittance, var_diffusediffuse_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].front_side_diffusediffuse_solar_reflectance, var_front_side_diffusediffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].back_side_diffusediffuse_solar_reflectance, var_back_side_diffusediffuse_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].diffusediffuse_visible_solar_transmittance, var_diffusediffuse_visible_solar_transmittance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].front_side_diffusediffuse_visible_solar_reflectance, var_front_side_diffusediffuse_visible_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].back_side_diffusediffuse_visible_solar_reflectance, var_back_side_diffusediffuse_visible_solar_reflectance)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].infrared_transmittance_applies_to_front_and_back, var_infrared_transmittance_applies_to_front_and_back)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].front_side_infrared_emissivity, var_front_side_infrared_emissivity)
        self.assertAlmostEqual(idf2.windowmaterialglazingequivalentlayers[0].back_side_infrared_emissivity, var_back_side_infrared_emissivity)