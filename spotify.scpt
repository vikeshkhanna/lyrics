#!/usr/bin/osascript

on getCurrentArtist()
  tell application "Spotify"
    set currentArtist to artist of current track as string
    return currentArtist
  end tell
end getCurrentArtist

on getCurrentTrack()
  tell application "Spotify"
    set currentTrack to name of current track as string
    return currentTrack
  end tell
end getCurrentTrack

set currentTrack to getCurrentTrack()
set currentArtist to getCurrentArtist()

return currentTrack & "\n" & currentArtist
