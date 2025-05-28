from processor_regex import classify_with_regex
from processor_llm import classify_with_llm
from processor_bert import classify_with_bert

def classify(logs):
    labels = []
    for source, log_message in logs:
        label = classify_log(source, log_message)
        labels.append(label)
        
    return labels

def classify_log(source, log_message):
    if source == "LegacyCRM":
        label = classify_with_llm(log_message)
    else:
        label = classify_with_regex(log_message)
        if label is None:
            label = classify_with_bert(log_message)
        
    return label

def classify_csv(input_file):
    import pandas as pd
    df = pd.read_csv(input_file)
    
    df["target_label"] = classify(list(zip(df["source"], df["log_message"])))
    
    output_file = "resources/output.csv"
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    classify_csv("resources/test.csv")
    
    # test_messages = [
    #     "User User123 logged in.",
    #     "Backup started at 2023-10-01 12:00:00.",
    #     "Hello, world!",
    #     "Backup completed successfully.",
    #     "This is a test message.",
    #     "System updated to version 1.2.3.",
    #     "File report.pdf uploaded successfully by user User456.",
    #     "Disk cleanup completed successfully.",
    #     "System reboot initiated by user User789.",
    #     "Account with ID 1001 created by admin."
    # ]
    
    # for message in test_messages:
    #     print(f"Log Message: {message} | Classification: {classify_with_regex(message)}")