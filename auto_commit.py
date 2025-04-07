import os
import random
import datetime
import requests
import base64
from pathlib import Path

# File paths
SCRIPT_PATH = Path(__file__).resolve()

# GitHub repository details
GITHUB_OWNER = "sakthiish12"
GITHUB_REPO = "auto-commits"
# GitHub Personal Access Token from environment variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get_github_headers():
    return {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

def get_file_sha(path):
    """Get the SHA of a file if it exists."""
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{path}"
    response = requests.get(url, headers=get_github_headers())
    if response.status_code == 200:
        return response.json()["sha"]
    return None

def modify_self():
    """Add a random comment to this script."""
    comments = [
        "Updated the code",
        "Made improvements",
        "Fixed bugs",
        "Enhanced functionality",
        "Optimized performance",
        "Added features",
        "Refactored code",
        "Improved stability",
        "Enhanced documentation",
        "Improved code quality",
        "Added new functionality",
        "Fixed edge cases",
        "Optimized algorithms",
        "Added error handling",
        "Improved user experience",
    ]
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_comment = f"\n# {random.choice(comments)} - {timestamp}"
    
    with open(SCRIPT_PATH, "a") as f:
        f.write(new_comment)

def push_file_to_github(path, content, commit_message):
    """Push a single file to GitHub."""
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{path}"
    
    # Encode content to base64
    content_bytes = content.encode('utf-8')
    content_base64 = base64.b64encode(content_bytes).decode('utf-8')
    
    # Get SHA if file exists
    sha = get_file_sha(path)
    
    # Prepare the data
    data = {
        "message": commit_message,
        "content": content_base64,
        "branch": "main"
    }
    
    if sha:
        data["sha"] = sha
    
    # Make the request
    response = requests.put(url, json=data, headers=get_github_headers())
    
    if response.status_code not in [200, 201]:
        print(f"Error pushing file {path}: {response.status_code}")
        print(response.json())
        return False
    return True

def push_changes():
    """Push changes to GitHub."""
    # Read the current content of the script
    with open(SCRIPT_PATH, "r") as f:
        script_content = f.read()
    
    # Create timestamp for commit
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Auto update {timestamp}"
    
    # Push the script file
    if not push_file_to_github("auto_commit.py", script_content, commit_message):
        print("Failed to push script file")
        return
    
    # Push a timestamp file
    timestamp_content = f"Auto-generated commit at {timestamp}"
    timestamp_path = f"commits/commit_{timestamp.replace(':', '-')}.txt"
    if not push_file_to_github(timestamp_path, timestamp_content, commit_message):
        print("Failed to push timestamp file")
        return
    
    print("Successfully pushed changes to GitHub!")

def check_token():
    """Check if GitHub token is set."""
    if not GITHUB_TOKEN:
        print("Error: GitHub token not set!")
        print("Please edit this script and add your GitHub Personal Access Token.")
        print("You can generate one at: https://github.com/settings/tokens")
        print("Make sure to give it 'repo' permissions.")
        return False
    return True

def main():
    if not check_token():
        return
    modify_self()
    push_changes()

if __name__ == "__main__":
    main() 
# Added error handling - 2025-03-23 19:22:07
# Improved user experience - 2025-03-23 19:31:59
# Fixed edge cases - 2025-03-24 01:11:34
# Made improvements - 2025-03-24 21:45:53
# Improved user experience - 2025-03-25 21:33:23
# Refactored code - 2025-03-29 00:59:57
# Enhanced functionality - 2025-03-29 15:01:38
# Refactored code - 2025-03-30 12:07:15
# Improved user experience - 2025-03-30 23:11:58
# Improved user experience - 2025-04-01 23:30:00
# Added features - 2025-04-02 22:40:57
# Improved user experience - 2025-04-03 22:00:02
# Improved code quality - 2025-04-03 22:11:30
# Optimized algorithms - 2025-04-03 23:00:01
# Improved user experience - 2025-04-04 00:00:01
# Updated the code - 2025-04-04 01:00:02
# Optimized performance - 2025-04-05 01:41:54
# Enhanced functionality - 2025-04-05 02:00:03
# Made improvements - 2025-04-05 02:41:55
# Updated the code - 2025-04-05 13:00:02
# Added new functionality - 2025-04-05 20:00:01
# Optimized performance - 2025-04-05 22:00:02
# Fixed edge cases - 2025-04-06 00:00:01
# Refactored code - 2025-04-06 01:00:03
# Improved code quality - 2025-04-06 02:00:02
# Added new functionality - 2025-04-06 12:00:18
# Optimized algorithms - 2025-04-06 14:00:02
# Fixed bugs - 2025-04-06 15:00:02
# Optimized algorithms - 2025-04-06 22:23:59
# Improved code quality - 2025-04-07 00:23:59
# Optimized performance - 2025-04-07 19:00:02