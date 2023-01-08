from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zvlBGwUXPLT=['_Isb%q',"34UbHOC","AcleorENEnWKH","HXwO<pkYTBZns"]
eaPgT=Factor('IoojsU',['IQxnzYxWdit','y fmBT}gqxsme',"xiDCDA>rI",zvlBGwUXPLT[3],'uMfQhhFTmMN',"s7G",'_lJKNI','9zX3A]zV',"fOU"])

### EXPERIMENT
design=[eaPgT]
crossing=[eaPgT]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/8_1_1"))
### END