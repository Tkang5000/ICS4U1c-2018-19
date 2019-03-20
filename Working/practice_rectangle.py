

class Rectangle (object):

    def __init__(self):
        self.width = 0
        self.height = 0


def get_area(rec):
    return rec.width * rec.height


def main():

    rect1 = Rectangle()
    rect1.width = float(input())
    rect1.height = float(input())
    print(rect1.width * rect1.height)


main()



