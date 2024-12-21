import pygame
class diamond:
    def __init__(self, p1, p2, p3, p4, orientation = None):
        self.p1 = p1 #left point
        self.p2 = p2 #top point
        self.p3 = p3 #right point
        self.p4 = p4 #bottom point
        self.center = ((p3[0] + p1[0]) / 2, (p4[1] + p2[1]) / 2)
        self.orientation = orientation
        self.points =[p1,p2,p3,p4]

    @classmethod
    def init(cls, p_1, p_2):
        if type(p_1) == tuple and type(p_2) == tuple and len(p_1) == 2 \
        and len(p_2) == 2:
        
            if p_1[0] == p_2[0] and p_1[1] != p_2[1]:  # Vertical alignment
                p2 = p_1
                p4 = p_2

                diag_len = (p_2[1] - p_1[1])
                half_val = diag_len / 2
                center_y = (p_2[1] + p_1[1]) / 2
                p1 = (p_1[0] - half_val, p_1[1] + half_val)
                p3 = (p_1[0] + half_val, p_1[1] + half_val)
                orientation = 'plumb'

                
            elif p_1[1] == p_2[1] and p_1[0] != p_2[0]:
                p1 = p_1
                p3 = p_2
                diag_len = (p_2[0] - p_1[0])
                half_val = diag_len / 2
                center_x = (p_2[0] + p_1[0]) / 2
                p2 = (center_x,p_1[1]-half_val)
                p4 = (center_x,p_1[1]+half_val)
                orientation = 'level'
            else:
                raise ValueError("Points p_1 and p_2 must align vertically or horizontally.")
            
            box = cls(p1, p2, p3, p4, orientation)  # Create an instance using the class
            return box
        else: 
            raise ValueError('Inputs need to be 2 tuples of length 2')
    @classmethod
    def init_point(cls, point, len , dir):
        if dir == 'left':
            box = cls.init(point,(point[0]-len,point[1]))
            return box
        elif dir == 'right':
            box = cls.init(point,(point[0]+len,point[1]))
            return box
        elif dir == 'up':
            box = cls.init(point,(point[0],point[1]-len))
            return box
        elif dir == 'down':
            box = cls.init(point,(point[0],point[1]+len))
            return box
        
    @classmethod
    def init_center(cls, center, length):
        """
        Initialize a diamond using its center point and length.
        :param center: A tuple (x, y) representing the center point of the diamond.
        :param length: The total distance from one point of the diamond to the opposite point.
        :return: An instance of the diamond class.
        """
        if type(center) != tuple or len(center) != 2:
            raise ValueError("Center must be a tuple of length 2.")
        
        half_length = length / 2
        
        # Calculate the four points of the diamond
        p2 = (center[0], center[1] - half_length)  # Top point
        p1 = (center[0] - half_length, center[1])  # Left point
        p4 = (center[0], center[1] + half_length)  # Bottom point
        p3 = (center[0] + half_length, center[1])  # Right point

        # Use the points to create the diamond instance
        return cls(p1, p2, p3, p4)

    def draw(self, win, color):
        pygame.draw.polygon(win, color, self.points)

    def isin(self, point):
        """takes a point and returns a boolean True if the point is inside the diamond obj"""
        h = ((abs(self.p1[0] - self.p3[0]) / 2) + (abs(self.p2[1] - self.p4[1]) / 2)) / 2
        if abs(point[0]-self.center[0])+abs(point[1]-self.center[1]) <= h:
            return True
        else: 
            return False
        
    def gerCenter(self):
        return self.center

def test():
    # Example usage
    p1 = (5, 5)
    p2 = (5, 20)
    box = diamond.init_point(p1, 5, 'down')

    print(box.p1, box.p2, box.p3, box.p4, box.orientation)

#test()