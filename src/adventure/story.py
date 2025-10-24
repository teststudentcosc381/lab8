from adventure.utils import read_events_from_file
import random
from rich import print
from rich.console import Console

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[black]You stand still, unsure what to do. The forest swallows you.[/black]"

def left_path(event):
    return "[red]You walk left. " + event + "[/red]"

def right_path(event):
    return "[blue]You walk right. " + event + "[/blue]"

if __name__ == "__main__":
    console = Console()
    events = read_events_from_file('events.txt')

    print("[green]You wake up in a dark forest. You can go left or right.[/green]")
    while True:
        choice = console.input("[italic yellow]Which direction do you choose?[/italic yellow] (left/right/exit): ")
        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        print(step(choice, events))
