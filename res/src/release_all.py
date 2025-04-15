import os
import subprocess
import sys
from pathlib import Path

# Get the absolute path to this script's directory
SCRIPT_DIR = Path(__file__).parent.resolve()
REPO_ROOT = SCRIPT_DIR.parent.parent.resolve()

def get_all_plugins():
    """Read all plugins from versioning.txt"""
    versioning_path = REPO_ROOT / 'res' / 'versioning.txt'
    plugins = []
    with open(versioning_path, 'r') as vfile:
        for line in vfile:
            if line.strip():  # Skip empty lines
                plugin_name = line.split('|')[0]
                plugins.append(plugin_name)
    return plugins

def release_plugin(plugin):
    """Release a single plugin using existing functions"""
    print(f"\nReleasing plugin: {plugin}")
    
    # Import functions here to avoid path issues
    from release import correct_characters, create_zip, versioning, write_news
    
    corrected = correct_characters(plugin)
    
    # Change to myplugins directory for zipping
    os.chdir(REPO_ROOT / 'myplugins')
    create_zip(plugin, corrected)
    
    # Run versioning from repo root
    os.chdir(REPO_ROOT)
    versioning(plugin, corrected)
    write_news(plugin)
    
    print(f"Successfully released {plugin}")

def main():
    """Main function to release all plugins"""
    # Start from repo root
    os.chdir(REPO_ROOT)
    
    plugins = get_all_plugins()
    print(f"Found {len(plugins)} plugins to release:")
    for i, plugin in enumerate(plugins, 1):
        print(f"{i}. {plugin}")
    
    print("\nStarting release process...")
    for plugin in plugins:
        try:
            release_plugin(plugin)
        except Exception as e:
            print(f"Error releasing {plugin}: {str(e)}")
            continue
    
    print("\nAll plugins processed!")

if __name__ == "__main__":
    main()