from turtle import Turtle


class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """
        Move the ball, bounces on the wall
        """
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move = -self.y_move
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def bounce_x(self):
        """
        Bounce the ball on the paddles
        """
        self.x_move = -self.x_move
        self.move_speed *= 0.9

    def reset_position(self):
        """
        Reset position of the ball
        """
        self.goto((0, 0))
        self.bounce_x()
        self.move_speed = 0.1
