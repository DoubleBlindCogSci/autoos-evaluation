from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS

_yQfAn= Factor("3yQfAn", [Level("XX4", 1), Level("wyf", 1), Level("2pcKqE! FL7e", 1), Level("OEnwYLpU", 1), Level("Kip>;x", 1), Level("PkY", 1), Level("kKQBbMoDy", 1), Level("RYyUHBNdcrYra", 10), Level("adPD7VChaem", 7), Level("RWthALArH1", 1)])
dqmk_= Factor("dqmk7", [Level("RQZ5[aV!N9btRm", 2), Level("%NcL", 1), Level("n]3Uq<AeizKA", 1), Level("wY)ph", 1), Level("ugu", 1), Level("xkeXsnDX", 1), Level("xxRs$f[", 1), Level("uDPJZY{$knh9", 1), Level("lt8", 2)])


design=[_yQfAn,dqmk_]
crossing=[_yQfAn,dqmk_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/9_2_0"))

### END
