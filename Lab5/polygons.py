import turtle as t


def polygon(n, edge, color):
    """Draw a colored polygon.

    A function using turtle to draw a polygon 
    with arbitrary color and number of edges.

    Parameters
    ----------
    n: int
        number of edges.
    edge: int
        length of each edge.
    color: string
        color of the polygon.
    """
    angle = 360 / n
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(n):
        t.forward(edge)
        t.left(angle)
    t.end_fill()


def triangle(edge, color):
    """Draw a colored triangle.

    See also:
    ---------
    polygon: Same as a polygon with n=3 edges.
    """
    polygon(3, edge, color)


def square(edge, color):
    """Draw a colored square.

    See also:
    ---------
    polygon: Same as a polygon with n=4 edges.
    """
    polygon(4, edge, color)


def hexagon(edge, color):
    """Draw a colored hexagon.

    See also:
    ---------
    polygon: Same as a polygon with n=6 edges.
    """
    polygon(6, edge, color)