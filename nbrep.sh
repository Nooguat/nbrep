#!/bin/bash
SESSION_DIR="$HOME/.sessions/"
WORKFILE="$SESSION_DIR$(date +"%m_%d")"
echo "$WORKFILE"
# Check for previous sessions files
# If prev file is found, warn user and add 7 days to the notes inside
