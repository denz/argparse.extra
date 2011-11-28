import unittest

class ArgparseExtraTestCase(unittest.TestCase):
    def test_extras_importable(self):
        from argparse.extra import DictArgumentParser
        from argparse import ArgumentParser
    
    def test_extras_testcase(self):
        from argparse.extra.parsers import GetArgparserTestCase
        suite = unittest.makeSuite(GetArgparserTestCase,'test')
        runner = unittest.TextTestRunner()
        runner.run(suite)
