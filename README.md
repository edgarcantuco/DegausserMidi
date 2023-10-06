# Degausser Midi
Save editor for Daigasso! Band Brothers P.
Derived from the work by [AdibSurani](https://github.com/AdibSurani) and [wangyu](https://github.com/wangyu-).

This software comes in two formats:
- In the `src` folder is the C# code for _Degausser_, intended to run on Windows. This version is able to import, export, convert .bdx and .bin files, as well as play and export songs. This has to be used in conjunction with an extdata dumping/restoring tool.
- In the `degausser3ds` folder is C code for the homebrew _degausser3ds_. While it's recommended to use [wangyu-'s upgraded version](https://github.com/wangyu-/Degausser/releases/latest), this version is only able to import all songs in a fixed directory, or export all songs to a fixed directory. This is able to import/export directly from/to extdata.

# Build midi Extractor (Python)
The Degausser software for Windows features the ability to export songs as midi files. To build the midi Extractor, run the following commands from src.

```
cd venv\Main\Scripts
activate
cd ..\..\..
pyinstaller midiextractor\midiextractor.py --dist bin/Debug --onefile --paths=.\venv\Main\Lib\site-packages --hidden-import=midiutil
```
