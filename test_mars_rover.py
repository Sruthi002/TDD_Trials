import pytest
class MarsRover:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'N'
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
        elif inp == 'b':
            self.y = self.y-1
        else:
            raise ValueError

    def left_right(self,inp):
        if inp == 'l':
            self.x = self.x -1
        elif inp == 'r':
            self.x = self.x +1
        else:
            raise ValueError

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
    rover_obj.set_position(0,100,'N')



def test_mars_rover():
    assert True

