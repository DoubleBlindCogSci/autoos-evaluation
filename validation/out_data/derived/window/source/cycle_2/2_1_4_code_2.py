from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zksmic= Factor("zksmic", ["jcy","plf","ugmriq","xezfoh","erjf","figvtg","ztgmq"])
def is_dhxvi_idwpav(zksmic):
    return zksmic[-3] != "erjf" and zksmic[-1] == "plf"
def is_dhxvi_ihula(zksmic):
    return not is_dhxvi_idwpav(zksmic)
dhxvi= Factor("dhxvi", [DerivedLevel("idwpav", Window(is_dhxvi_idwpav, [zksmic], 4, 1)), DerivedLevel("ihula", Window(is_dhxvi_ihula, [zksmic], 4, 1))])

design=[zksmic, dhxvi]
crossing=[dhxvi]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/2_1_4"))

### END
