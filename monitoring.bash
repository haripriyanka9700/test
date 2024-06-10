#!/bin/bash

# Define thresholds
CPU_THRESHOLD=80
MEMORY_THRESHOLD=80
DISK_THRESHOLD=80

# Check CPU usage
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}')
CPU_USAGE_VAL=$(echo $CPU_USAGE | tr -d '%')

# Check Memory usage
MEMORY_USAGE=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
MEMORY_USAGE_VAL=$(echo $MEMORY_USAGE | awk '{print int($1+0.5)}')

# Check Disk usage
DISK_USAGE=$(df -h / | grep / | awk '{print $5}')
DISK_USAGE_VAL=$(echo $DISK_USAGE | tr -d '%')

# Log file
LOG_FILE="/var/log/system_health.log"

# Check CPU
if [ $CPU_USAGE_VAL -gt $CPU_THRESHOLD ]; then
  echo "CPU usage is above threshold: $CPU_USAGE" | tee -a $LOG_FILE
fi

# Check Memory
if [ $MEMORY_USAGE_VAL -gt $MEMORY_THRESHOLD ]; then
  echo "Memory usage is above threshold: $MEMORY_USAGE%" | tee -a $LOG_FILE
fi

# Check Disk
if [ $DISK_USAGE_VAL -gt $DISK_THRESHOLD ]; then
  echo "Disk usage is above threshold: $DISK_USAGE" | tee -a $LOG_FILE
fi

# Check Running Processes
echo "Running processes:" | tee -a $LOG_FILE
ps -aux | tee -a $LOG_FILE
