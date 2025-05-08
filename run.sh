#!/bin/sh

# Copy cron job to system crontab
cp /app/cronjob /etc/crontabs/root

# Start cron in foreground with log level 2
crond -f -l 2