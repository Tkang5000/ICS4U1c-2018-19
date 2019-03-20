class Rectangle(object):
    """
    A class representing a rectangle
    """

    def __init__(self, rwidth, rheight):

        self.width = rwidth
        self.height = rheight
        self.area = 0


def main():

    rec2 = Rectangle(5, 4)
    rec2.area = rec2.width * rec2.height

    print("The area of the rectangle is:", str(rec2.area))


main()
