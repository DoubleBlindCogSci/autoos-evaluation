from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
sLRSmrw_wog = Factor("sLRSmrw~wog", ["JusJqs2B2z", "BLQjTh", ";CElSNCU", "ZxEvrF"])
wEcCabp_bARhA = Factor("wEcCabp*bARhA", ["mHeP:rTHbt", "~efWGJ", "ZLXzE(0 T?q", "e{!VchU8", "HIXEsBPUdXuUON", "rwLHf"])
W_CkWTrgStL = Factor("W;CkWTrgStL", ["gMfiFPym~VMigr", "Q;FEmr?ErxTmy", "I[gQ", "#Me@PasrN"])

design=[sLRSmrw_wog,wEcCabp_bARhA,W_CkWTrgStL]
crossing=[sLRSmrw_wog,wEcCabp_bARhA,W_CkWTrgStL]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/4_3_1"))

### END
