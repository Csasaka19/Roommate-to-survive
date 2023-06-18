#!/bin/bash

# This script generates an AUTHORS file based on the output of git log. It then commits and pushes the file to the repository.

REPO_OWNER="Csasaka19"
REPO_NAME="Roommate-to-survive"
AUTHORS_FILE="AUTHORS"

# Define the content of the AUTHORS file
AUTHORS_CONTENT=$(cat <<EOF
# Authors

Clive Sasaka <clivesasaka@gmail.com>
EOF
)

# Create the AUTHORS file locally
echo "$AUTHORS_CONTENT" > "$AUTHORS_FILE"

# Commit and push the AUTHORS file to the repository
git add "$AUTHORS_FILE"
git commit -m "Add AUTHORS file"
git push origin master

# Output success message
echo "AUTHORS file created and pushed to the repository."
