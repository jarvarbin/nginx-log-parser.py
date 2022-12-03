import re
import csv

# Define the regular expression pattern for parsing the log line
log_pattern = re.compile(r"(?P<ip_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<time>[^\]]*)\] \"(?P<method>[A-Z]*) (?P<url>[^\"]*) (?P<protocol>[^\"]*)\" (?P<status>\d*) (?P<bytes>\d*) \"(?P<referrer>[^\"]*)\" \"(?P<user_agent>[^\"]*)\"")

# Define the path to the nginx log file
log_file = "/var/log/nginx/access.log"

# Open the log file for reading
with open(log_file, "r") as f:
  # Open the output CSV file for writing
  with open("nginx_logs.csv", "w") as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)

    # Write the CSV header row
    writer.writerow(["IP Address", "Time", "Method", "URL", "Protocol", "Status", "Bytes", "Referrer", "User Agent"])

    # Read each line of the log file
    for line in f:
      # Use the regular expression to parse the log line
      match = log_pattern.match(line)
      if match:
        # Extract the data from the log line
        ip_address = match.group("ip_address")
        time = match.group("time")
        method = match.group("method")
        url = match.group("url")
        protocol = match.group("protocol")
        status = match.group("status")
        bytes = match.group("bytes")
        referrer = match.group("referrer")
        user_agent = match.group("user_agent")

        # Write the data to the CSV file
        writer.writerow([ip_address, time, method, url, protocol, status, bytes, referrer, user_agent])
