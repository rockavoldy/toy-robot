import unittest
import robot as r

class TestRobot(unittest.TestCase):
    def test_01_create_robot(self):
        robot = r.Robot(0, 0, "NORTH", 5, 5)
        self.assertEqual(robot.pos_x, 0)
        self.assertEqual(robot.pos_y, 0)
        self.assertEqual(robot.facing.name, "NORTH")
        self.assertEqual(robot.border_x, 5)
        self.assertEqual(robot.border_y, 5)
        self.assertEqual(str(robot), "0,0,NORTH")
    
    def test_02_move_robot(self):
        robot = r.Robot(0, 0, "NORTH", 5, 5)
        robot.move()
        self.assertEqual(str(robot), "0,1,NORTH")
    
    def test_03_turn_left_robot(self):
        robot = r.Robot(0, 0, "NORTH", 5, 5)
        robot.turn("LEFT")
        self.assertEqual(str(robot), "0,0,WEST")

    def test_04_turn_right_robot(self):
        robot = r.Robot(0, 0, "NORTH", 5, 5)
        robot.turn("RIGHT")
        self.assertEqual(str(robot), "0,0,EAST")

    def test_05_turn_left_move_robot(self):
        robot = r.Robot(4, 0, "NORTH", 5, 5)
        robot.turn("LEFT")
        self.assertEqual(str(robot), "4,0,WEST")
        robot.move()
        self.assertEqual(str(robot), "3,0,WEST")
    
    def test_05_turn_right_move_robot(self):
        robot = r.Robot(4, 0, "EAST", 5, 5)
        robot.turn("RIGHT")
        self.assertEqual(str(robot), "4,0,SOUTH")
        with self.assertRaises(Warning) as cm:
            robot.move()
        self.assertEqual(str(cm.exception), "Forbidden move")

        self.assertEqual(str(robot), "4,0,SOUTH")

if __name__ == '__main__':
    unittest.main()