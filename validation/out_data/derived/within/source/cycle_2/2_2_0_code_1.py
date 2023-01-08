from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
vpq = Factor("vpq", ["pgn","wuubg","ajwvvn","pntjpx","ozh","koznz","rhz"])
ovkmj = Factor("ovkmj", ["pgn","wuubg","ajwvvn","pntjpx","ozh","koznz","rhz"])
ezejn = Factor("ezejn", ["pgn","wuubg","ajwvvn","pntjpx","ozh","koznz","rhz"])
def vwa(vpq, ovkmj, ezejn):
    return vpq != ovkmj or vpq != ezejn
def sremcz(vpq, ovkmj, ezejn):
    return vpq == ovkmj and vpq == ezejn
fuwwh = DerivedLevel("rsja", WithinTrial(vwa, [vpq, ovkmj, ezejn]))
tbqvcc = DerivedLevel("zbfi", WithinTrial(sremcz, [vpq, ovkmj, ezejn]))
gvihfx = Factor("kdrz", [fuwwh, tbqvcc])

### EXPERIMENT
design=[vpq,ovkmj,ezejn,gvihfx]
crossing=[gvihfx]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/2_2_0"))
### END