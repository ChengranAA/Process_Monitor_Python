#######################################################################
## Simulated Task 
import time
from tqdm import tqdm
from process_monitoring import show_pid

# Function to simulate a task with a progress bar
def simulate_task(duration):
    with tqdm(total=duration, desc="Processing", unit="sec") as pbar:
        start_time = time.time()
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time >= duration:
                break
            pbar.update(1)
            time.sleep(1)

if __name__ == "__main__":
    # Set the duration of the task in seconds
    task_duration = 60  # 1 minutes
    show_pid.show_pid()
    simulate_task(task_duration)
