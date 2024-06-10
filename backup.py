import os
import shutil
import smtplib
from datetime import datetime
from email.mime.text import MIMEText

# Configurations
SOURCE_DIR = '/path/to/source'
BACKUP_DIR = '/path/to/backup'
REMOTE_SERVER = 'user@remote:/path/to/remote/backup'
LOG_FILE = '/var/log/backup.log'

def log_message(message):
    with open(LOG_FILE, 'a') as log:
        log.write(f'{datetime.now()} - {message}\n')

def backup_directory():
    try:
        # Create a backup
        backup_name = os.path.join(BACKUP_DIR, f'backup_{datetime.now().strftime("%Y%m%d%H%M%S")}')
        shutil.make_archive(backup_name, 'gztar', SOURCE_DIR)
        
        # Copy to remote server
        os.system(f'scp {backup_name}.tar.gz {REMOTE_SERVER}')
        
        log_message('Backup successful.')
        return True
    except Exception as e:
        log_message(f'Backup failed: {str(e)}')
        return False

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'recipient_email@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your_email@example.com', 'password')
        server.sendmail('your_email@example.com', ['recipient_email@example.com'], msg.as_string())

if __name__ == '__main__':
    if backup_directory():
        send_email('Backup Successful', 'The backup operation completed successfully.')
    else:
        send_email('Backup Failed', 'The backup operation failed. Check the log for details.')
