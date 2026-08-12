import turtle

def draw_tree(branch_len, t):
    if branch_len > 5:
        # Draw the branch
        t.forward(branch_len)
        # Turn right and create a new, smaller tree
        t.right(20)
        draw_tree(branch_len - 15, t)
        # Turn left to draw the other branch
        t.left(40)
        draw_tree(branch_len - 15, t)
        # Return to the original position
        t.right(20)
        t.backward(branch_len)

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.speed(0) # Maximum speed
    draw_tree(80, t)
    print("Fractal! Click on the window to close.")
    my_win.exitonclick()

main()
