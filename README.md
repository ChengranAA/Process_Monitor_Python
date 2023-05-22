# Process Monitoring Package (Working in Progress ...)

The Process Monitoring package provides functionality to monitor a process by its PID and send email notifications when the process completes.

## Installation

You can install the package using `pip`:

```
pip install process-monitoring
```

## Usage

### Show PID

To display the PID (Process ID) of the current script, use the `show_pid` function:

```python
from process_monitoring.show_pid import show_pid

show_pid()
```

This will print the PID of the current script to the console.

### Monitor Process

To monitor a specific process by its PID and receive email notifications when it is completed, use the `monitor_process` function:

```python
from process_monitoring.monitor import monitor_process

pid = 1234  # Replace with the PID of the process you want to monitor
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@gmail.com"
password = "your_email_password"

monitor_process(pid, sender_email, receiver_email, password)
```

Replace `pid` with the PID of the process you want to monitor. Provide the necessary email configuration, including the sender's email, receiver's email, and email password. This function will continuously check if the process is running. When the process is completed, an email notification will be sent.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.

## License

This package is licensed under the GPL3.0 License. See the [LICENSE](https://chat.openai.com/c/LICENSE) file for more information.
