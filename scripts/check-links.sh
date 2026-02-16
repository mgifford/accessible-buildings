#!/bin/bash

# Ensure linkinator is installed
if ! npx linkinator --version > /dev/null 2>&1; then
  echo "Installing linkinator..."
  npm install --save-dev linkinator
fi

echo "Building site..."
bundle exec jekyll build

echo "Starting local server..."
npx serve _site -p 4001 &
SERVER_PID=$!

# Wait for server to start
sleep 5

echo "Running link validation..."
npx linkinator http://localhost:4001/accessible-buildings/ --recurse --silent --concurrency 10

EXIT_CODE=$?

# Kill server
kill $SERVER_PID

if [ $EXIT_CODE -eq 0 ]; then
  echo "✅ No broken links found!"
else
  echo "❌ Broken links detected."
fi

exit $EXIT_CODE
