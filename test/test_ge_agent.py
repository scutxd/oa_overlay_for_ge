# -*- coding: UTF-8 -*-

__author__ = 'scutxd'
import unittest

import ge_agent


class TestGEAgent(unittest.TestCase):
    def test_generate_kml(self):
        ge_agent.generate_kml(
            '113.3181589196196,30.97968899527223,113.3384812250916,30.99556779277229'
        )
        # self.assertLogs()


if (__name__ == 'main'):
    unittest.main()
