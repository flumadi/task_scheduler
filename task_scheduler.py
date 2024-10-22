import time
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init()

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, datetime_str):
        task_time = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')
        self.tasks.append({"description": description, "time": task_time})
        print(Fore.GREEN + Style.BRIGHT + f"Task '{description}' scheduled for {task_time}" + Style.RESET_ALL)

    def show_tasks(self):
        print(Fore.CYAN + Style.BRIGHT + "\nScheduled Tasks:" + Style.RESET_ALL)
        for task in self.tasks:
            print(Fore.YELLOW + f" - {task['description']} at {task['time']}" + Style.RESET_ALL)

    def run_scheduler(self):
        while self.tasks:
            now = datetime.now()
            for task in self.tasks:
                if task["time"] <= now:
                    print(Fore.RED + Style.BRIGHT + f"Time to: {task['description']}" + Style.RESET_ALL)
                    self.tasks.remove(task)
            time.sleep(60)  # Check every minute