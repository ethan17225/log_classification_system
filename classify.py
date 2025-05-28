from processor_regex import classify_with_regex

def classify(logs):
    labels = []
    for log in logs:
        label = classify_with_regex(log)
        labels.append(label)
        
    return labels

def classify_log(source, log_message):
    if source == "LegacyCRM":
        pass
    else:
        label = classify_with_regex(log_message)
        if label is None:
            pass
        else:
            return label

if __name__ == "__main__":
    test_messages = [
        "User User123 logged in.",
        "Backup started at 2023-10-01 12:00:00.",
        "Hello, world!",
        "Backup completed successfully.",
        "This is a test message.",
        "System updated to version 1.2.3.",
        "File report.pdf uploaded successfully by user User456.",
        "Disk cleanup completed successfully.",
        "System reboot initiated by user User789.",
        "Account with ID 1001 created by admin."
    ]
    
    for message in test_messages:
        print(f"Log Message: {message} | Classification: {classify_with_regex(message)}")