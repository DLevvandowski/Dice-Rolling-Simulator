from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Poproszenie użytkownika o liczbę kości.
num_dice = int(input("Ile kości chcesz rzucić? "))

# Poproszenie użytkownika o liczbę ścianek kości.
dice_sides = []
for die_index in range(num_dice):
    sides = int(input(f"Ile ścianek ma kość {die_index + 1}? "))
    dice_sides.append(sides)

# Poproszenie użytkownika o liczbę rzutów.
num_rolls = int(input("Ile razy chcesz rzucić kośćmi? "))

# Utworzenie obiektów kości na podstawie podanych przez użytkownika liczby 
# ścianek.
dice = [Die(sides) for sides in dice_sides]

# Wykonanie rzutów i zapisanie wyników.
results = []
for roll_num in range(num_rolls):
    # Rzucenie wszystkimi koścmi i zapisanie wyników.
    result = sum(die.roll() for die in dice)
    results.append(result)

# Analiza wyników.
frequencies = []
# Określenie maksymalnego możliwego wyniku.
max_result = sum(die.num_sides for die in dice)
for value in range(len(dice), max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Wizualizacja wyników.
x_values = list(range(len(dice), max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Wynik', 'dtick': 1}
y_axis_config = {'title': 'Częstotliwość występowania wartości'}
my_layout = Layout(title=f'Wynik rzucania {num_dice} kośćmi {num_rolls} razy',
            xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='dice_simulation.html')
