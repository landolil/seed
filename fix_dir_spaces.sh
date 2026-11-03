#!/bin/bash
# Rename directories with spaces to use underscores for Windows compatibility
# Process deepest first to avoid path issues

find /workspace/app -type d -name "* *" ! -path "*/.git/*" | awk -F/ '{print NF-1 "\t" $0}' | sort -rn | cut -f2- | while IFS= read -r dir; do
    if [[ -d "$dir" ]]; then
        parent=$(dirname "$dir")
        old_name=$(basename "$dir")
        new_name=$(echo "$old_name" | sed 's/ /_/g')
        if [[ "$old_name" != "$new_name" ]]; then
            new_path="$parent/$new_name"
            echo "Renaming: $dir -> $new_path"
            git mv "$dir" "$new_path" 2>/dev/null || echo "  Failed (may already be renamed or conflict)"
        fi
    fi
done

echo "Done"