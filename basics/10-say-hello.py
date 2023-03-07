from typing import List

def say_hello(names:List[str])->List[str]:
    welcome_msgs = []
    for name in names:
        welcome_msgs.append(f"Hello {name}")
    
    return welcome_msgs


print(say_hello(["Zuzu", "Anka", "Madzia"]))