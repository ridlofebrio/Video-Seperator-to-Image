# Video Separator

## Description
**Video Separator** is a Python tool designed to extract individual frames from videos at a rate of 1 frame per second. The extracted frames are saved as JPEG images in an organized directory structure.

## Features
- Extract frames at a rate of **1 frame per second**.
- Process **single video files** or **entire directories**.
- Support for multiple video formats: **.mp4, .avi, .mkv, .mov**.
- Organizes output by creating a separate folder for each video.
- Provides **performance timing** and **detailed logging**.

## Requirements
- Python **3.6+**
- OpenCV
- NumPy

## Installation
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd video-separator
   ```
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place your video files inside the `Video/` directory.
2. Run the script:
   ```bash
   python pemisah.py
   ```
3. Extracted frames will be saved in the `Foto/` directory, with each video's frames stored in a separate subfolder.

## How It Works
The script utilizes **OpenCV** to:
- Read video files and calculate properties such as FPS and duration.
- Extract frames at precise **1-second intervals**.
- Save each frame as a JPEG image using the naming convention:
  ```
  {video_name}_sec{second_number}.jpg
  ```

## Project Structure
```
video-separator/
│── Video/              # Directory for input video files
│── Foto/               # Directory where extracted frames are stored
│── pemisah.py          # Main script for processing videos
│── requirements.txt    # Required dependencies
│── README.md           # Project documentation
```

## Notes
- The script processes all videos in the `Video/` directory by default.
- It also specifically processes `Video/pal.mp4` if present.
- Modify the `main()` function in **pemisah.py** to change input/output paths or processing behavior.

## License
This project is **open-source** and free to use or modify.

---
Developed with ❤️ using Python.

