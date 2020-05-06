# DOTA 2 Auto Accept

This script will help you poop without worry!

## Installation

Run ```install.py``` or go to install folder if you are on Windows run ```install.bat``` if you are on Linux (Arch-based) run ```install.bash```

## Run

Windows ```run.bat```
Linux ```run.bash```

## Config

Because everyone has different screen size. I recommend that you take the screenshot of your own, crop the accept button, and replace accept-en.png.

**CHECK_INTERVAL** - time (secs) between each search.
**CLICK_INTERVAL**  - time (secs) between each click.
**NUM_OF_CLICKS** - number of clicking times.
**CONFIDENCE** - (0-1) higher = more pixel-perfect.
**GRAYSCALE** - (True/False) changing not recommended.
**PATH_TO_IMG** - path to image file.

## Dependencies

PyAutoGUI

```bash
pip install pyautogui
```

OpenCV

```bash
pip install opencv_python
```

Numpy

```bash
pip install numpy
```

Pyyaml

```bash
pip install pyyaml
```

## Author

**pannxe** - original work - [Github](https://github.com/pannxe)

## License

GNU General Public License v3.0
