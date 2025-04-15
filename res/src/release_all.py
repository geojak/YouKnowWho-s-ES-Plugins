import os
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
REPO_ROOT = SCRIPT_DIR.parent.parent.resolve()

def get_plugins():
    """Get plugins from versioning.txt"""
    with open(REPO_ROOT/'res'/'versioning.txt') as f:
        return [line.split('|')[0] for line in f if line.strip()]

def release_plugin(plugin):
    """Process one plugin exactly like release.py"""
    # Import functions from release.py
    from release import correct_characters, create_zip, versioning, write_news
    
    corrected = correct_characters(plugin)
    os.chdir(REPO_ROOT/'myplugins')
    create_zip(plugin, corrected)
    os.chdir(REPO_ROOT)
    versioning(plugin, corrected)
    write_news(plugin)

def main():
    os.chdir(REPO_ROOT)
    for plugin in get_plugins():
        try:
            print(f"Processing {plugin}...")
            release_plugin(plugin)
        except Exception as e:
            print(f"Error with