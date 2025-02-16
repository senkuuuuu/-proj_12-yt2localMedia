<div align="center">
  <img src="resources/icons/logo.png" alt="logo">
</div>


Greetings, this is the documentation for YouTube to Local Media converter, a simple tool equipped with GUI that is created by senkuuu for the purpose of converting youtube videos into either Mp3 or Mp4

### 🖥️ Installation
<b>Option 1:</b> cloning the repository and making an exe file for the codebase in your own local device
Step 1: clone the repository
```bash
git clone https://github.com/senkuuuuu/-proj_12-yt2localMedia.git
```
Step 2: use pyinstaller to make exe file for the codebase
```bash
pyinstaller --onefile --name=YouTube2LocalMedia --icon=logo.ico --add-data "resources;resources" --windowed main.py
```
<b>NOTE:</b> for this to work you must have the following installed in your device
- ffmpeg
- python
- git
- this repository
- pygame
- pygame_gui
- pyinstalller

<b>Option 2:</b> download the already available exe file in the repository

---

### ⭐ Features
- can convert in either Mp4 or Mp3
- can convert in bundle such as converting whole Youtube Playlists
- has a sleek and simple GUI design for better user experience
---

### ⛓️ Limitations
- can't convert membership only videos
- can't convert age restricted videos
---

### ⚒️ Build
- backend uses yt-dlp and ffmpeg
- frontend uses pygame and pygame_gui
---

## 📝 To do
- codebase optimizations
- add cookie fetcher or authentication for yt-dlp to have access on age restricted videos
- bypass membership only videos



