import midiutil
import json, os

Folder = os.getcwd()

with open(f"{Folder}\\Temp.json", "r") as f:
    midiExport = json.loads(f.read())

Tempo = midiExport["Tempo"][0] * 10
# Tempo = 2200
MyMIDI = midiutil.MIDIFile(1)
MyMIDI.addTempo(0, 0, Tempo)

channelsAnalyzed = 0

for chnl in midiExport["Channels"]:
    track = 0

    for note in range(len(chnl["Notes"])):
        if chnl["Notes"][note]["state"] == 0:
            continue

        offset = 1
        channel = chnl["Notes"][note]["channel"]
        pitch = chnl["Notes"][note]["note"]
        volume = chnl["Notes"][note]["volume"]
        position = chnl["Notes"][note]["position"]

        if(chnl["Notes"][note]["state"] == 2):
            offset = 0
        else:
            while(note + offset <= len(chnl["Notes"]) - 1 and (chnl["Notes"][note + offset]["note"] != pitch or chnl["Notes"][note + offset]["state"] == 1)):
                offset += 1

            if(note + offset > len(chnl["Notes"]) - 1):
                offset = 0

        if offset > 0:
            duration = chnl["Notes"][note + offset]["position"] - position
        else:
            duration = 1

        MyMIDI.addNote(track, channel, pitch, position, duration, volume)


with open(f"{Folder}\\EXPORTEDUNIQUENAME.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)