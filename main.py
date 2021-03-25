import time
import random

import yaml

import sort_jokes
import sys


sort_jokes.run()
nested = yaml.safe_load(open("jokes2signs.yaml"))
jokes2signs = {}
for d in jokes2signs.values():
    for k, v in d.items():
        jokes2signs[k] = v


print(time.ctime())
start_time = time.time()
game_length = 20
game_is_over = False
player_score = 0
total_counter = 0
missed = {}
while not game_is_over:
  joke = random.choice(list(jokes2signs))
  print(joke)
  player_response = input('which sign?: ')
  total_counter += 1
  player_is_correct = jokes2signs[joke] == player_response
  if player_is_correct:
    player_score += 1
  else:
    missed[joke] = jokes2signs[joke]
  current_time = time.time()
  game_is_over = current_time - start_time >= game_length
  del jokes2signs[joke]

print()
print(time.ctime())
print("Correct Answers: " + str(player_score))
print("Wrong Answers: " + str(total_counter-player_score))
print("Total Questions: " + str(total_counter))
print()
for key, val in missed.items():
  print(f"Missed: '{key}'")
  print(f"Correct Answer: '{val}'\n")
