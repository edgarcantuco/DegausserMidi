import midiutil
import json, os

Folder = os.getcwd()

with open(f"{Folder}\\Temp.json", "r") as f:
    midiExport = json.loads(f.read())
MyMIDI = midiutil.MIDIFile(1)
Tempo = midiExport["Tempo"][0] * 10 * 1.19620253165 #The third number comes from the ratio of the expected length for a few songs.
MyMIDI.addTempo(0, 0, Tempo)
previousTempo = 1
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
        Tempo = midiExport["Tempo"][position] * 10 * 1.19620253165 
        
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

        if previousTempo != Tempo:
            MyMIDI.addTempo(0, position, Tempo)
        previousTempo = Tempo
        MyMIDI.addNote(track, channel, pitch, position, duration, volume)


with open(f"{Folder}\\EXPORTEDUNIQUENAME.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)