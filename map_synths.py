#!/usr/bin/python3
"""
   - Midi message routing
   - CC to NRPN conversion for Roland M-xx1 soundmodules
   - CC mapping, sustain for Volca FM
   - Sustain for Circuit
   - Note to PC mapping fur Circuit drums
"""

#--- mididings preliminaries
from mididings import *
from mididings.extra.inotify import AutoRestart

hook(
	AutoRestart(modules=True) 
)

#--- port definitions
inports = [('in_map_synths',)]  # add virtual input port

outports= [
	('to_SE1', 'MIDI4x4:2'), 
	('to_OC1', 'MIDI4x4:2'),   # midi daisy chained	
	('to_VOLCA','MIDI4x4:3'),	# midi daisy chained to Neutron			
	('to_NEUTRON','MIDI4x4:3'),		
	('to_CIRCUIT','Circuit:0'),		
]

config(
	client_name='map_synths', 
	backend='alsa',		
	in_ports=inports,	
	out_ports= outports,		
	start_delay=0.5
)

#-- Define channelnumbers for filter
Ch_CIRCUITDR = 10 # drums
Ch_CIRCUIT1 = 11  # synth 1, will be mapped to ch=1 
Ch_CIRCUIT2 = 12  # synth 2, will be mapped to ch=2

Ch_SE1 = 13
Ch_OC1 = 14
Ch_VOLCA = 15
Ch_NEUTRON = 16

#-- Output-patches
from CC2NRPN import *  # output converter for Roland Soundexpansions
from EV2VOLCAFM109 import * # output converter for Volca FM
from CircuitDrums import * # defines NOTE2DRUM

CC_Vol = 7
CC_Pan = 10
CC_Hold = 64

outp_CIRCUIT1 = [
	CtrlFilter(CC_Vol) >> CtrlMap(CC_Vol, 12) >> Output('to_CIRCUIT',16),
	CtrlFilter(CC_Pan) >> CtrlMap(CC_Pan, 117) >> Output('to_CIRCUIT',16),
	PedalToNoteoff(ctrl=CC_Hold) >> Output('to_CIRCUIT',1)  # Fake Sustain
]

outp_CIRCUIT2 = [
	CtrlFilter(CC_Vol) >> CtrlMap(CC_Vol, 14) >> Output('to_CIRCUIT',16),
	CtrlFilter(CC_Pan) >> CtrlMap(CC_Pan, 118) >> Output('to_CIRCUIT',16),
	PedalToNoteoff(ctrl=CC_Hold) >> Output('to_CIRCUIT',2) # Fake Sustain
]
outp_CIRCUITDR = NOTE2DRUM >> Output('to_CIRCUIT',10) # Drum/Sample channel

outp_SE1  = CC2NRPN >> Output('to_SE1',1)
outp_OC1  = CC2NRPN >> Output('to_OC1',2)

outp_VOLCAFM = EV2VOLCAFM109 >> Output('to_VOLCA',1)  
outp_NEUTRON = Output('to_NEUTRON',2)


#-- Main patch
run([
		ChannelSplit({	
			Ch_CIRCUIT1: outp_CIRCUIT1,
			Ch_CIRCUIT2: outp_CIRCUIT2,	
			Ch_CIRCUITDR: outp_CIRCUITDR,									 
			Ch_SE1: outp_SE1,
			Ch_OC1: outp_OC1,				
			Ch_VOLCA: outp_VOLCAFM,
			Ch_NEUTRON: outp_NEUTRON,		   
			}),
		
		Filter(SYSRT_CLOCK) >> [outp_VOLCAFM, outp_NEUTRON, outp_CIRCUITDR], # midi clock events, runs permanent			
		Filter(SYSRT_START, SYSRT_CONTINUE, SYSRT_STOP) >> [outp_CIRCUITDR], # sync start/stop to FA-sequencer
		Filter(SYSCM_SONGPOS) >> [outp_CIRCUITDR], # sync songposition
	]
)
