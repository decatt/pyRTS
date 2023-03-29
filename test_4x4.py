import numpy
import time
from pyrts import RTSENV, init_map

#grid states
NUMSTATE = 23

PLAYER1 = 0
PLAYER2 = 1
NONE = 2
WAITING = 3
WORKER = 4
SOLDIER = 5
BASE = 6
BARRACKS = 7
RESOURCE = 8
HP = 9
ATK = 10
ATKRANGE = 11
RP = 12 # number of resource
MOVING = 13
ATTACKING = 14
HARVESTING = 15
RETURNING = 16
PRODUCING = 17
ACTIONUP = 18
ACTIONRIGHT = 19
ACTIONDOWN = 20
ACTIONLEFT = 21
TARGET = 22

#vetor states
WORKER1=0
SOLDIER1=1
BASE1=2
BARRACKS1=3
WORKER2=4
SOLDIER2=5
BASE2=6
BARRACKS2=7
RESOURCES=8
NOTHING=9

#action
NUMACTION = 9

MOVE = 0
ATTACK = 1
HARVEST = 2
RETURN = 3
PRODUCE = 4
UP = 5
RIGHT = 6
DOWN = 7
LEFT = 8

test_map1=numpy.array([[NOTHING,NOTHING,BASE2,RESOURCES,
                        NOTHING,NOTHING,BASE2,BASE2,
                        NOTHING,NOTHING,NOTHING,NOTHING,
                        BASE1,NOTHING,NOTHING,NOTHING]])
h=4
w=4
num_nev = 1

init_state = init_map(test_map1,num_nev,h,w)
envs = RTSENV(num_nev,init_state,h,w)
while True:
    envs.render()
    actions = numpy.zeros((num_nev,h*w,NUMACTION))
    if envs.states[0][12][BASE] == 1 and envs.states[0][:,WORKER].sum() < 1:
        actions[0][12] = numpy.array([0.,0.,0.,0.,1.,1.,0.,0.,0.])
    if envs.states[0][8][WORKER] == 1 and envs.states[0][8][RP] == 1:
        actions[0][8] = numpy.array([0.,0.,0.,1.,0.,0.,0.,1.,0.])
    elif envs.states[0][8][WORKER] == 1 and envs.states[0][8][RP] == 0:
        actions[0][8] = numpy.array([1.,0.,0.,0.,0.,1.,0.,0.,0.])
    elif envs.states[0][4][WORKER] == 1 and envs.states[0][4][RP] == 0:
        actions[0][4] = numpy.array([1.,0.,0.,0.,0.,1.,0.,0.,0.])
    elif envs.states[0][4][WORKER] == 1 and envs.states[0][4][RP] == 1:
        actions[0][4] = numpy.array([1.,0.,0.,0.,0.,0.,0.,1.,0.])
    elif envs.states[0][0][WORKER] == 1 and envs.states[0][0][RP] == 0:
        actions[0][0] = numpy.array([1.,0.,0.,0.,0.,0.,1.,0.,0.])
    elif envs.states[0][0][WORKER] == 1 and envs.states[0][0][RP] == 1:
        actions[0][0] = numpy.array([1.,0.,0.,0.,0.,0.,0.,1.,0.])
    elif envs.states[0][1][WORKER] == 1 and envs.states[0][1][RP] == 0:
        if envs.states[0][2][PLAYER2] == 1:
            actions[0][1] = numpy.array([0.,1.,0.,0.,0.,0.,1.,0.,0.])
        elif envs.states[0][2][NONE] == 1:
            actions[0][1] = numpy.array([1.,0.,0.,0.,0.,0.,1.,0.,0.])
    elif envs.states[0][1][WORKER] == 1 and envs.states[0][1][RP] == 1:
        actions[0][1] = numpy.array([1.,0.,0.,0.,0.,0.,0.,0.,1.])
    elif envs.states[0][2][WORKER] == 1 and envs.states[0][2][RP] == 0:
        actions[0][2] = numpy.array([0.,0.,1.,0.,0.,0.,1.,0.,0.])
    elif envs.states[0][2][WORKER] == 1 and envs.states[0][2][RP] == 1:
        actions[0][2] = numpy.array([1.,0.,0.,0.,0.,0.,0.,0.,1.])

    envs.step(actions,PLAYER1)
    
    

