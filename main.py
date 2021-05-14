import time
import random

import yaml

import sort_jokes


sort_jokes.run()
nested = yaml.safe_load(open("jokes2signs.yaml"))
jokes2signs = {}
for d in nested.values():
    for k, v in d.items():
        jokes2signs[k] = v


print(time.ctime())
start_time = time.time()
game_length = 120
game_is_over = False
player_score = 0
total_counter = 0
missed = {}
while not game_is_over:
    joke = random.choice(list(jokes2signs))
    print(joke)
    player_response = input("which sign?: ")
    total_counter += 1
    player_is_correct = jokes2signs[joke] == player_response
    if player_is_correct:
        player_score += 1
    else:
        missed[joke] = {'correct': jokes2signs[joke], 'response': player_response}
    current_time = time.time()
    game_is_over = current_time - start_time >= game_length
    del jokes2signs[joke]

print()
print(time.ctime())
print("Correct Answers: " + str(player_score))
print("Wrong Answers: " + str(total_counter - player_score))
print("Total Questions: " + str(total_counter))
print()
for joke, data in missed.items():
    correct = data['correct']
    response = data['response']
    print(f"Missed: '{joke}'")
    print(f"You answered: '{response}'")
    print(f"Correct Answer: '{correct}'")
    print(f"https://www.signasl.org/sign/{correct}\n")
