#!/bin/bash

# Arguments
COMMAND=$1
MAX_RETRIES=${2:-3}
SLEEP_TIME=${3:-5}

# Retry logic
for ((i=1; i<=MAX_RETRIES; i++)); do
    eval "$COMMAND" && break || {
        if [[ $i -lt MAX_RETRIES ]]; then
            echo "Command failed. Retrying in $SLEEP_TIME seconds..."
            sleep $SLEEP_TIME;
        else
            echo "Command failed after $i attempts."
            exit 1;
        fi
    }
done
