import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **balls):
    self.balls = balls
    self.contents = []
    for color, number in balls.items():
      for i in range(number):
        self.contents.append(color)

  def draw(self, n_draw):
    j = len(self.contents)
    if n_draw >= j:
      return self.contents
 
    chosen_balls = []
    for x in range(n_draw):
      r = random.randint(0, j-1)
      chosen_balls.append(self.contents[r])
      del self.contents[r]
      j -= 1
    return chosen_balls
  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  print(f"\n---------NEW EXPERIMENT---------\nHat : {hat.balls}\nExp. balls : {expected_balls}\n"
       f"n : {num_balls_drawn}\nN exp: {num_experiments}\n________________________________")
  for i in range(num_experiments):
    h = copy.deepcopy(hat)
    d_balls = h.draw(num_balls_drawn)
    b = True
    for ball, n in expected_balls.items():
      if d_balls.count(ball) < n:
        b = False
    if b:
      success += 1
  return success/num_experiments
        
        
    
