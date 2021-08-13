from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self._write_score()

    def _write_score(self):
        """
        Write the scoreboard
        """
        self.clear()
        self.goto((0, 200))
        self.write(f"{self.l_score} - {self.r_score}",
                   align="center", font=("Courier", 80, "normal"))

    def update_l_score(self):
        """
        Update the l_score
        """
        self.l_score += 1
        self._write_score()

    def update_r_score(self):
        """
        Update the r_score
        """
        self.r_score += 1
        self._write_score()
