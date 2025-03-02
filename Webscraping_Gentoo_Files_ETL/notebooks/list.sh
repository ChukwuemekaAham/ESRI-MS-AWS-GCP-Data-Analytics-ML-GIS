set -x

# list all text files in the current directory (excluding subdirectories) that have been modified in the last month

find . -maxdepth 1 -type f -name "*.txt" -newermt "$(date -d "1 month ago" +"%Y-%m-%d")"