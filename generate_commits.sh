#!/bin/bash

CSV_FILE="commits_amazingwallet.csv"
FILES=("backend/main.py" "backend/services/wallet.py" "backend/services/swap.py" "README.md")

if [ ! -f "$CSV_FILE" ]; then
  echo "Файл $CSV_FILE не найден!"
  exit 1
fi

touch dummy.txt
git add .

tail -n +2 "$CSV_FILE" | while IFS=, read -r date message; do
  file=${FILES[$RANDOM % ${#FILES[@]}]}
  echo "# commit" >> "$file"
  git add .
  GIT_AUTHOR_DATE="$date" GIT_COMMITTER_DATE="$date"   git commit -m "$message"
done
