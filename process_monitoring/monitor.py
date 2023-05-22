import psutil
from process_monitoring.notify import send_email

# Monitor process by PID
def monitor_process(pid, sender_email, receiver_email, password):
    print("Start Monitoring ...")
    try:
        process = psutil.Process(pid)
    except psutil.NoSuchProcess:
        print("Process with PID", pid, "not found.")
        return

    while True:
        if not process.is_running():
            # Process is no longer running, send email notification
            subject = "Process Monitoring - Process Completed"
            message = f"The process with PID {pid} has completed."
            send_email(subject, message, sender_email, receiver_email, password)
            break
