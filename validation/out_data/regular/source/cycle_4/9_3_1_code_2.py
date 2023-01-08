from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
qcAJmQDvCchZy = Factor("qcAJmQDvCchZy", ["oBb?PyBrQwz", "YzVWSjq6LBaQ", "FwqmKR6UlJ", "YDFmv", "Cvzw F$[N^", ">nRhVopm:V", "TCwsYOzc", "1bubPsYDrU", "gC}zo("])
w_biplTVb__ = Factor("w3biplTVb*3", [Level("EnQLTyc1cIhZVR", 1), Level("Gmw6NG]tuy", 1), Level("AnHg8p;_ETEvI", 3), Level("Q%jhzDfi", 1), Level("dvFS FysnTvssH", 1), Level("fuHMjSx", 1), Level("vqmam84?ywV", 1), Level("Inkdkmy", 1), Level("C<Q&SVzkz", 1), Level("D[KG&E)$", 1)])

design=[qcAJmQDvCchZy,w_biplTVb__]
crossing=[qcAJmQDvCchZy,w_biplTVb__]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_3_1"))

### END
