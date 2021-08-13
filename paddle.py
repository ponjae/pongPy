from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, location):
        """
        Initialize the class

        :param location: Starting location for the paddle
        """
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(location)

    def go_up(self):
        """
        Method for moving the paddle up

        return: None
        """
        new_y = self.ycor() + 20
        self.goto((self.xcor(), new_y))

    def go_down(self):
        """
        Method for moving the paddle down

        return: None
        """
        new_y = self.ycor() - 20
        self.goto((self.xcor(), new_y))
