from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
zfe_zhLScy = Factor("zfe_zhLScy", ["QrTKMJ", "eNI", "JvGsraTvrPVEa7", "7]GrzT", "UHc", "HsOSlX", "vM^w#uO]Z", "gXP", "FrvfyWS", "sD^QgJpQXYSIVO", "F*^zIIoP*"])
Ub_Ej = Factor("Ub{Ej", ["UKxVXAAf[}f", "gfzf", "}XA", "OCnK)Xb", "cXf2LrxWIx#L:4", "IEi&AlOC*GC", "2cK0xXT", "d2NMsnbFW:CPE", "oqceZM{kA", "XUmQ"])
Yi__hWsP = Factor("Yi[[hWsP", ["%ahUE$kel", "f*f", "q(exG", "Wdiut~b]nOAa", "IgF*h4Qu", "4lSP_gqklv~j", "u$Kkvue9", "ejnWq?", "$T!SYP"])

design=[zfe_zhLScy,Ub_Ej,Yi__hWsP]
crossing=[zfe_zhLScy,Ub_Ej,Yi__hWsP]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/10_3_1"))

### END
