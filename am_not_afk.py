import time
import random
import sys
import subprocess
from threading import Event
from rich.console import Console
from rich.text import Text
from rich.progress import track
from rich.prompt import Prompt
from rich.panel import Panel
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController, Key

console = Console()
mouse = MouseController()
keyboard = KeyboardController()
stop_event = Event()

# 🛠️ Auto-install dependencies without infinite restart
def install_dependencies():
    missing = False
    try:
        import pynput
        import rich
    except ImportError:
        missing = True
        console.print("🔄 Installing missing dependencies...", style="bold yellow")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

    return missing

# Run installation once and then continue normally
if install_dependencies():
    console.print("✅ Dependencies installed! Restarting...\n", style="bold green")
    time.sleep(2)  # Wait before restarting
    python = sys.executable
    subprocess.run([python] + sys.argv)
    sys.exit()  # Exit after restart

# 🌟 Display Banner
console.print(Panel(Text("🔥 AM-NOT-AFK 🔥", justify="center", style="bold magenta"), title="AFK Prevention Tool", style="blue"))

# 🎛️ User Configuration
interval = float(Prompt.ask("⏳ Interval between actions (seconds)", default="5"))
movement_range = int(Prompt.ask("🎯 Mouse movement range (pixels)", default="20"))
keystroke_enabled = Prompt.ask("⌨️ Enable keystrokes? (yes/no)", default="yes").lower() == "yes"
total_runtime = int(Prompt.ask("⏰ Total runtime in minutes (0 for infinite)", default="0")) * 60

# 🔑 Fix Keypress Issue
special_keys = {
    "space": Key.space,
    "shift": Key.shift,
    "ctrl": Key.ctrl,
    "tab": Key.tab,
    "enter": Key.enter,
    "esc": Key.esc
}
keystroke_list = list(special_keys.keys()) if keystroke_enabled else []

console.print("[bold yellow]✨ Configuration Complete! Starting in 3 seconds...[/bold yellow]")
time.sleep(3)

start_time = time.time()

# 🛠️ AFK Prevention Logic
def move_mouse():
    """Moves the mouse randomly."""
    x, y = mouse.position
    dx = random.randint(-movement_range, movement_range)
    dy = random.randint(-movement_range, movement_range)
    mouse.move(dx, dy)
    console.print(f"[cyan]🖱️ Mouse moved to ({x+dx}, {y+dy})[/cyan]")

def press_key():
    """Simulates a random keypress with fixed special key handling."""
    if keystroke_enabled and keystroke_list:
        key = random.choice(keystroke_list)
        key_to_press = special_keys.get(key, key)  # Convert string to pynput Key object if needed
        keyboard.press(key_to_press)
        keyboard.release(key_to_press)
        console.print(f"[green]⌨️ Pressed key: {key}[/green]")

def avoid_afk():
    """Main AFK prevention loop."""
    while not stop_event.is_set():
        move_mouse()
        if keystroke_enabled:
            press_key()
        if total_runtime and (time.time() - start_time > total_runtime):
            console.print("[bold red]⏳ Time limit reached. Exiting...[/bold red]")
            break
        time.sleep(interval)

# 🛑 Handle CTRL+C Gracefully
def exit_handler():
    stop_event.set()
    console.print("\n[bold red]❌ Stopping AFK Prevention...[/bold red]")
    sys.exit()

try:
    avoid_afk()
except KeyboardInterrupt:
    exit_handler()
