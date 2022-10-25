import pytest

class Obstacle:
    x_cord = 0
    y_cord = 0

    @staticmethod
    def set_obstacle(x,y):
       Obstacle.x_cord = x
       Obstacle.y_cord = y

    @staticmethod
    def get_obstacle():
        return (Obstacle.x_cord,Obstacle.y_cord)

class MarsRover:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'N'
        self.movement = ''
        return
    def set_position_direction(self,x,y,d):
        self.x = x
        self.y = y
        self.direction = d
        return

    def command(self,command_rover):

        if command_rover.isalpha() == False:
            raise TypeError
        else:
            return "command approved"

    def forward_backward(self,inp):
        if inp == 'f':
            self.y = self.y+1
            self.movement = 'f'
        elif inp == 'b':
            self.movement = 'b'
            self.y = self.y-1
        else:
            raise ValueError

    def left_right(self,inp):
        if inp == 'l':
            self.movement = 'l'
            self.x = self.x -1
        elif inp == 'r':
            self.movement = 'r'
            self.x = self.x +1
        else:
            raise ValueError

    def wrap_edge(self):
        if self.x == 0 and self.y == 100:
            self.direction = 'E'
        elif self.x == 100 and self.y == 100:
            self.direction = 'S'
        elif self.x == 100 and self.y == 0:
            self.direction = 'W'
        else:
            self.direction = 'N'
        return "edge wrapped"

    def obstacle_detection(self):
        obstacle_x,obstacle_y = Obstacle.get_obstacle()

        if self.x == obstacle_x and self.y == obstacle_y:
            if self.movement == 'f':
                self.forward_backward('b')
            elif self.movement == 'b':
                self.forward_backward('f')
            elif self.movement == 'l':
                self.left_right('r')
            else:
                self.left_right('l')

def test_inital_position_and_direction():
    rover_obj = MarsRover()
    rover_obj.set_position_direction(5,3,'N')
    assert rover_obj.x == 5
    assert rover_obj.y == 3
    assert rover_obj.direction == 'N'

def test_rover_command():
    rover_obj = MarsRover()
    with pytest.raises(TypeError) as expinfo:
        assert expinfo == rover_obj.command('f1b')

def test_forward_backward():
    rover_obj = MarsRover()
    rover_obj.set_position_direction(10,10,'N')
    current_x = rover_obj.x
    current_y = rover_obj.y
    rover_obj.forward_backward('b')
    assert current_y == rover_obj.y+1

def test_left_right():
    rover_obj = MarsRover()
    rover_obj.set_position_direction(10,10,'N')
    current_x = rover_obj.x
    current_y = rover_obj.y
    rover_obj.left_right('l')
    assert current_x == rover_obj.x+1

def test_wrap_edges():
    rover_obj = MarsRover()
    # let assume that 100 is the max row and col limit
    rover_obj.set_position_direction(0,100,'N')
    assert "edge wrapped" == rover_obj.wrap_edge()

def test_obstacle_detection():
    rover_obj = MarsRover()
    rover_obj.set_position_direction(10,10,'N')
    rover_obj.left_right('r')
    first_x = rover_obj.x
    first_y = rover_obj.y

    Obstacle.set_obstacle(11,10)
    rover_obj.obstacle_detection()
    assert rover_obj.x == 11-1






