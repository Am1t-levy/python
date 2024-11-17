import csv
import time
import speedtest
from datetime import datetime

# Function to test internet speed and return results
def test_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()  # Select the best server based on ping
    download_speed = st.download() / 1_000_000  # Convert from bits/s to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert from bits/s to Mbps
    return download_speed, upload_speed

# Function to log results to CSV
def log_speed_to_csv():
    file_name = "internet_speed.csv"
    
    # Check if the CSV file exists
    try:
        with open(file_name, mode='r') as file:
            pass  # File exists, do nothing
    except FileNotFoundError:
        # File does not exist, create it with headers
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Download Speed (Mbps)", "Upload Speed (Mbps)"])
    
    while True:
        # Get current timestamp and internet speeds
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        download_speed, upload_speed = test_internet_speed()
        
        # Log data to CSV
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, round(download_speed, 2), round(upload_speed, 2)])
        
        # Print to console for real-time feedback (optional)
        print(f"{timestamp} - Download Speed: {round(download_speed, 2)} Mbps, Upload Speed: {round(upload_speed, 2)} Mbps")
        
        # Wait for 5 minutes before running the test again
        time.sleep(300)

if __name__ == "__main__":
    log_speed_to_csv()
