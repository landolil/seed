#!/usr/bin/env python3
"""Rename directories with spaces to use underscores for Windows compatibility."""
import os
import subprocess
import sys

def get_dirs_with_spaces(root):
    """Get all directories with spaces, sorted deepest first."""
    dirs = []
    for dirpath, dirnames, _ in os.walk(root):
        if '.git' in dirpath:
            continue
        for d in dirnames:
            if ' ' in d:
                full = os.path.join(dirpath, d)
                dirs.append(full)
    # Sort by depth (deepest first) to avoid path issues
    dirs.sort(key=lambda x: x.count(os.sep), reverse=True)
    return dirs

def rename_dir(old_path, new_path):
    """Rename directory using git mv."""
    try:
        result = subprocess.run(['git', 'mv', old_path, new_path], 
                               capture_output=True, text=True, cwd='/workspace/app')
        if result.returncode != 0:
            print(f"ERROR renaming {old_path} -> {new_path}: {result.stderr}")
            return False
        print(f"Renamed: {old_path} -> {new_path}")
        return True
    except Exception as e:
        print(f"EXCEPTION renaming {old_path}: {e}")
        return False

def main():
    root = '/workspace/app'
    dirs = get_dirs_with_spaces(root)
    print(f"Found {len(dirs)} directories with spaces")
    
    renamed = 0
    for old_path in dirs:
        # Get the directory name and parent
        parent = os.path.dirname(old_path)
        old_name = os.path.basename(old_path)
        
        # Replace spaces with underscores
        new_name = old_name.replace(' ', '_')
        new_path = os.path.join(parent, new_name)
        
        if old_path != new_path:
            if rename_dir(old_path, new_path):
                renamed += 1
    
    print(f"Renamed {renamed} directories")

if __name__ == '__main__':
    main()