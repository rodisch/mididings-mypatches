# mididings-mypatches
Mididings patches for my multi-synth/multi-keyboard setup

Main script: map_synths.py

All data from the virtual input 'input_map_synths' is processed. The different synths are adressed by their specific midi channels and then mapped to different outputs. I am using a USB to 4xMidi interface. 
'Input_map_synths' is connected via aconnect to one USB-output of a MidiHUB (see http://blokas.io).

The main-script imports several subscripts to do the data mapping:
- CC to NRPN for the old ROland gear (M-SE1, M-OC2)
- Note to drum mapping for the nocation Circuit
- Some controller mapping and sustaint for the Volca FM
