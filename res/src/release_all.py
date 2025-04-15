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
    
    # Read the generated tags from GITHUB_ENV
    env_file = os.getenv('GITHUB_ENV')
    with open(env_file, "r") as f:
        env_vars = f.read()
    
    update_tag = None
    update_tag2 = None
    for line in env_vars.split('\n'):
        if line.startswith('UPDATE_TAG='):
            update_tag = line.split('=')[1]
        elif line.startswith('UPDATE_TAG2='):
            update_tag2 = line.split('=')[1]
    
    return update_tag, update_tag2

def main():
    """Main function to release all plugins"""
    # Start from repo root
    os.chdir(REPO_ROOT)
    
    plugins = get_all_plugins()
    print(f"Found {len(plugins)} plugins to release:")
    for i, plugin in enumerate(plugins, 1):
        print(f"{i}. {plugin}")
    
    print("\nStarting release process...")
    release_data = []
    for plugin in plugins:
        try:
            tag, tag2 = release_plugin(plugin)
            if tag and tag2:  # Only add if tags were generated
                release_data.append(f"{plugin},{tag},{tag2}\n")
        except Exception as e:
            print(f"Error releasing {plugin}: {str(e)}")
            continue
    
    # Write release data to file in the root directory
    with open(REPO_ROOT / 'release_data.txt', 'w') as f:
        f.writelines(release_data)
    
    print("\nAll plugins processed!")

if __name__ == "__main__":
    main()