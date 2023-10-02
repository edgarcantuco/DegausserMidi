# Degausser
Save editor for Daigasso! Band Brothers P. There are currently two flavours:

1. In the `src` folder is the C# code for _Degausser_, intended to run on Windows. This version is able to import, export, convert .bdx and .bin files, as well as play the songs. This has to be used in conjunction with an extdata dumping/restoring tool.
2. In the `degausser3ds` folder is C code for the homebrew _degausser3ds_. This version is only able to import all songs in a fixed directory, or export all songs to a fixed directory. This is able to import/export directly from/to extdata.

In the future we might use this space to discuss some of the file formats, but otherwise feel free to check out the Releases.


# Build python extractor

To build the python extractor, run the next commands on src.

```
cd venv\Main\Scripts

activate

cd ..\..\..

pyinstaller midiextractor\midiextractor.py --dist bin/Debug --onefile --paths=.\venv\Main\Lib\site-packages --hidden-import=midiutil
```
