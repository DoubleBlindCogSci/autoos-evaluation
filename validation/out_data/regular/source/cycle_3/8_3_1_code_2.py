from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
auEoRjOoUoY = Factor("auEoRjOoUoY", [Level("lc7xSZt", 1), Level("rptBXcIX{M", 6), Level("Agyby:hOe", 1), Level("r2eaF1AWHv", 1), Level("YehMUHRE", 1), Level("%nRB", 1), Level("HXdfaZaJfs", 1), Level("B;~Bz&GsKu", 1)])
Y_i = Factor(" Y1i", [Level("H}JQlKD9xLU", 1), Level("x[IB", 1), Level("N}K~LzJ0f", 4), Level("oCs]", 1), Level("OMYRU", 1), Level("wrNxwn", 7), Level("ZaZsE", 1), Level("knK)m!qFc", 2), Level("Xhnf:npliL", 1)])
IDgrZeSAS_J = Factor("IDgrZeSAS6J", [Level("MinwE%Bkvxlm", 1), Level("QFzszNUNw*aAo", 1), Level("NPbIlW", 1), Level("FT~OSUKsC", 1), Level("dZ;Q", 5), Level("eHWbWphlpFg", 1), Level(" 0Oe", 1), Level("ZEmL ", 1)])

design=[auEoRjOoUoY,Y_i,IDgrZeSAS_J]
crossing=[auEoRjOoUoY,Y_i,IDgrZeSAS_J]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/8_3_1"))

### END
