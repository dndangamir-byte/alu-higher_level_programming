#!/bin/bash

ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"
GRADES_FILE="grades.csv"

if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
fi

TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
NEW_NAME="grades_${TIMESTAMP}.csv"

if [ -f "$GRADES_FILE" ]; then
    mv "$GRADES_FILE" "$ARCHIVE_DIR/$NEW_NAME"
    touch "$GRADES_FILE"
    echo "$(date): Archived $GRADES_FILE as $NEW_NAME" >> "$LOG_FILE"
    echo "Archived $GRADES_FILE -> $ARCHIVE_DIR/$NEW_NAME"
else
    echo "Error: $GRADES_FILE not found, nothing to archive."
fi
