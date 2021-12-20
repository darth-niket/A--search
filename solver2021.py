#!/usr/local/bin/python3
# solver2021.py : 2021 Sliding tile puzzle solver
#
# Code by: name IU ID
#
# Based on skeleton code by D. Crandall & B551 Staff, September 2021
#
import heapq
import sys
import math
import heapq as heap #Importing heapq to get the state with the lowest manhattan distance

ROWS = 5
COLS = 5


def printable_board(board):
    return [('%3d ') * COLS % board[j:(j + COLS)] for j in range(0, ROWS * COLS, COLS)]

#heuristic - sum of MD
def manhattan_distance_not(state):
    # dictionary of goal states
    goal_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3), 5: (0, 4), 6: (1, 0), 7: (1, 1), 8: (1, 2), 9: (1, 3),
                 10: (1, 4), 11: (2, 0), 12: (2, 1), 13: (2, 2), 14: (2, 3), 15: (2, 4), 16: (3, 0), 17: (3, 1),
                 18: (3, 2), 19: (3, 3), 20: (3, 4), 21: (4, 0), 22: (4, 1), 23: (4, 2), 24: (4, 3), 25: (4, 4)}
    # Convert tuple to list of lists
    t2l = list(state)
    board_as_lol = []
    start = 0
    end = COLS
    for i in range(ROWS):
        board_as_lol.append(t2l[start:end])
        start += COLS
        end += COLS

    #print(state)
    distance_sum = 0
    # Calculate sum of manhattan distance
    for i in range(0, ROWS):
        for j in range(0, COLS):
            goal_coods = goal_dict.get(board_as_lol[i][j])
            distance_sum += abs(goal_coods[0] - i) + abs(goal_coods[1] - j)

    return distance_sum

def manhattan_distance(state):
    goal_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3), 5: (0, 4), 6: (1, 0), 7: (1, 1), 8: (1, 2), 9: (1, 3),
                 10: (1, 4), 11: (2, 0), 12: (2, 1), 13: (2, 2), 14: (2, 3), 15: (2, 4), 16: (3, 0), 17: (3, 1),
                 18: (3, 2), 19: (3, 3), 20: (3, 4), 21: (4, 0), 22: (4, 1), 23: (4, 2), 24: (4, 3), 25: (4, 4)}
                 
    t2l = list(state)
    board_as_lol = []
    start = 0
    end = COLS
    for i in range(ROWS):
        board_as_lol.append(t2l[start:end])
        start += COLS
        end += COLS
    #print(state)
    distance_sum = 0
    for i in range(0, ROWS): 
        for j in range(0, COLS):
            goal_coods = goal_dict.get(board_as_lol[i][j])
            if goal_coods[0] != i and goal_coods[1] != j:
                distance_sum += 1

    return distance_sum

# Calculate g(s) as number of moves executed to reach the current state
def number_of_moves(state):
    return len(state[2].split(" ")) - 1

#COnfigurations for rotations begin here. They are each implemented as seperate functions
#The rotations are 1. Left wrap
#                  2. Right wrap
#                  3. Up with wrap
#                  4. Down with Wrap
#                  5. Outer ring rotation clockwise and anticlockwise
#                  6. Inner ring rotation clockwise and anticlockwise


def innerRingCounterClockWrap(state):
    t2l = list(state)
    board_as_lol = []
    start = 0
    end = COLS
    for i in range(ROWS):
        board_as_lol.append(t2l[start:end])
        start += COLS
        end += COLS

    temp = []
    temp.append(board_as_lol[0])
    temp.append(board_as_lol[1][:1] + board_as_lol[1][2:4] + board_as_lol[2][3:4] + board_as_lol[1][-1:])
    temp.append(
        board_as_lol[2][:1] + board_as_lol[1][1:2] + board_as_lol[2][2:3] + board_as_lol[3][3:4] + board_as_lol[2][-1:])
    temp.append(board_as_lol[3][:1] + board_as_lol[2][1:2] + board_as_lol[3][1:3] + board_as_lol[3][-1:])
    temp.append(board_as_lol[4])

    successor = [0, (), ""]
    for x in range(0, ROWS):
        successor[1] = successor[1] + tuple(temp[x])
    successor[2] = "Icc"
    successor[0] = manhattan_distance(successor[1])

    return  successor


def innerRingClockWrap(state):
    t2l = list(state)
    board_as_lol = []
    start = 0
    end = COLS
    for i in range(ROWS):
        board_as_lol.append(t2l[start:end])
        start += COLS
        end += COLS

    temp = []
    temp.append(board_as_lol[0])
    temp.append(board_as_lol[1][:1] + board_as_lol[2][1:2] + board_as_lol[1][1:3] + board_as_lol[1][-1:])
    temp.append(
        board_as_lol[2][:1] + board_as_lol[3][1:2] + board_as_lol[2][2:3] + board_as_lol[1][3:4] + board_as_lol[2][-1:])
    temp.append(board_as_lol[3][:1] + board_as_lol[3][2:4] + board_as_lol[2][3:4] + board_as_lol[3][-1:])
    temp.append(board_as_lol[4])

    successor = [0, (), ""]
    for x in range(0, ROWS):
        successor[1] = successor[1] + tuple(temp[x])
    successor[2] = "Ic"
    successor[0] = manhattan_distance(successor[1])

    return successor


def outerRingCounterClockWrap(state):
    t2l = list(state)
    board_as_lol = []
    start = 0
    end = COLS
    for i in range(ROWS):
        board_as_lol.append(t2l[start:end])
        start += COLS
        end += COLS

    temp = []
    temp.append(board_as_lol[0][1:] + board_as_lol[1][-1:])
    temp.append(board_as_lol[0][:1] + board_as_lol[1][1:4] + board_as_lol[2][-1:])
    temp.append(board_as_lol[1][:1] + board_as_lol[2][1:4] + board_as_lol[3][-1:])
    temp.append(board_as_lol[2][:1] + board_as_lol[3][1:4] + board_as_lol[4][-1:])
    temp.append(board_as_lol[3][:1] + board_as_lol[4][:4])

    successor = [0, (), ""]
    for x in range(0, ROWS):
        successor[1] = successor[1] + tuple(temp[x])
    successor[2] = "Occ"
    successor[0] = manhattan_distance(successor[1])

    return successor

def outerRingClockWrap(state):
    t2l = list(state)
    board_as_lol = []
    start = 0
    end = COLS
    for i in range(ROWS):
        board_as_lol.append(t2l[start:end])
        start += COLS
        end += COLS

    temp = []
    temp.append(board_as_lol[1][:1] + board_as_lol[0][:4])
    temp.append(board_as_lol[2][:1] + board_as_lol[1][1:4] + board_as_lol[0][-1:])
    temp.append(board_as_lol[3][:1] + board_as_lol[2][1:4] + board_as_lol[1][-1:])
    temp.append(board_as_lol[4][:1] + board_as_lol[3][1:4] + board_as_lol[2][-1:])
    temp.append(board_as_lol[4][1:] + board_as_lol[3][-1:])

    successor = [0, (), ""]
    for x in range(0, ROWS):
        successor[1] = successor[1] + tuple(temp[x])
    successor[2] = "Oc"
    successor[0] = manhattan_distance(successor[1])

    return successor



def SlideLeftWrap(state):
    statesLeftWrapped = []
    listSlideLeft = tuple((state[i: i + ROWS] for i in range(0, len(state), ROWS)))
    result_item = [0, (), ""]
    list_tuple = [elem for elem in listSlideLeft]
    for i in range(len(list_tuple)):
        list_tuple[i] = list_tuple[i][1:5] + list_tuple[i][0:1]
        result_item[1] = list_tuple
        result_item[2] = "L"+str(i+1)
        result_item[0] = 0
        statesLeftWrapped.append(tuple(result_item))
        list_tuple = list(listSlideLeft)
    listofsuccessors = []
    for i in range(0, COLS):
        successor = [0, (), ""]
        for j in range(0, COLS):
            successor[1] += tuple(statesLeftWrapped[i][1][j])
        successor[2] = statesLeftWrapped[i][2]
        successor[0] = manhattan_distance(successor[1])
        listofsuccessors.append(successor)
    return listofsuccessors


def SlideRightWrap(state):
    statesRightWrapped = []
    listSlideRight = tuple((state[i: i + ROWS] for i in range(0, len(state), ROWS)))
    list_tuple = [elem for elem in listSlideRight]
    result_item = [0, (), ""]
    for i in range(len(list_tuple)):
        list_tuple[i] = list_tuple[i][-1:] + list_tuple[i][0:4]
        result_item[1] = list_tuple
        result_item[2] = "R" + str(i + 1)
        result_item[0] = 0
        statesRightWrapped.append(tuple(result_item))
        list_tuple = list(listSlideRight)
    listofsuccessors = []
    for i in range(0, COLS):
        successor = [0, (), ""]
        for j in range(0, COLS):
            successor[1] += tuple(statesRightWrapped[i][1][j])
        successor[2] = statesRightWrapped[i][2]
        successor[0] = manhattan_distance(successor[1])
        listofsuccessors.append(successor)
    return listofsuccessors


def SlideUpWrapAround(state):
    statesUpWrapped = []
    listSlideUp = tuple(state[i: i + 5] for i in range(0, len(state), 5))
    list_tuple = [list(elem) for elem in listSlideUp]
    result_item = [0, (), ""]
    for column_number in range(len(list_tuple)):
        result = PerformSlideUpWrapAround(list_tuple, column_number)
        result = [tuple(elem) for elem in result]
        result_item[1] = result
        result_item[2] = "U" + str(column_number + 1)
        result_item[0] = 0
        statesUpWrapped.append(tuple(result_item))
        list_tuple = list(list(elem) for elem in listSlideUp)

    listofsuccessors = []
    for i in range(0, COLS):
        successor = [0, (), ""]
        for j in range(0, COLS):
            successor[1] += tuple(statesUpWrapped[i][1][j])
        successor[2] = statesUpWrapped[i][2]
        successor[0] = manhattan_distance(successor[1])
        listofsuccessors.append(successor)
    return listofsuccessors


def PerformSlideUpWrapAround(listSlideUp, column_number):
    temp = listSlideUp[0][column_number]
    for j in range(0, len(listSlideUp) - 1):
        listSlideUp[j][column_number] = listSlideUp[j + 1][column_number]
    listSlideUp[len(listSlideUp) - 1][column_number] = temp
    return listSlideUp


def SlideDownWrapAround(state):
    statesDownWrapped = []
    listSlideDown = list(list(state[i: i + 5]) for i in range(0, len(state), 5))
    list_tuple = [list(elem) for elem in listSlideDown]
    result_item = [0, (), ""]
    for column_number in range(len(list_tuple)):
        result = PerformSlideDownWrapAround(list_tuple, column_number)
        result = [tuple(elem) for elem in result]
        result_item[1] = result
        result_item[2] = "D" + str(column_number + 1) #rotation scheme
        result_item[0] = 0 #manhattan distance
        statesDownWrapped.append(tuple(result_item))
        list_tuple = list(list(elem) for elem in listSlideDown)

    listofsuccessors = []
    for i in range(0, COLS):
        successor = [0, (), ""]
        for j in range(0, COLS):
            successor[1] += tuple(statesDownWrapped[i][1][j])
        successor[2] = statesDownWrapped[i][2]
        successor[0] = manhattan_distance(successor[1])
        listofsuccessors.append(successor)
    return listofsuccessors


def PerformSlideDownWrapAround(listSlideDown, column_number):
    temp = listSlideDown[len(listSlideDown) - 1][column_number]
    for j in range(len(listSlideDown) - 1, 0, -1):
        listSlideDown[j][column_number] = listSlideDown[j - 1][column_number]
    listSlideDown[0][column_number] = temp
    return listSlideDown


# return a list of possible successor states
def successors(state):
    listofsuccessors = []
    listofsuccessors.append(innerRingCounterClockWrap(state))
    listofsuccessors.append(innerRingClockWrap(state))
    listofsuccessors.append(outerRingCounterClockWrap(state))
    listofsuccessors.append(outerRingClockWrap(state))
    temp = SlideLeftWrap(state)
    for x in temp:
        listofsuccessors.append(x)
    temp = SlideRightWrap(state)
    for x in temp:
        listofsuccessors.append(x)
    temp = SlideUpWrapAround(state)
    for x in temp:
        listofsuccessors.append(x)
    temp = SlideDownWrapAround(state)
    for x in temp:
        listofsuccessors.append(x)
    return listofsuccessors


# check if we've reached the goal
def is_goal(state):
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25)
    if state == goal_state:
        return True
    else:
        return False


def solve(initial_board):
    """
    1. This function should return the solution as instructed in assignment, consisting of a list of moves like ["R2","D2","U1"].
    2. Do not add any extra parameters to the solve() function, or it will break our grading and testing code.
       For testing we will call this function with single argument(initial_board) and it should return
       the solution.
    3. Please do not use any global variables, as it may cause the testing code to fail.
    4. You can assume that all test cases will be solvable.
    5. The current code just returns a dummy solution.
    """
    fringe = [(0, initial_board, "")]
    closed = []
    data = []
    normalised_dist = 0
    while len(fringe) > 0:
        heap.heapify(fringe)
        max = heap.nlargest(1, fringe)
        min = heap.nsmallest(1, fringe)
        (cost, curr_board_state, rotation_move) = heap.heappop(fringe)
        closed.append(curr_board_state)
        for state in successors(curr_board_state):
            if state[1] in closed:
                continue
            if is_goal(state[1]):
                state[2] = rotation_move + state[2]
                return state[2].split(" ")
            state[2] = rotation_move + state[2] + " "
            #if max[0][0]==min[0][0]:
            #    normalised_dist = 0
            #else:
            #    normalised_dist = (cost-min[0][0])/(max[0][0]-min[0][0])

            state[0] = number_of_moves(state) + state[0] #f(s) = g(s) + h(s)
            heap.heappush(fringe, state)
    return "no path found"

# Please don't modify anything below this line
#
if __name__ == "__main__":
    if (len(sys.argv) != 2):
        raise (Exception("Error: expected a board filename"))

    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [int(i) for i in line.split()]

    if len(start_state) != ROWS * COLS:
        raise (Exception("Error: couldn't parse start state file"))

    print("Start state: \n" + "\n".join(printable_board(tuple(start_state))))

    print("Solving...")
    route = solve(tuple(start_state))

    print("Solution found in " + str(len(route)) + " moves:" + "\n" + " ".join(route))
