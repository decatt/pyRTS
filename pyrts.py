import numpy
import matplotlib.pyplot as plt

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

WORKER_HP = 1
WORKER_ATK = 1
WORKER_ATK_RANGE = 1
SOLDIER_HP = 4
SOLDIER_ATK = 1
SOLDIER_ATK_RANGE = 1
BASE_HP = 10
BARRACKS_HP = 5
NUM_INTI_RESOURCE = 25


class RTSENV:
    def __init__(self,num_envs,init_states,map_hight=4,map_width=4):
        self.num_envs = num_envs
        self.map_hight = map_hight
        self.map_width = map_width
        self.init_states = init_states
        self.states = self.init_states
        self.atk_time_cost = 1
        self.move_time_cost = 1
        self.harvest_time_cost = 1
        self.return_time_cost = 1
        self.produce_worker_time = 1
        self.produce_soldier_time = 1
        self.produce_worker_cost = 1
        self.produce_soldier_cost = 4
        self.init_team_resource = 5
        self.team_resources=numpy.array([[self.init_team_resource,self.init_team_resource] for _ in range(num_envs)])

    def reset(self):
        self.init_states = self.init_states,
        self.states = self.init_states

    def step(self,actions, allay = 0):
        if allay == 0:
            allay = PLAYER1
            enemy = PLAYER2
        else:
            allay = PLAYER2
            enemy = PLAYER1
        for i in range(self.num_envs):
            state = self.states[i]
            action = actions[i]
            if action.sum()==0:
                continue
            else:
                for pos in range(self.map_hight*self.map_width):
                    target = int(state[pos][TARGET])
                    if state[pos][allay] == 1:
                        if state[pos][WAITING] > 0:
                            state[pos][WAITING] = state[pos][WAITING] - 1
                            if state[pos][WAITING] == 0:
                                if target < 0:
                                    continue                     
                                else:
                                    if state[pos][ATTACKING] == 1 and state[target][enemy] == 1:
                                        state[target][HP] = state[target][HP] - state[pos][ATK]
                                        state[pos][ATTACKING] = 0
                                        if state[target][HP] < 1:
                                            state[target] = numpy.array([0.,0.,1.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,-1.])
                                    elif state[pos][MOVING] == 1 and state[target][NONE] == 1 and state[target][RESOURCE] == 0:
                                        state[pos][MOVING] = 0
                                        state[target] = state[pos]
                                        state[pos] = numpy.zeros((NUMSTATE,))
                                        state[pos][NONE] = 1
                                    elif state[pos][HARVESTING] == 1 and state[pos][RP] == 0 and state[target][RESOURCE] == 1 and state[target][RP]>0:
                                        state[target][RP] = state[target][RP] - 1
                                        state[pos][RP] = 1
                                        state[pos][HARVESTING] = 0
                                    elif state[pos][RETURNING] == 1 and state[pos][RP] == 1 and state[target][BASE] == 1 and state[target][allay] == 1:
                                        state[pos][RP] = 0
                                        self.team_resources[i][allay] = self.team_resources[i][allay] + 1
                                        state[pos][RETURNING] = 0
                                    elif state[pos][PRODUCING] == 1 and  state[target][NONE] == 1:
                                        if state[pos][BARRACKS] == 1:
                                            if allay == PLAYER1:
                                                state[target] = numpy.array([1.,0.,0.,0.,0.,1.,0.,0.,0.,SOLDIER_HP,SOLDIER_ATK,SOLDIER_ATK_RANGE,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,-1.])
                                            elif allay == PLAYER2:
                                                state[target] = numpy.array([0.,1.,0.,0.,0.,1.,0.,0.,0.,SOLDIER_HP,SOLDIER_ATK,SOLDIER_ATK_RANGE,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,-1.])
                                        elif state[pos][BASE] == 1:
                                            if allay == PLAYER1:
                                                state[target] = numpy.array([1.,0.,0.,0.,1.,0.,0.,0.,0.,WORKER_HP,WORKER_ATK,WORKER_ATK_RANGE,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,-1.])
                                            elif allay == PLAYER2:
                                                state[target] = numpy.array([0.,1.,0.,0.,1.,0.,0.,0.,0.,WORKER_HP,WORKER_ATK,WORKER_ATK_RANGE,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,-1.])
                                        state[pos][PRODUCING] = 0
                                    
                                    state[pos][ACTIONUP] = 0
                                    state[pos][ACTIONRIGHT] = 0
                                    state[pos][ACTIONDOWN] = 0
                                    state[pos][ACTIONLEFT] = 0
                        else:
                            if action[pos][UP] == 1:
                                x = pos % self.map_width
                                y = pos // self.map_width - 1
                                if y < 0:
                                    target = -1
                                else:
                                    target = self.map_width*y+x
                                    state[pos][ACTIONUP] = 1
                            elif action[pos][RIGHT] == 1:
                                x = pos % self.map_width + 1
                                y = pos // self.map_width
                                if x > self.map_width:
                                    target = -1
                                else:
                                    target = self.map_width*y+x
                                    state[pos][ACTIONRIGHT] = 1
                            elif action[pos][DOWN] == 1:
                                x = pos % self.map_width
                                y = pos // self.map_width + 1
                                if y > self.map_hight:
                                    target = -1
                                else:
                                    target = self.map_width*y+x
                                    state[pos][ACTIONDOWN] = 1
                            elif action[pos][LEFT] == 1:
                                x = pos % self.map_width - 1
                                y = pos // self.map_width
                                if x < 0:
                                    target = -1
                                else:
                                    target = self.map_width*y+x
                                    state[pos][ACTIONLEFT] = 1
                            
                            if target>=0:
                                state[pos][TARGET] = target
                                if action[pos][ATTACK] == 1:
                                    state[pos][ATTACKING] = 1
                                    state[pos][WAITING] = self.atk_time_cost
                                elif action[pos][MOVE] == 1:
                                    state[pos][MOVING] = 1
                                    state[pos][WAITING] = self.move_time_cost
                                elif action[pos][HARVEST] == 1:
                                    state[pos][HARVESTING] = 1
                                    state[pos][WAITING] = self.harvest_time_cost
                                elif action[pos][RETURN] == 1:
                                    state[pos][RETURNING] = 1
                                    state[pos][WAITING] = self.return_time_cost
                                elif action[pos][PRODUCE] == 1:
                                    if state[pos][BASE] == 1:
                                        if self.team_resources[i][allay]>self.produce_worker_cost:
                                            self.team_resources[i][allay] = self.team_resources[i][allay] - self.produce_worker_cost
                                            state[pos][PRODUCING] = 1
                                            state[pos][WAITING] = self.produce_worker_time
                                    elif state[pos][BARRACKS] == 1:
                                        if self.team_resources[i][allay]>self.produce_soldier_cost:
                                            self.team_resources[i][allay] = self.team_resources[i][allay] - self.produce_soldier_cost
                                            state[pos][PRODUCING] = 1
                                            state[pos][WAITING] = self.produce_soldier_cost
                                else:
                                    continue
            self.states[i] = state
        return self.states
        
    def render(self):
        render_state = numpy.reshape(self.states[0],(self.map_hight,self.map_width,NUMSTATE))
        plt.ylim(-1, self.map_hight)
        plt.xlim(-1, self.map_width)
        for y in range(self.map_hight):
            for x in range(self.map_width):
                unit = render_state[y][x]
                if unit[PLAYER1] == 1:
                    color = 'r'
                elif unit[PLAYER2] == 1:
                    color = 'b'
                else:
                    color = 'g'
                
                have_tp = True
                if unit[BASE] == 1:
                    tp = '*'
                elif unit[WORKER] == 1:
                    tp = 'o'
                elif unit[SOLDIER] == 1:
                    tp = 'p'
                elif unit[BARRACKS] == 1:
                    tp = 'D'
                elif unit[RESOURCE] == 1:
                    tp = 's'
                else:
                    have_tp = False
                
                have_dir = True
                if unit[ACTIONUP] == 1:
                    direction = '<'
                elif unit[ACTIONRIGHT] == 1:
                    direction = '^'
                elif unit[ACTIONDOWN] == 1:
                    direction = '>'
                elif unit[ACTIONLEFT] == 1:
                    direction = 'v'
                else: 
                    have_dir = False

                if have_tp:
                    plt.plot(y, x, tp, markersize=40, color = color)
                if have_dir:
                    plt.plot(y, x, direction, markersize=20, color = 'g')
        plt.draw()
        plt.pause(0.3)
        plt.cla()

    def action_masks(self):
        masks = numpy.zeros((self.num_envs,self.map_hight*self.map_width,NUMACTION))
        
        return masks  
                       
def init_map(vetor_map,num_env,h,w):
    states = numpy.zeros((num_env,h*w, NUMSTATE))
    for i in range(num_env):
        state = numpy.zeros((h*w, NUMSTATE))
        for j in range(h*w):
            if vetor_map[i][j]==WORKER1:
                state[j]=numpy.array([1,0,0,0,1,0,0,0,0,WORKER_HP,WORKER_ATK,WORKER_ATK_RANGE,0,0,0,0,0,0,0,0,0,0,-1])
            elif vetor_map[i][j]==SOLDIER1:
                state[j]=numpy.array([1,0,0,0,0,1,0,0,0,SOLDIER_HP,SOLDIER_ATK,SOLDIER_ATK_RANGE,0,0,0,0,0,0,0,0,0,0,-1])
            elif vetor_map[i][j]==BASE1:
                state[j]=numpy.array([1,0,0,0,0,0,1,0,0,BASE_HP,0,0,0,0,0,0,0,0,0,0,0,0,-1])
            elif vetor_map[i][j]==BARRACKS1:
                state[j]=numpy.array([1,0,0,0,0,0,0,1,0,BARRACKS_HP,0,0,0,0,0,0,0,0,0,0,0,0,-1])
            elif vetor_map[i][j]==WORKER2:
                state[j]=numpy.array([0,1,0,0,1,0,0,0,0,WORKER_HP,WORKER_ATK,WORKER_ATK_RANGE,0,0,0,0,0,0,0,0,0,0,-1])
            elif vetor_map[i][j]==SOLDIER2:
                state[j]=numpy.array([0,1,0,0,0,1,0,0,0,SOLDIER_HP,SOLDIER_ATK,SOLDIER_ATK_RANGE,0,0,0,0,0,0,0,0,0,0,-1])
            elif vetor_map[i][j]==BASE2:
                state[j]=numpy.array([0,1,0,0,0,0,1,0,0,BASE_HP,0,0,0,0,0,0,0,0,0,0,0,0,-1])
            elif vetor_map[i][j]==BARRACKS2:
                state[j]=numpy.array([0,1,0,0,0,0,0,1,0,BARRACKS_HP,0,0,0,0,0,0,0,0,0,0,0,0,-1])
            elif vetor_map[i][j]==RESOURCES:
                state[j]=numpy.array([0.,0.,1.,0.,0.,0.,0.,0.,1.,0.,0.,0.,NUM_INTI_RESOURCE,0.,0.,0.,0.,0.,0.,0.,0.,0.,-1.])
            else:
                state[j]=numpy.array([0.,0.,1.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,-1.])
        states[i] = state
    return states
