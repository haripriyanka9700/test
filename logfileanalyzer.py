import re
from collections import defaultdict

# Configuration
LOG_FILE = '/path/to/access.log'

# Patterns
pattern_404 = re.compile(r' 404 ')
pattern_request = re.compile(r'"GET (.*?) HTTP/')
pattern_ip = re.compile(r'^(.*?) ')

# Data structures
error_404_count = 0
page_requests = defaultdict(int)
ip_requests = defaultdict(int)

# Analyze log file
with open(LOG_FILE, 'r') as log:
    for line in log:
        # Count 404 errors
        if pattern_404.search(line):
            error_404_count += 1
        
        # Count page requests
        match_request = pattern_request.search(line)
        if match_request:
            page = match_request.group(1)
            page_requests[page] += 1
        
        # Count IP requests
        match_ip = pattern_ip.search(line)
        if match_ip:
            ip = match_ip.group(1)
            ip_requests[ip] += 1

# Summarize report
most_requested_page = max(page_requests, key=page_requests.get)
most_active_ip = max(ip_requests, key=ip_requests.get)

report = f"""
Log Analysis Report:
---------------------
Total number of 404 errors: {error_404_count}

Most requested page: {most_requested_page} with {page_requests[most_requested_page]} requests

IP address with the most requests: {most_active_ip} with {ip_requests[most_active_ip]} requests
"""

print(report)
