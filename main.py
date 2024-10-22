from task_scheduler import TaskScheduler

def main():
    scheduler = TaskScheduler()

    # Example tasks
    scheduler.add_task("Write report", "2024-11-01 09:00")
    scheduler.add_task("Team meeting", "2024-11-02 10:00")
    scheduler.add_task("Code review", "2024-11-03 14:00")

    scheduler.show_tasks()

if __name__ == "__main__":
    main()