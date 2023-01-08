from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vpq= Factor("vpq", ["pgn","wuubg","ajwvvn","pntjpx","ozh","koznz","rhz"])
ovkmj= Factor("ovkmj", ["pgn","wuubg","ajwvvn","pntjpx","ozh","koznz","rhz"])
ezejn= Factor("ezejn", ["pgn","wuubg","ajwvvn","pntjpx","ozh","koznz","rhz"])
def is_kdrz_rsja(vpq, ovkmj, ezejn):
    return vpq != ovkmj or vpq != ezejn
def is_kdrz_zbfi(vpq, ovkmj, ezejn):
    return vpq == ovkmj and vpq == ezejn
kdrz= Factor("kdrz", [DerivedLevel("rsja", WithinTrial(is_kdrz_rsja, [vpq, ovkmj, ezejn])), DerivedLevel("zbfi", WithinTrial(is_kdrz_zbfi, [vpq, ovkmj, ezejn]))])

design=[vpq,ovkmj,ezejn, kdrz]
crossing=[kdrz]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_2_0"))

### END
