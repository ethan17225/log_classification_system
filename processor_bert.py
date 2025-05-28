from sentence_transformers import SentenceTransformer
import joblib

# Load the pre-trained BERT model for sentence embeddings
transformer_model = SentenceTransformer('all-MiniLM-L6-v2')

# Load the pre-trained classifier
classifier = joblib.load('models/log_classifier.joblib')

def classify_with_bert(log_message):
    # Compute the embedding for the log message
    message_embedding = transformer_model.encode(log_message)
    
    probability = classifier.predict_proba([message_embedding])[0]
    
    if max(probability) < 0.5:
        return "Unclassified"
    
    predicted_label = classifier.predict([message_embedding])[0]
    
    return predicted_label

if __name__ == "__main__":
    test_messages = [
        # "User User123 logged in.",
        # "Backup started at 2023-10-01 12:00:00.",
        "Hello, world!",
        # "Backup completed successfully.",
        # "This is a test message.",
        # "System updated to version 1.2.3.",
        # "File report.pdf uploaded successfully by user User456.",
        # "Disk cleanup completed successfully.",
        # "System reboot initiated by user User789.",
        # "Account with ID 1001 created by admin."
    ]
    
    for message in test_messages:
        print(f"Log Message: {message} | Classification: {classify_with_bert(message)}")
    
    