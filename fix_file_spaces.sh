#!/bin/bash
# Rename files with spaces to use underscores for Windows compatibility

find /workspace/app -type f -name "* *" ! -path "*/.git/*" | while IFS= read -r file; do
    if [[ -f "$file" ]]; then
        parent=$(dirname "$file")
        old_name=$(basename "$file")
        new_name=$(echo "$old_name" | sed 's/ /_/g')
        if [[ "$old_name" != "$new_name" ]]; then
            new_path="$parent/$new_name"
            echo "Renaming: $file -> $new_path"
            git mv "$file" "$new_path" 2>/dev/null || echo "  Failed (may already be renamed or conflict)"
        fi
    fi
done

echo "Done"