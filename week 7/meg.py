import turtle


def draw_concentric_squares(side_length, num_squares, shrinking_factor):
    """this program draws shrinking concentric squares"""

    screen = turtle.Screen()
    screen.setup(width=500, height=500)
    screen.bgcolor("white")
    screen.title("Concentric Squares")

    pen = turtle.Turtle()
    pen.speed(1)
    pen.color("purple")
    pen.pensize(2)

    pen.penup()
    pen.goto(-side_length / 2, -side_length / 2)
    pen.pendown()

    current_side = side_length

    for i in range(num_squares):

        for _ in range(4):
            pen.forward(current_side)
            pen.left(90)


        pen.penup()


        move_in = (current_side - (current_side * shrinking_factor)) / 2

        pen.forward(move_in)
        pen.left(90)
        pen.forward(move_in)
        pen.right(90)

        pen.pendown()
        current_side *= shrinking_factor

    pen.hideturtle()
    screen.mainloop()


initial_side = 300
number_of_squares = 5
shrink_factor = 0.8

draw_concentric_squares(initial_side, number_of_squares, shrink_factor)