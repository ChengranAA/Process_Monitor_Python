# Show PID function for target process
import os

def show_pid(write_to_file=False):
    pid = os.getpid()
    print("Current script PID:", pid)
    if write_to_file:
        # Write the PID to .pid_monitor file
        file_path = os.path.join(os.getcwd(), ".pid_monitor")
        with open(file_path, "w") as file:
            file.write(str(pid))


# Read PID from .pid_monitor
def get_pid():
    file_path = os.path.join(os.getcwd(), ".pid_monitor")
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            pid = file.read().strip()
            if pid.isdigit():
                return int(pid)
            else:
                print("Invalid PID found in .pid_monitor file.")
    else:
        print(".pid_monitor file not found.")

# Clean up .pid_monitor file
def cleanup():
    file_path = os.path.join(os.getcwd(), ".pid_monitor")
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(".pid_monitor file removed.")
    else:
        print(".pid_monitor file not found.")