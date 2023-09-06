# Toy Robot Simulator

## Constrains
- Square tabletop, 5x5
- No obstruction on table surface
- 0,0 is the most SOUTH WEST corner
- Ignore command that make the robot falling from the table
- Ignore any commands before PLACE

## Commands
- **PLACE** followed by `x,y,FACING` format, Ex. `PLACE 0,0,NORTH`
- **MOVE** move robot by 1 space forward depends on facing
- **LEFT** turn robot 90 degrees to left, Ex. When robot is facing NORTH, turn left make the robot facing WEST
- **RIGHT** turn robot 90 degrees to right
- **REPORT** print current robot status

## How to run
1. Run in interactive mode, series-of-commands is ended with Enter
    ```sh
    python3 robot.py
    ```
2. Load from testcase.txt, it will run every testcase from the file
    ```sh
    python3 robot.py testcase.txt
    ```
