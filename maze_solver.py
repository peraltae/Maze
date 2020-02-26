'''
   Esteban Peralta
   maze_solver
   Spring 2019

   Program solves maze using recursion
'''
import maze



def rc_update(direction, row_col_pair):
    new_sqr = ()

    #Update up
    if direction == 'U':
        new_sqr = (row_col_pair[0]-1, row_col_pair[1])

    #update down
    if direction == 'D':
        new_sqr = (row_col_pair[0]+1, row_col_pair[1])

    #Update right
    if direction == 'R':
        new_sqr = (row_col_pair[0], row_col_pair[1]+1)

    #update left
    if direction == 'L':
        new_sqr = (row_col_pair[0], row_col_pair[1]-1)

    return new_sqr


def rec(amaze,row_col_pair,been_there):
    path = []
        
    open_dirs_list = amaze.openDirs(row_col_pair)   
    if row_col_pair == amaze.getEnd():
        path.append(row_col_pair)
                  
    else:     
        for dirs in open_dirs_list:     #iterate through the open directions available
            new_sqr = rc_update(dirs,row_col_pair)   #creates list of possible squares to move into
       
            if new_sqr not in been_there:   #moving to new_sqr that has not been visited
                been_there.append(new_sqr)
                s = rec(amaze,new_sqr,been_there)
                if amaze.getEnd() in s:
                    path.append(row_col_pair)
                    path.extend(s)
                    return path  #passing path along to the next function up the call-stack
                elif len(amaze.openDirs(new_sqr)) >= 1 or new_sqr not in been_there:   #deadends
                    been_there.append(new_sqr)  #if deadend encountered, new_sqr is added to been_there list, then move on to next available open_dir
    
    return path  


def solver(amaze):   
    end = amaze.getEnd()
    start = amaze.getStart()
    print('start:', start, 'end:',end)
    print('This is a', amaze.getSize()[0], 'x', amaze.getSize()[1], 'size maze.')   

    #check to see is soln is where I start
    if start == end:
        print('start is end')

    else:
        row_col_pair = start
        been_there = [start]
        soln = rec(amaze,row_col_pair,been_there)
        print('start & end:',start,end)
        print('thinking ...')
        print('your solution path is:')

        for i in soln:
              print(i)

def main():
    try:
        fname = input('Enter file name \n')
        myMaze = maze.Maze(fname)
        solver(myMaze)

    except FileNotFoundError as err:
        print(err)

    except Exception as err:
        print(err)

    
main() 


    

