# Eja — Simple Age Calculator

Eja is a small, friendly age calculator app built with Kivy and KivyMD. It's designed to be lightweight and easy to use — pick a date of birth and Eja tells you your age in years  with a clean Material-style UI.

This README will help you get the app running locally, package it for Android, and understand the project's structure.

## Features

- Simple, minimal Material Design UI using KivyMD
- Select a date of birth with a date picker
- Calculates age in years
- Lightweight and easy to extend

## Screenshots

![Eja Main Screen](screenshots/Screenshot_20250820-120725.png) 
![Eja Date Picker](screenshots/Screenshot_20250820-120725.png)


## Requirements

- Python 3.8+ (recommended)
- Kivy (tested with 2.x)
- KivyMD
- pip

For packaging to Android:
- Buildozer (Linux recommended)
- Android SDK / NDK (installed via Buildozer)

## Installation (Development)

1. Clone the repository:
   git clone https://github.com/nathankuipa25/eja.git
   cd eja

2. Create and activate a virtual environment (recommended):
   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .venv\Scripts\activate     # Windows (PowerShell: .venv\Scripts\Activate.ps1)

3. Install dependencies:
   pip install --upgrade pip
   pip install kivy kivymd

   If you have a `requirements.txt` in the repo:
   pip install -r requirements.txt

4. Run the app:
   python main.py

## Usage

- Launch the app.
- Tap the date picker and choose a date of birth.
- Tap "GET AGE" (or similar) to display your age in years. 
- Extend the UI or logic in the `main.py` as needed.

## Packaging for Android (Buildozer)

1. Install Buildozer (Linux):
   pip install buildozer
   sudo apt install -y build-essential git python3-pip python3-virtualenv zip unzip openjdk-8-jdk

2. Initialize a Buildozer spec:
   buildozer init

3. Edit `buildozer.spec`:
   - Set `package.name`, `package.domain`
   - Add required Python modules to `requirements = kivy,kivymd,python-dateutil` (if used)
   - Configure icons, permissions, etc.

4. Build and deploy:
   buildozer android debug deploy run

See Buildozer docs for details: https://github.com/kivy/buildozer

## Project Structure 

- main.py — entry point for the app
- /screenshots — images and screenshots
- requirements.txt — Python deps 
- buildozer.spec — Buildozer configuration 
- presplash.png
- icon.png


## Contributing

Contributions are welcome! 
Suggested ways to contribute:

- Bug reports and feature requests via Issues
- Pull requests for fixes, improvements, or new features
- Add translations

When submitting a PR:
- Keep changes small and focused
- Include screenshots if UI is changed
- Add tests or manual verification steps if relevant

## Known Issues & TODO

- Accessibility improvements (screen reader hints)
- Input validation UX could be improved for invalid dates
- Add localization / multi-language support
- Add option to show total days or weeks lived

## License

This project is provided under the MIT License. See the LICENSE file for details.

## Acknowledgements

- Built with Kivy — https://kivy.org
- UI components from KivyMD — https://kivymd.readthedocs.io

## Social links

- githu b - https://github.com/nathankuipa25/

