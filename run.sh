#!/bin/bash
SpotifyResponse=`osascript spotify.scpt`

arr=()
while read -r line; do
  arr+=("$line")
done <<< "$SpotifyResponse"

songName=${arr[0]}
artistName=${arr[1]}

python fetch.py "$songName" "$artistName"
