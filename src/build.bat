cd venv\Main\Scripts

activate

cd ..\..\..

echo ############## Activated virtual environment ##############

pyinstaller midiextractor\midiextractor.py --dist bin/Debug --onefile --paths=.\venv\Main\Lib\site-packages --hidden-import=midiutil