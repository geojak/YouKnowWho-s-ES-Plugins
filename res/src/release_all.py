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

def create_zip(p, corrected):
    """Create zip file in root directory"""
    zip_path = REPO_ROOT / f"{corrected}.zip"
    if zip_path.exists():
        zip_path.unlink()
    subprocess.run(["zip", "-r", str(zip_path), p], 
                 cwd=REPO_ROOT / "myplugins",
                 stdout=subprocess.DEVNULL)
    return zip_path

def release_plugin(plugin):
    """Release a single plugin"""
    print(f"\nReleasing plugin: {plugin}")
    
    from release import correct_characters, versioning, write_news
    
    corrected = correct_characters(plugin)
    create_zip(plugin, corrected)
    
    os.chdir(REPO_ROOT)
    versioning(plugin, corrected)
    write_news(plugin)
    
    # Read generated tags
    with open(os.getenv('GITHUB_ENV'), "r") as f:
        env_vars = f.read()
    
    update_tag = next(line.split('=')[1] for line in env_vars.split('\n') 
                     if line.startswith('UPDATE_TAG='))
    update_tag2 = next(line.split('=')[1] for line in env_vars.split('\n') 
                      if line.startswith('UPDATE_TAG2='))
    
    return update_tag, update_tag2

def main():
    """Main function to release all plugins"""
    os.chdir(REPO_ROOT)
    
    plugins = get_all_plugins()
    print(f"Found {len(plugins)} plugins to release:")
    
    release_data = []
    for plugin in plugins:
        try:
            tag, tag2 = release_plugin(plugin)
            release_data.append(f"{plugin},{tag},{tag2}\n")
            print(f"Successfully processed {plugin}")
        except Exception as e:
            print(f"Error releasing {plugin}: {str(e)}")
            continue
    
    print("\nAll plugins processed!")

if __name__ == "__main__":
    main()