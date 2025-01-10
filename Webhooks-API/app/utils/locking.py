# app/utils/locking.py

import fcntl

def lock_file(file):
    # Lock the file (example for Unix-like systems)
    fcntl.flock(file, fcntl.LOCK_EX)

def unlock_file(file):
    # Unlock the file
    fcntl.flock(file, fcntl.LOCK_UN)
