import utmp
import os

# Define the wtmp file location (usually "/var/log/wtmp")
WTMP_FILE = '/home/kali/repo/obsidian-vault/obsidian-vault/CTF/HTB/sherlock/wtmp'

# Check if the wtmp file exists
if os.path.exists(WTMP_FILE):
    # Open the wtmp file using the utmp library
    with open(WTMP_FILE, 'rb') as wtmp_file:
        # Iterate over the entries in the wtmp file
        for entry in utmp.read(wtmp_file):
            # Each entry contains different fields like:
            #   - ut_user: the name of the user
            #   - ut_line: the terminal (e.g., tty1, pts/0)
            #   - ut_host: the remote hostname (if applicable)
            #   - ut_time: the time of the entry

            print(f"User: {entry.ut_user}, Terminal: {entry.ut_line}, "
                  f"Host: {entry.ut_host}, Time: {entry.ut_time}")
else:
    print(f"Error: {WTMP_FILE} not found!")

