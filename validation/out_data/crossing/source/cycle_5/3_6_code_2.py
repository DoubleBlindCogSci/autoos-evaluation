from sweetpea import *
import os
_dir=os.path.dirname(__file__)
wej = Factor("wej", ["bevf", "eaklvp"])
buxe = Factor("buxe", ["jdj", "vqqf"])
aqzlz = Factor("aqzlz", ["wtwz", "fqlis"])
ucag = Factor("ucag", ["wff", "dsudg"])
zwnt = Factor("zwnt", ["uljiaw", "mfz"])
vvgt = Factor("vvgt", ["hvvh", "oyyby"])
jldenz = Factor("jldenz", ["jvi", "oniker"])
fzox = Factor("fzox", ["nyo", "ghbz"])
kptit = Factor("kptit", ["jmsy", "qnh"])
constraints = []
crossing = [[wej, buxe, aqzlz, ucag], [zwnt, vvgt, jldenz, fzox, kptit]]


design=[wej,buxe,aqzlz,ucag,zwnt,vvgt,jldenz,fzox,kptit]
### APPENDIX
block=MultiCrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_6"))

### END