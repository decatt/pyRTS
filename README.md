# pyRTS
start the example with test_4x4.py
## states
shape = (num_envs,map_height*map_width,grid_state)

gird_state
  * PLAYER1     bool
  * PLAYER2     bool 
  * NONE        bool
  * WAITING     int
  * WORKER      bool
  * SOLDIER     bool
  * BASE        bool
  * BARRACKS    bool
  * RESOURCE    bool
  * HP          int
  * ATK         int
  * ATKRANGE    int
  * RP          int 
  * MOVING      bool
  * ATTACKING   bool
  * HARVESTING  bool
  * RETURNING   bool
  * PRODUCING   bool
  * ACTIONUP    bool
  * ACTIONRIGHT bool
  * ACTIONDOWN  bool
  * ACTIONLEFT  bool
  * TARGET      int
