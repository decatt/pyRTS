import numpy
import matplotlib.pyplot as plt
import time
import random

# import gym
# from gym.envs.classic_control import rendering


#grid states
NUMSTATE = 11

PLAYER1 = 0
PLAYER2 = 1
NONE = 2
WORKER = 3
SOLDIER = 4
BASE = 5
BARRACKS = 6
RESOURCE = 7
HP = 8
ATK = 9
RP = 10 # number of resource

#vetor states
NOTHING=0
WORKER1=1
SOLDIER1=2
BASE1=3
BARRACKS1=4
WORKER2=5
SOLDIER2=6
BASE2=7
BARRACKS2=8
RESOURCES=9


#action
NUMACTION = 4

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

WORKER_HP = 1
WORKER_ATK = 1
WORKER_RESOURCE_LIMIT = 1
SOLDIER_HP = 4
SOLDIER_ATK = 1
BASE_HP = 10
BARRACKS_HP = 5
NUM_INTI_RESOURCE = 25

def softmax(x, axis=None):
    x = x - x.max(axis=axis, keepdims=True)
    y = numpy.exp(x)
    return y / y.sum(axis=axis, keepdims=True)


def sample(logits):
    p = softmax(logits, axis=1)
    c = p.cumsum(axis=1)
    u = numpy.random.rand(len(c), 1)
    choices = (u < c).argmax(axis=1)
    return choices.reshape(-1, 1)

def random_map(num_units):
    unit_list = []
    for i in range(len(num_units)):
        unit_list = unit_list + num_units[i]*[i]
    random.shuffle(unit_list)  
    return unit_list


def init_map(vetor_map,num_env,h,w):
    states = numpy.zeros((num_env,h*w, NUMSTATE))
    for i in range(num_env):
        state = numpy.zeros((h*w, NUMSTATE))
        for j in range(h*w):
            if vetor_map[i][j]==WORKER1:
                state[j]=numpy.array([1,0,0,1,0,0,0,0,WORKER_HP,WORKER_ATK,0])
            elif vetor_map[i][j]==SOLDIER1:
                state[j]=numpy.array([1,0,0,0,1,0,0,0,SOLDIER_HP,SOLDIER_ATK,0])
            elif vetor_map[i][j]==BASE1:
                state[j]=numpy.array([1,0,0,0,0,1,0,0,BASE_HP,0,0])
            elif vetor_map[i][j]==BARRACKS1:
                state[j]=numpy.array([1,0,0,0,0,0,1,0,BARRACKS_HP,0,0])
            elif vetor_map[i][j]==WORKER2:
                state[j]=numpy.array([0,1,0,1,0,0,0,0,WORKER_HP,WORKER_ATK,0])
            elif vetor_map[i][j]==SOLDIER2:
                state[j]=numpy.array([0,1,0,0,1,0,0,0,SOLDIER_HP,SOLDIER_ATK,0])
            elif vetor_map[i][j]==BASE2:
                state[j]=numpy.array([0,1,0,0,0,1,0,0,BASE_HP,0,0])
            elif vetor_map[i][j]==BARRACKS2:
                state[j]=numpy.array([0,1,0,0,0,0,1,0,BARRACKS_HP,0,0])
            elif vetor_map[i][j]==RESOURCES:
                state[j]=numpy.array([0,0,0,0,0,0,0,1,0,0,NUM_INTI_RESOURCE])
            else:
                state[j]=numpy.array([0,0,1,0,0,0,0,0,0,0,0])
        states[i] = state
    return states

class LightRTS:
    def __init__(self,num_envs,init_states,map_hight,map_width):
        self.num_envs = num_envs
        self.map_hight = map_hight
        self.map_width = map_width
        self.init_states = init_states
        self.states = self.init_states
        self.produce_worker_cost = 1
        self.produce_soldier_cost = 4
        self.init_team_resource = 5
        self.team_resources=numpy.array([[self.init_team_resource,self.init_team_resource] for _ in range(num_envs)])

        self.viewer = None
        self.shape_size = 50
        self.vacant = 20

    def step(self,actions, allay = 0):
        rewards = numpy.array([0 for _ in range(self.num_envs)])
        done = False
        info = dict()

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
                    if state[pos][allay] == 1 and action[pos].sum()>0:
                        target = -1
                        if action[pos][UP] == 1:
                            x = pos % self.map_width
                            y = pos // self.map_width - 1
                            if y < 0:
                                target = -1
                            else:
                                target = self.map_width*y+x
                        elif action[pos][RIGHT] == 1:
                            x = pos % self.map_width + 1
                            y = pos // self.map_width
                            if x >= self.map_width:
                                target = -1
                            else:
                                target = self.map_width*y+x
                        elif action[pos][DOWN] == 1:
                            x = pos % self.map_width
                            y = pos // self.map_width + 1
                            if y >= self.map_hight:
                                target = -1
                            else:
                                target = self.map_width*y+x
                        elif action[pos][LEFT] == 1:
                            x = pos % self.map_width - 1
                            y = pos // self.map_width
                            if x < 0:
                                target = -1
                            else:
                                target = self.map_width*y+x
                        
                        if target < 0:
                            print('Cannot move outside the map')
                        else:
                            # attack if the target is an enemy
                            if  state[target][enemy] == 1:
                                state[target][HP] = state[target][HP] - state[pos][ATK]
                                if state[target][HP] <= 0:
                                    state[target] = numpy.array([0,0,1,0,0,0,0,0,0,0,0])
                            # Harvest if the target is a resource
                            elif state[target][RESOURCE] == 1 and state[pos][RP]<WORKER_RESOURCE_LIMIT:
                                state[target][RP] = state[target][RP] - 1
                                state[pos][RP] = state[pos][RP] + 1
                                if state[target][RP] <= 0:
                                    state[target] = numpy.array([0,0,1,0,0,0,0,0,0,0,0])
                            # move if target is empty
                            elif state[target][NONE] == 1:
                                if state[pos][BASE] == 1:
                                    if self.team_resources[i][allay] >= self.produce_worker_cost:
                                        state[target] = numpy.array([0,0,0,1,0,0,0,0,WORKER_HP,WORKER_ATK,0])
                                        state[target][allay] = 1
                                elif state[pos][BARRACKS] == 1:
                                    if self.team_resources[i][allay] >= self.produce_soldier_cost:
                                        state[target]=numpy.array([0,0,0,0,1,0,0,0,SOLDIER_HP,SOLDIER_ATK,0])
                                        state[target][allay] = 1
                                elif state[pos][WORKER] == 1 or state[pos][SOLDIER]:
                                    state[target] = state[pos]
                                    state[pos] = numpy.array([0,0,1,0,0,0,0,0,0,0,0])
                            # return if target is base
                            elif state[target][BASE] == 1 and state[target][allay] == 1 and state[pos][RP]>0:
                                state[pos][RP] = state[pos][RP] - 1
                                self.team_resources[i][allay] = self.team_resources[i][allay] + 1
            self.states[i] = state
        
        return self.states, rewards, done, info
    
    def render(self):
        plt.cla()
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
                    color = 'y'
                
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
                
                if have_tp:
                    plt.plot(x, self.map_hight-y-1, tp, markersize=40, color = color)
        plt.draw()
        plt.pause(0.3)

    def get_action_mask(self, allay = 0):
        if allay == 0:
            allay = PLAYER1
        else:
            allay = PLAYER2
        
        action_masks = numpy.zeros((self.num_envs,self.map_hight*self.map_width,NUMACTION))

        for i in range(self.num_envs):
             for pos in range(self.map_hight*self.map_width):
                if self.states[i][pos][allay] == 1:
                    x = pos % self.map_width
                    y = pos // self.map_width

                    if y - 1 >= 0:
                        action_masks[i][pos][UP] = 1
                    if x + 1 < self.map_width:
                        action_masks[i][pos][RIGHT] = 1
                    if y + 1 < self.map_hight:
                        action_masks[i][pos][DOWN] = 1
                    if x - 1 >= 0:
                        action_masks[i][pos][LEFT] = 1
        
        return action_masks

if __name__ == "__main__":
    h=4
    w=4
    num_nev = 1

    test_map1=numpy.array([[NOTHING,NOTHING,BASE2,RESOURCES,
                        NOTHING,NOTHING,BASE2,BASE2,
                        NOTHING,NOTHING,NOTHING,NOTHING,
                        BASE1,NOTHING,NOTHING,NOTHING]])
    
    init_state = init_map(test_map1,num_nev,h,w)
    envs = LightRTS(num_nev,init_state,h,w)
    while True:
        envs.render()
        time.sleep(0.01)
        actions = numpy.zeros((num_nev,h*w,NUMACTION))
        if envs.states[0][12][BASE] == 1 and envs.states[0][:,WORKER].sum() < 1:
            actions[0][12] = numpy.array([1.,0.,0.,0.])
        
        if envs.states[0][8][WORKER] == 1 and envs.states[0][8][RP] == 1:
            actions[0][8] = numpy.array([0.,0.,1.,0.])
        elif envs.states[0][8][WORKER] == 1 and envs.states[0][8][RP] == 0:
            actions[0][8] = numpy.array([1.,0.,0.,0.])

        elif envs.states[0][4][WORKER] == 1 and envs.states[0][4][RP] == 0:
            actions[0][4] = numpy.array([1.,0.,0.,0.])
        elif envs.states[0][4][WORKER] == 1 and envs.states[0][4][RP] == 1:
            actions[0][4] = numpy.array([0.,0.,1.,0.])

        elif envs.states[0][0][WORKER] == 1 and envs.states[0][0][RP] == 0:
            actions[0][0] = numpy.array([0.,1.,0.,0.])
        elif envs.states[0][0][WORKER] == 1 and envs.states[0][0][RP] == 1:
            actions[0][0] = numpy.array([0.,0.,1.,0.])

        elif envs.states[0][1][WORKER] == 1 and envs.states[0][1][RP] == 0:
            actions[0][1] = numpy.array([0.,1.,0.,0.])
        elif envs.states[0][1][WORKER] == 1 and envs.states[0][1][RP] == 1:
            actions[0][1] = numpy.array([0.,0.,0.,1.])
            
        elif envs.states[0][2][WORKER] == 1 and envs.states[0][2][RP] == 0:
            actions[0][2] = numpy.array([0.,1.,0.,0.])
        elif envs.states[0][2][WORKER] == 1 and envs.states[0][2][RP] == 1:
            actions[0][2] = numpy.array([0.,0.,0.,1.])

        envs.step(actions,PLAYER1)
    
    
    
