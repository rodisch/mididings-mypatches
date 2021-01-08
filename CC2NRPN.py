from mididings import *
"""
	Conversion of CC messages to NRPN for M-xx1 sound modules
"""

CC_Cutoff = 74
CC_Resonance = 71
CC_Attack = 73
CC_Release = 72
CC_Vrate = 76
CC_Vdepth = 77
CC_Vdelay = 78

DATA_MSB = 6
DATA_LSB = 38
NRPN_MSB = 99
NRPN_LSB = 98

CC2NRPN = [ 
	~Filter(CTRL),
	CtrlFilter([CC_Cutoff,CC_Resonance,CC_Attack,CC_Release,CC_Vrate,CC_Vdepth,CC_Vdelay]) %		
		CtrlSplit({		
			CC_Cutoff:  CtrlRange(CC_Cutoff, 0x0E,0x72) >> [Ctrl(NRPN_MSB,0x01),Ctrl(NRPN_LSB,0x20),Ctrl(DATA_MSB, EVENT_VALUE)],   
			CC_Resonance: CtrlRange(CC_Resonance, 0x0E,0x72) >> [Ctrl(NRPN_MSB,0x01),Ctrl(NRPN_LSB,0x21),Ctrl(DATA_MSB, EVENT_VALUE)], 	  
			CC_Attack:  CtrlRange(CC_Attack, 0x0E,0x72) >> [Ctrl(NRPN_MSB,0x01),Ctrl(NRPN_LSB,0x63),Ctrl(DATA_MSB, EVENT_VALUE)], 
			CC_Release: CtrlRange(CC_Release,0x0E,0x72) >> [Ctrl(NRPN_MSB,0x01),Ctrl(NRPN_LSB,0x66),Ctrl(DATA_MSB, EVENT_VALUE)],
			CC_Vrate:   CtrlRange(CC_Vrate,  0x0E,0x72) >> [Ctrl(NRPN_MSB,0x01),Ctrl(NRPN_LSB,0x08),Ctrl(DATA_MSB, EVENT_VALUE)],
			CC_Vdepth:  CtrlRange(CC_Vdepth, 0x0E,0x72) >> [Ctrl(NRPN_MSB,0x01),Ctrl(NRPN_LSB,0x09),Ctrl(DATA_MSB, EVENT_VALUE)],
			CC_Vdelay:  CtrlRange(CC_Vdelay, 0x0E,0x72) >> [Ctrl(NRPN_MSB,0x01),Ctrl(NRPN_LSB,0x0A),Ctrl(DATA_MSB, EVENT_VALUE)],
		})	
	
]
