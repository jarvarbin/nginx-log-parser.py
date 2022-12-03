# nginx-log-parser.py
This script uses a regular expression to parse each line of the nginx log file and extract the relevant data. The extracted data is then written to a CSV file with a header row containing the field names.

To use this script, you would need to replace /var/log/nginx/access.log with the actual path to your nginx log file. You can then run the script and it will extract the data from the log file and write it to the CSV file nginx_logs.csv.
