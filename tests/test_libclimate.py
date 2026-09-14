import unittest

import libclimate


class Test_libclimate(unittest.TestCase):

    def test_version(self):

        self.assertEqual('0.0.0.1', libclimate.__version__)

    def test_runtime_dependencies_importable(self):

        self.assertEqual('diagnosticism', libclimate.diagnosticism.__name__)
        self.assertEqual('pyclasp', libclimate.pyclasp.__name__)
        self.assertEqual('woad', libclimate.woad.__name__)
