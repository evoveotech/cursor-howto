#!/bin/bash
# Log all bash commands
# Hook: PostToolUse:Bash

COMMAND="$1"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
LOGFILE="$HOME/.cursor/bash-commands.log"

# Create log directory if it doesn't exist
mkdir -p "$(dirname "$LOGFILE")"

# Log the command
echo "[$TIMESTAMP] $COMMAND" >> "$LOGFILE"

# Optional: Log to system log as well
# logger -t "cursor-bash" "$COMMAND"

exit 0
