from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
JPEeK_bkk= Factor("JPEeK bkk", [Level("xekdk!qo1KXd", 1), Level("uoRn", 1), Level("]s;LlOhKDh4nO", 1), Level("dg[KbbqeYb", 6), Level("JOPDSRc", 1)])
FYdEXnj_hvR_= Factor("FYdEXnj_hvR0", [Level("lvOntGk", 3), Level("rPHWnDpjUUj", 1), Level("yOX ", 1), Level("w4Hraly8rOCOt", 1), Level("Jplf&syKU", 1)])
AmUdvwcYmOEu= Factor("AmUdvwcYmOEu", [Level("^ucgbDZUF8", 1), Level("Wax*Rn", 6), Level("jPrdx3>eh", 1), Level("LCxxI[gA", 1), Level("g]DoKdSY", 7), Level("UO>aKUuZXspP)F", 1)])

design=[JPEeK_bkk,FYdEXnj_hvR_,AmUdvwcYmOEu]
crossing=[JPEeK_bkk,FYdEXnj_hvR_,AmUdvwcYmOEu]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block, experiment, os.path.join(_dir, "out_code_2/5_3_0"))

### END
