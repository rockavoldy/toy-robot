# 4 x x x x x
# 3 x x x x x
# 2 x x x x x
# 1 x x x x x
# 0 x x x x x
#   0 1 2 3 4

# Constraint
# when there is some commands before PLACE, ignore them
# when PLACE commands is not the same as FORMAT, show warning
# when x/y > 4 OR < 0, show warning

# Input format
# PLACE X,Y,F ...commands
# Output format
# X,Y,F
# Example
# PLACE 0,0,NORTH MOVE REPORT
# 0,1,NORTH

from enum import Enum, EnumMeta
import re
import sys

class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        # Needed to enable check if the string is exist in the enum
        # https://stackoverflow.com/a/65225753/13028862
        return item in cls.__members__.keys()


class BaseEnum(Enum, metaclass=MetaEnum):
    pass

class Facing(BaseEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Command(BaseEnum):
    PLACE = 0
    MOVE = 1
    LEFT = 2
    RIGHT = 3
    REPORT = 4

class Robot():
    pos_x = 0
    pos_y = 0
    border_x = 4
    border_y = 4
    facing = Facing.NORTH

    def __init__(self, x, y, facing, border_x, border_y):
        """ Create new robot with the position, facing, and how big the table is """
        if (x > 4 or x < 0) or (y > 4 or y < 0):
            raise Warning("Can't place the robot outside the board.")
        if facing not in Facing:
            raise Warning("facing is Invalid.")

        self.pos_x = x
        self.pos_y = y
        self.facing = Facing[facing]
        self.border_x = border_x
        self.border_y = border_y

    def move(self):
        """ move method will be used to move 1 step based on the facing """
        if self.pos_x == 0 and self.facing == Facing.WEST:
            raise Warning("Forbidden move")
        if self.pos_x == self.border_x and self.facing == Facing.NORTH:
            raise Warning("Forbidden move")
        if self.pos_y == 0 and self.facing == Facing.SOUTH:
            raise Warning("Forbidden move")
        if self.pos_y == self.border_y and self.facing == Facing.EAST:
            raise Warning("Forbidden move")
        
        if self.facing == Facing.NORTH:
            self.pos_y = self.pos_y + 1
            return
        if self.facing == Facing.EAST:
            self.pos_x = self.pos_x + 1
            return
        if self.facing == Facing.SOUTH:
            self.pos_y= self.pos_y - 1
            return
        if self.facing == Facing.WEST:
            self.pos_x= self.pos_x - 1
            return

    def turn(self, turning):
        """ turn method will be used for command LEFT and RIGHT to turn facing """
        if turning == "LEFT":
            # when current facing is north (value = 0), turn left will be west (value = 3)
            if self.facing == Facing(0):
                self.facing = Facing(3)
            else:
                self.facing = Facing(self.facing.value - 1)
        else:
            # when current facing is west (value = 3), turn right will be north (value = 0)
            if self.facing == Facing(3):
                self.facing = Facing(0)
            else:
                self.facing = Facing(self.facing.value + 1)

    def report(self):
        """ print current status with format posx,posy,facing """
        print("%s,%s,%s" % (self.pos_x, self.pos_y, self.facing.name))

    def __str__(self):
        return "%s,%s,%s" % (self.pos_x, self.pos_y, self.facing.name)

def run(input_cmd):
    input_cmds = input_cmd.split(" ")

    # command place must conform this pattern
    pattern = re.compile("\d+,\d+,[A-Za-z]+")
    robot = False
    for i, cmd in enumerate(input_cmds):
        try:
            if Command[cmd] == Command.PLACE and pattern.match(input_cmds[i+1]) and not robot:
                # Create Robot first by command PLACE
                place_cmd = input_cmds[i+1].split(",")
                robot = Robot(int(place_cmd[0]), int(place_cmd[1]), place_cmd[2], 4, 4)
                continue
            elif pattern.match(cmd) and robot:
                # ignore the placing command since it's already used by PLACE command
                continue
            elif cmd in Command and robot:
                match Command[cmd]:
                    case Command.MOVE:
                        robot.move()
                    case Command.LEFT:
                        robot.turn("LEFT")
                    case Command.RIGHT:
                        robot.turn("RIGHT")
                    case Command.REPORT:
                        robot.report()
            else:
                continue

        except Warning as e:
            pass
            # print("Warning: %s" % e)
        finally:
            continue

if __name__ == '__main__':
    arg_file = sys.argv[1:]
    if len(arg_file) == 0:
        while True:
            input_cmd = input("Enter commands: ")
            run(input_cmd)
    else:
        file = open(arg_file[0])
        try:
            for line in file.readlines():
                run(line.rstrip())
        finally:
            file.close()