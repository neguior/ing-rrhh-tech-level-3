# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 20:57:16 2024

@author: Nelson Enrique Guio
"""
from robot_collisions import robot_collisions

import unittest

class TestRobotCollisions(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(robot_collisions('LR'), '0 0')
        self.assertEqual(robot_collisions('RL'), '1 1')
        self.assertEqual(robot_collisions('RRR'), '0 0 0')
        self.assertEqual(robot_collisions('RRL'), '1 2 1')
        self.assertEqual(robot_collisions('RRLRL'), '1 2 2 2 1')
        self.assertEqual(robot_collisions('LRLR'), '0 1 1 0')
    
    def test_edge_cases(self):
        self.assertEqual(robot_collisions(''), '')
        self.assertEqual(robot_collisions('R'), '0')
        self.assertEqual(robot_collisions('L'), '0')
        self.assertEqual(robot_collisions('RRRR'), '0 0 0 0')
        self.assertEqual(robot_collisions('LLLL'), '0 0 0 0')

if __name__ == '__main__':
    unittest.main()
