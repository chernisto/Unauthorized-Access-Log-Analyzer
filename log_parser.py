import re
import pandas as pd
import matplotlib.pyplot as plt

# Load the log file
log_file = "./apache_logs.txt"
with open(log_file, 'r') as file:
    logs = file.readlines()

# Regex to extract IP and status codes
log_pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+).+?"\s(?P<status>\d{3})'
parsed_logs = [
    re.search(log_pattern, line).groupdict()
    for line in logs if re.search(log_pattern, line)
]

# Convert parsed logs to a DataFrame
df = pd.DataFrame(parsed_logs)

# Count occurrences of each status code
status_counts = df['status'].value_counts()
print("HTTP Status Code Counts:")
print(status_counts)

# Filter for failed login attempts (401 Unauthorized)
failed_attempts = df[df['status'] == '401']
print("\nFailed Attempts (401 Unauthorized):")
print(failed_attempts)

# Group by IP and count unauthorized attempts
unauthorized_counts = failed_attempts['ip'].value_counts()
print("\nUnauthorized Access Attempts by IP:")
print(unauthorized_counts)

# Filter IPs exceeding a threshold (e.g., more than 1 attempt)
threshold = 1
suspicious_ips = unauthorized_counts[unauthorized_counts > threshold]
print(f"\nSuspicious IPs (more than {threshold} unauthorized attempts):")
print(suspicious_ips)

# Save suspicious IPs to a CSV file
"""suspicious_ips.to_csv("suspicious_ips.csv", header=["Failed Attempts"])
print("\nSuspicious IPs saved to suspicious_ips.csv")"""

# Visualize unauthorized attempts
plt.figure(figsize=(10, 6))
unauthorized_counts.plot(kind='bar', color='red', title='Unauthorized Access Attempts')
plt.xlabel('IP Address')
plt.ylabel('Failed Attempts')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("unauthorized_attempts.png")
plt.show()
print("\nUnauthorized access attempts graph saved as 'unauthorized_attempts.png'.")
