from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
lMvkinK=Factor("sLRSmrw~wog",["JusJqs2B2z",'BLQjTh',';CElSNCU',"ZxEvrF"])
DTS5Sdi="mHeP:rTHbt"
DJ1VZX='rwLHf'
r5xFAZG1=[DTS5Sdi,"~efWGJ",'ZLXzE(0 T?q',"e{!VchU8",'HIXEsBPUdXuUON',DJ1VZX]
NBtS=Factor('wEcCabp*bARhA',r5xFAZG1)
l5tij5jE7i3=Factor("W;CkWTrgStL",['gMfiFPym~VMigr','Q;FEmr?ErxTmy',"I[gQ",'#Me@PasrN'])

### EXPERIMENT
design=[lMvkinK,NBtS,l5tij5jE7i3]
crossing=[lMvkinK,NBtS,l5tij5jE7i3]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/4_3_1"))
### END