class Rectangle:

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


def is_overlap(rect1, rect2):
    x_overlap = rect1.x2 - rect2.x1
    y_overlap = rect1.y2 - rect2.y1

    return x_overlap > 0 or y_overlap > 0


def find_overlap_width(rect1, rect2):

    return min(rect1.x2, rect2.x2) - max(rect1.x1, rect2.x1)


def find_overlap_height(rect1, rect2):

    return min(rect1.y2, rect2.y2) - max(rect1.y1, rect2.y1)


def find_overlap_area(rect1, rect2):

    # check if rectangles do overlap
    if not is_overlap(rect1, rect2):
        return False

    # find length and width of overlap
    return find_overlap_width(rect1, rect2) * find_overlap_height(rect1, rect2)


if __name__ == '__main__':
    rect1 = Rectangle(2, 5, 1, 5)
    rect2 = Rectangle(5, 5, 2, 7)

    print(find_overlap_area(rect1, rect2))
