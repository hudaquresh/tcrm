"""
    Tropical Cyclone Risk Model (TCRM) - Version 1.0 (beta release)
    Copyright (C) 2011 Commonwealth of Australia (Geoscience Australia)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


 Title: TestSamplingOrigin.py
 Author: Nariman Habili, nariman.habili@ga.gov.au
 CreationDate: 2006-12-14
 Description: Unit testing module for SamplingOrigin.py

 Version: $Rev$

 $Id$
"""
import os, sys
import cPickle
import unittest
from scipy import random
import NumpyTestCase
try:
    import pathLocate
except:
    from unittests import pathLocate

# Add parent folder to python path
unittest_dir = pathLocate.getUnitTestDirectory()
sys.path.append(pathLocate.getRootDirectory())
from StatInterface import SamplingOrigin
from Utilities.files import flStartLog


class TestSamplingOrigin(NumpyTestCase.NumpyTestCase):
    
    def setUp(self):
        self.numberOfSamples = 1000
        pkl_file = open(os.path.join(unittest_dir, 'test_data', 'kdeOrigin_xyz.pck'), 'r')
        xp = cPickle.load(pkl_file)
        yp = cPickle.load(pkl_file)
        zp = cPickle.load(pkl_file)
        self.sampOrg = SamplingOrigin.SamplingOrigin(zp, xp, yp)
        random.seed(10)

    def test_GenerateSamples(self):
        """Testing GenerateSamples"""
        samplesp = cPickle.load(open(os.path.join(unittest_dir, 'test_data', 'sample_origin.pck')))
        lonLatp = cPickle.load(open(os.path.join(unittest_dir, 'test_data', 'sample_origin_lonLat.pck')))
        lonLat = self.sampOrg.generateSamples(self.numberOfSamples)
        self.numpyAssertAlmostEqual(lonLatp[:,0], lonLat[:,0])
        self.numpyAssertAlmostEqual(lonLatp[:,1], lonLat[:,1])

    def test_GenerateOneSample(self):
        """Testing GenerateOneSample"""
        xp = 151.89999999999529
        yp = -9.4
        
        x, y = self.sampOrg.generateOneSample()
        self.assertAlmostEqual(xp, x, 4)
        self.assertAlmostEqual(yp, y, 4)

if __name__ == "__main__":

    testSuite = unittest.makeSuite(TestSamplingOrigin,'test')
    unittest.TextTestRunner(verbosity=2).run(testSuite)
