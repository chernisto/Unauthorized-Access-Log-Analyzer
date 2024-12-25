# Unauthorized Access Log Analyzer

This Python project is a **Log Analysis Tool** that processes Apache server log files to identify and analyze unauthorized access attempts. It highlights suspicious IP addresses and visualizes failed login attempts to aid in understanding attack patterns.

---

## 📜 Features

- **Parse Apache Logs**:
  - Extracts IP addresses and HTTP status codes from log files.
- **HTTP Status Code Analysis**:
  - Summarizes occurrences of various HTTP status codes.
- **Unauthorized Access Detection**:
  - Identifies failed login attempts (HTTP 401).
- **Suspicious IP Identification**:
  - Highlights IP addresses with multiple unauthorized access attempts.
- **Visualization**:
  - Generates a bar chart of IPs involved in unauthorized attempts.
- **Export Data**:
  - Saves suspicious IPs to a CSV file for further analysis.

---

## 📁 Project Files

- `log_parser.py`: Python script that performs log parsing, analysis, and visualization.
- `sample_logs.txt`: Sample Apache log file for testing.
- `suspicious_ips.csv`: CSV file containing the extracted suspicious IPs.
- `unauthorized_attempts.png`: Bar chart visualizing unauthorized access attempts.

---

## 🔧 Requirements

Ensure the following dependencies are installed:

- **Python**: Version 3.7+
- **Libraries**:
  - `pandas`
  - `matplotlib`

Install the required libraries using pip:

```bash
pip install pandas matplotlib
```
---

## 🚀 Usage

**1. Clone the Repository**:

```bash
git clone <repository_url>
cd log_parser_project
```

**2. Prepare Log File**:
- Place the log file you want to analyze in the project directory.
- Rename it to `apache_logs.txt` or update the file name in the script.

**3. Run the Script**:
```bash
python log_parser.py
```

**4. Outputs**:
- Terminal: Summary of HTTP status codes and suspicious IPs.
- Files:
  - ``suspicious_ips.csv``: Contains failed login attempts.
  - ``unauthorized_attempts.png``: Bar chart visualization.

---

## 📝 Sample Output

**Terminal Output**
```
HTTP Status Code Counts:
status
200    9126
304     445
404     213
...

Suspicious IPs (more than 1 unauthorized attempt):
ip
192.168.1.1    2
```

**Visualization**

![Screenshot 2024-12-25 135648](https://github.com/user-attachments/assets/e8678532-a0f5-402c-a4ae-e4ad7592adfa)

---

## ⚙️ How It Works

**1. Log Parsing**:
- Uses regular expressions to extract IP addresses and HTTP status codes from the log file.
  
**2. Data Analysis**:
- Identifies failed attempts (HTTP 401) and counts occurrences by IP.
  
**3. Visualization**:
- Bar chart displaying IPs with failed login attempts.

---

## ✨ Enhancements

**Potential future improvements**:
- Geolocation:
  - Use APIs (e.g., ``ipinfo`` or ``geoip2``) to map IPs to locations.
- Real-Time Analysis:
  - Monitor logs dynamically as they are written.
- Dashboard Integration:
  - Export results to tools like Kibana or Grafana for advanced visualization.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for enhancements or bug fixes.

---

## 📄 License

This project is licensed under the MIT License. See the ``LICENSE`` file for details.

---

## 📬 Connect with Me

LinkedIn: https://www.linkedin.com/in/chernor-a-bah

If you like this project, give it a ⭐ and share your feedback!
