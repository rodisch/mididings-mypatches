from mididings import *
from mididings.extra import *
"""
	Conversion of key velocity to CC41 message for Volca FM (firmware 1.04),
	Conversion hold pedal to note-off
	Mapping of generic CCs to Volca CCs
"""
# Midi in CCs
CC_Modulation = 1
CC_Hold = 64
CC_Cutoff = 74
CC_Resonance = 71
CC_Attack = 73
CC_Release = 72
CC_Vrate = 76
CC_Vdepth = 77
CC_Vdelay = 78
CC_PortOnoff = 65
CC_PortTime = 5

# Volca out CCs
CC_Transpose = 40
CC_Velocity = 41
CC_ModAttack = 42
CC_ModDecay = 43
CC_CrAttack = 44
CC_CrDecay = 45
CC_LFOrate = 46
CC_LFOdepth = 47
CC_Algo = 48
CC_ArpType = 49
CC_ArpDiv = 50


EV2VOLCAFM = [ 	
	~Filter(CTRL, NOTE),
	
	PedalToNoteoff(ctrl=CC_Hold) >> [			
		Filter(NOTEON) % [
			Ctrl(CC_Velocity, EVENT_VELOCITY),
			Pass()
		],
		
		CtrlFilter([CC_Cutoff,CC_Resonance,CC_Attack,CC_Release,CC_Vrate,CC_Vdepth,CC_Modulation, CC_PortOnoff, CC_PortTime]) %		
			CtrlSplit({	
				CC_Cutoff:  Ctrl(CC_ModAttack, EVENT_VALUE),
				CC_Resonance:  Ctrl(CC_ModDecay, EVENT_VALUE), 				  
				CC_Attack:  Ctrl(CC_CrAttack, EVENT_VALUE), 
				CC_Release: Ctrl(CC_CrDecay, EVENT_VALUE), 			
				
				CC_Vrate:   Ctrl(CC_LFOrate, EVENT_VALUE),
				CC_Vdepth:  Ctrl(CC_LFOdepth, EVENT_VALUE),
				CC_Modulation:  CtrlRange(CC_Modulation, 0x00,0x40) >> Ctrl(CC_LFOdepth, EVENT_VALUE),	
				CC_PortOnoff: Ctrl(CC_ArpType, EVENT_VALUE),
				CC_PortTime: Ctrl(CC_ArpDiv, EVENT_VALUE),
			})	
	],
			
			
]
