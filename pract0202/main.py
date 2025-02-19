from robot import Robot

if __name__ == "__main__":
    robot = Robot(0, 0)
    robot.move("WWWSSSNNNEEE")
    print(robot.path())
