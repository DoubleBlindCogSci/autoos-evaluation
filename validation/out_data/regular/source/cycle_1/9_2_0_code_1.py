from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
bIwD='kKQBbMoDy'
gGW1N=Factor("3yQfAn",['XX4',"wyf","2pcKqE! FL7e","OEnwYLpU",Level('Kip>;x',1),'PkY',bIwD,Level("RYyUHBNdcrYra",10),Level('adPD7VChaem',7),"RWthALArH1"])
nvfEcQK=Factor("dqmk7",[Level('RQZ5[aV!N9btRm',2),'%NcL','n]3Uq<AeizKA','wY)ph','ugu',"xkeXsnDX","xxRs$f[","uDPJZY{$knh9",Level("lt8",2)])

### EXPERIMENT
design=[gGW1N,nvfEcQK]
crossing=[gGW1N,nvfEcQK]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_1/9_2_0"))
### END