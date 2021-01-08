from mididings import *
from mididings.extra import *
"""
Mapping of notes to Drum patch+key on the Novation Circuit

"""

# Circuit CCs
CC_Patch1 = 8
CC_Patch2 = 18
CC_Patch3 = 44
CC_Patch4 = 50

NOTE2DRUM = [
		~Filter(NOTE),
		
		Filter(NOTE) % [
		KeyFilter(notes=[35]) % [Ctrl(CC_Patch1,8), Key(60)], # Bass	
		KeyFilter(notes=[36]) % [Ctrl(CC_Patch1,0), Key(60)],		
		KeyFilter(notes=[37]) % [Ctrl(CC_Patch1,16), Key(60)],		
				
		KeyFilter(notes=[38]) % [Ctrl(CC_Patch2, 1), Key(62)], # Snare	
		KeyFilter(notes=[40]) % [Ctrl(CC_Patch2, 9), Key(62)], 
		
		KeyFilter(notes=[42]) % [Ctrl(CC_Patch3,10), Key(64)], # HiHat
		KeyFilter(notes=[44]) % [Ctrl(CC_Patch3,2), Key(64)], 
		KeyFilter(notes=[46]) % [Ctrl(CC_Patch3,3), Key(64)], 
		
		KeyFilter(notes=[43]) % [Ctrl(CC_Patch4,4), Key(65)],  # Toms
		KeyFilter(notes=[45]) % [Ctrl(CC_Patch4,5), Key(65)], 
		KeyFilter(notes=[47]) % [Ctrl(CC_Patch4,6), Key(65)], 
		KeyFilter(notes=[48]) % [Ctrl(CC_Patch4,7), Key(65)],  # Tamburin
		]
]

