'''
Maze class created by John Park, Northeastern University
Spring 2019 for CS5001

'''

class Maze:
    def __init__(self, fname):
        self.read_maze_file(fname)
    
    def read_maze_file(self, fname):
        try:
            fd = open(fname, "r")
            linenum = 1
            vals = [int(x) for x in fd.readline().split()]
            self.dims = (vals[0], vals[1])
            self.start = (vals[2], vals[3])
            self.end = (vals[4], vals[5])
            linenum += 1
            fd.readline()    # discard top wall
            self.right_walls = []
            self.bottom_walls = []
            for r in range(self.dims[0]):
                # process side walls
                self.right_walls.append([])
                linenum += 1
                s = fd.readline()[2::2]
                for c in range(self.dims[1]):
                    self.right_walls[r].append(s[c] == '|')
                # process bottom walls
                self.bottom_walls.append([])
                linenum += 1
                s = fd.readline()[1::2]
                for c in range(self.dims[1]):
                    self.bottom_walls[r].append(s[c] == '-')

        except FileNotFoundError as err:
            raise  # re-raise exception
        except Exception as err:
            print("Processing line", linunum, "raised exception:", err)
            raise  # re-raise exception
    
    def getSize(self):
        return self.dims
    
    def getStart(self):
        return self.start
    
    def getEnd(self):
        return self.end

    def openDirs(self,row_col_pair):
        dirs = []
        
        #going up
        if row_col_pair[0] > 0:
            if not self.bottom_walls[row_col_pair[0]-1][row_col_pair[1]]:
                dirs.append('U')
                
        #Going down
        if row_col_pair[0] < (self.getSize()[0] -1):
            if not self.bottom_walls[row_col_pair[0]][row_col_pair[1]]:
                dirs.append('D')

        #going right
        if row_col_pair[1] < (self.getSize()[1] -1):
            if not self.right_walls[row_col_pair[0]][row_col_pair[1]]:
                dirs.append('R')

        #going left
        if row_col_pair[1] > 0:
            if not self.right_walls[row_col_pair[0]][row_col_pair[1]-1]:
                dirs.append('L')
            
        return dirs
