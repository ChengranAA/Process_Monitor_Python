#######################################################################
## DEMO
from process_monitoring.monitor import monitor_process

if __name__ == "__main__":
    # Set the PID of the process you want to monitor
    process_pid = None # YOUR PID

    # Email configuration
    sender_email = "SENDER@EMAIL.COM"
    receiver_email = "RECEIVER@EMAIL.COM"
    password = "PASSWD"

    monitor_process(process_pid, sender_email, receiver_email, password)