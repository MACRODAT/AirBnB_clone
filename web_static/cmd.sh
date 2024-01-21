#!/usr/bin/bash

for file in 4-*; do
    echo "Copying $file to 5-${file#4-}"
	cp -n "$file" "5-${file#4-}"
done