#!/usr/bin/bash

for file in 3-*; do
    echo "Copying $file to 4-${file#3-}"
	cp "$file" "4-${file#3-}"
done