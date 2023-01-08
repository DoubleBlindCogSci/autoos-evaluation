from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
jic = Factor("jic", ["mlAZbtzOD", "nKr*#Y", "B&~T9GDSZ", "B0xjrSIfn", "1AAewslQoHsdI", "sxxrZ1aFrEGi"])
vtg_aXID = Factor("vtg:aXID", ["ENJX~vDmHu", "uz~wzT a", "rwi%jIzEJ", "VyoHmOmf", "QmEkjZRr z^dE", "DpKtQyJNUiyDIY", "OoV7f~l<"])
a_fUekLOWtD = Factor("a&fUekLOWtD", [Level("tSLOOQGs5 ", 4), Level("KoZ", 1), Level("#dM1Eo7EPc", 1), Level("elgmRMLGeY!kw@", 1), Level(" owJn", 1), Level("osHHgtGdGLbG", 1), Level("JLMygcjPqDTz", 2)])

design=[jic,vtg_aXID,a_fUekLOWtD]
crossing=[jic,vtg_aXID,a_fUekLOWtD]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_3_1"))

### END
