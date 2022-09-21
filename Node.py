class Node(object):

    def __init__(self, data, parent = None, left = None, right = None):
        
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        
        self.pos = None
        self.nullable = False
        self.firstpos = []
        self.lastpos = []
        self.followpos = []
        
        