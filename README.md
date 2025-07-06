<div align="center">
  <img src="resources/icons/logo.png" alt="logo">
</div>


Greetings, this is the documentation for YouTube to Local Media converter, a simple tool equipped with GUI that is created by senkuuu for the purpose of converting youtube videos into either Mp3 or Mp4

### 🖥️ Installation
Step 1: clone the repository
```bash
git clone https://github.com/senkuuuuu/-proj_12-yt2localMedia.git
```
Step 2: Install dependencies, you can make a virtual environment if you want to
```bash
pip install -r requirements.txt
```
Step 3: use pyinstaller to make exe file for the codebase
```bash
pyinstaller --onefile --name=YouTube2LocalMedia --icon=logo.ico --add-data "resources;resources" --windowed main.py
```

<b>NOTE:</b> for this to work you must have the following installed in your device
- ffmpeg
- python
- git
- this repository

---

### ⭐ Features
- can convert in either Mp4 or Mp3
- can convert in bundle such as converting whole Youtube Playlists
- has a sleek and simple GUI design for better user experience
- can download long videos quickly
---

### ⛓️ Limitations
- can't convert membership only videos
- can't convert age restricted videos
- not cross platform only works on windows
---

### ⚒️ Build
- backend uses yt-dlp and ffmpeg
- frontend uses pygame and pygame_gui
- packaged using pyinstaller
---

### 💡 Keep in mind
- always make sure that the app is up-to-date to the latest version of yt-dlp, otherwise you might encounter unexpocted errors.
---

## 📝 To do
- add cookie fetcher or authentication for yt-dlp to have access on age restricted videos
- bypass membership only videos
- add auto-update for the yt-dlp module
- allow for the ffmpeg to be packaged along with the app
---

## 👀 Preview
<div align="center">
  <img src="preview\preview_1.png" alt="logo">
  <img src="preview\preview_2.png" alt="logo">
  <img src="preview\preview_3.png" alt="logo">
  <img src="preview\preview_4.png" alt="logo">
</div>



