import os
import subprocess
import sys

# Add the directory containing release.py to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from release import correct_characters, create_zip, versioning, write_news

def get_all_plugins():
    """Read all plugins from versioning.txt"""
    plugins = []
    with open('../res/versioning.txt', 'r') as vfile:  # Adjusted path
        for line in vfile:
            if line.strip():  # Skip empty lines
                plugin_name = line.split('|')[0]
                plugins.append(plugin_name)
    return plugins

def release_plugin(plugin):
    """Release a single plugin using existing functions"""
    print(f"\nReleasing plugin: {plugin}")
    corrected = correct_characters(plugin)
    create_zip(plugin, corrected)
    versioning(plugin, corrected)
    write_news(plugin)
    print(f"Successfully released {plugin}")

def main():
    """Main function to release all plugins"""
    # Change working directory to match release.py expectations
    os.chdir(os.path.join(os.path.dirname(__file__), '../..'))
    
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