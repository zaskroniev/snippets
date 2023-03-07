#funkcja pobierajaca dowolną ilość argumentów pozycyjnych
# *args - dowolne argumenty, tuple

def calculate_salary(*args, base:float) -> float:
    salary = base
    
    for arg in args:
        salary = salary + (salary * arg)
    
    return salary

print(calculate_salary(0.1, 0.25, 0.3, base=1000))