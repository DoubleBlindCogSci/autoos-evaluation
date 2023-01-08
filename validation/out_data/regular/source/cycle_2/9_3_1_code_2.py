from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
ozndzP_R = Factor("ozndzP~R", [Level("#buNacuy", 1), Level("YNiQCbujIRl", 6), Level(">Ab", 1), Level("lH]tGfO*wAk8kQ", 1), Level("ZVS:", 2), Level("Splvlo", 1), Level("|a*hCPDN", 1), Level("cER", 1), Level("bhxspM&TUbgo", 1)])
aIRsfp_r_FH = Factor("aIRsfp;r0FH", [Level("DUigxkR]3ACJW", 1), Level("SOVSBYqSjXUi", 1), Level(":hZc2gJoUG", 1), Level("Elq", 1), Level("j;E", 1), Level("]RuF>JdytuDGZ", 1), Level("!izZ3EwlEi", 1), Level("pgG", 1), Level("pAp", 1), Level("uOuNm#KYEOg7KR", 1)])
rrCuzg = Factor("rrCuzg", [Level("VtoEgmqSUjXZo", 1), Level("ibii8kH", 3), Level("l3f", 1), Level("s2uX", 10), Level("swRxu|NZbmy&c", 1), Level("YMQ#", 1), Level("GlrG", 1), Level("oJneQnjMU4#f", 1), Level("I%KCddz BO", 1)])

design=[ozndzP_R,aIRsfp_r_FH,rrCuzg]
crossing=[ozndzP_R,aIRsfp_r_FH,rrCuzg]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_3_1"))

### END
