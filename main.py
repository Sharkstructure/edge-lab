# Sharks of Mistvayo , The System

import datetime

user_input = input("Give me a signal: ").lower()

# decyzja
if "money" in user_input:
    response = "→ Direction: build, not consume."
elif "tired" in user_input:
    response = "→ Direction: reset, not force."
elif "love" in user_input or "her" in user_input:
    response = "→ Direction: feel it, but stay aware."
else:
    response = "→ Direction: observe and refine."

print(response)

# zapis do pamięci
timestamp = datetime.datetime.now()

with open("memory.log", "a") as f:
    f.write(f"{timestamp} | {user_input} | {response}\n")

print("System processed and stored input.")
