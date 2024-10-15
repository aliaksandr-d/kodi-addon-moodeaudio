# MoodeAudio Kodi Addon
This Kodi addon allows you to control **MoodeAudio** via its HTTP API. With this addon, you can manage radio stations, play music albums, control playback, and view the current status of your MoodeAudio player—all from within Kodi.

## Features
- **Radio Station Control:** Browse, select, and play radio stations available on MoodeAudio.
- **Music Library:** View and play albums and tracks from your MoodeAudio music library.
- **Playback Control:** Start, stop, pause, and resume playback.
- **Current Player Status:** View the current status of playback, including volume, track info, and more.

## Installation
1. Clone this repository to your Kodi addons directory or create a zip file to install it via Kodi.

```bash
git clone https://github.com/aliaksandr-d/pkodi-addon-moodeaudio.git
```
The typical path for Kodi addons is:

- **Windows:** `C:\Users\<YourUserName>\AppData\Roaming\Kodi\addons`
- **Linux:** `~/.kodi/addons`
- **macOS:** `/Users/<YourUserName>/Library/Application Support/Kodi/addons`
2. Alternatively, package the addon as a `.zip` file, then install it via Kodi's "Install from zip file" option under **Add-ons > Install from zip file**.

## Usage
1. Go to **Add-ons** in Kodi.
2. Select **MoodeAudio Player** from your Music Add-ons list.
3. Configure the **MoodeAudio Host** by going to the addon settings and entering the IP address of your MoodeAudio device (e.g., `192.168.0.8`).
4. Navigate through the available options:
- **Radio:** List of radio stations available on MoodeAudio.
- **Music Library:** Your music collection stored in MoodeAudio.
- **Playback Control:** Play, pause, or stop the current track.

## Configuration
### Setting the MoodeAudio Host

- In Kodi, navigate to **Add-ons > My Add-ons > Music Add-ons > MoodeAudio Player**.
- Open **Settings** and input the IP address of your MoodeAudio device in the **MoodeAudio Host** field (e.g., `192.168.0.8`).

## API Overview
The addon interacts with MoodeAudio through the following API endpoints:

- Get Radio Stations: `/command/radio.php?cmd=get_stations`
- Get Music Library: `/command/music-library.php?cmd=load_library`
- Get Player Status: `/engine-mpd.php`
- Playback Control:
  - `/engine-mpd.php?state=play`
  - `/engine-mpd.php?state=stop`
  - `/engine-mpd.php?state=pause`
- Play Radio Station: `/command/queue.php?cmd=clear_play_item`
- Play Music Tracks: `/command/queue.php?cmd=clear_play_group`

## Dependencies
Kodi: Version 19 or later
Python: 3.x (Kodi plugin API)


## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Feel free to contribute by submitting issues or pull requests. Any improvements, such as new features or optimizations, are welcome.

