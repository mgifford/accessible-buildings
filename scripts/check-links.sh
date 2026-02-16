#!/bin/bash

# Ensure linkinator is installed
if ! npx linkinator --version > /dev/null 2>&1; then
  echo "Installing linkinator..."
  npm install --save-dev linkinator
fi

echo "Building site..."
rm -rf _site
bundle exec jekyll build

echo "Structuring _site for baseurl testing..."
rm -rf _site_final
mkdir -p _site_final/accessible-buildings
cp -R _site/* _site_final/accessible-buildings/

echo "Starting local server..."
npx serve _site_final -p 4001 &
SERVER_PID=$!

# Wait for server to start
sleep 5

echo "Running link validation..."
npx linkinator http://localhost:4001/accessible-buildings/ --recurse --silent --concurrency 10

EXIT_CODE=$?

# Kill server
kill $SERVER_PID
rm -rf _site_final

if [ $EXIT_CODE -eq 0 ]; then
  echo "✅ No broken links found!"
else
  echo "❌ Broken links detected."
fi

exit $EXIT_CODE
