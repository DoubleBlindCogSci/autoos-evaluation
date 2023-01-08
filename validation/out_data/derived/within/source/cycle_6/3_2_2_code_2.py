from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
khg = Factor("khg", ["das","nef","nzdsi","mlbqzo","qlnb","quq"])
jcs = Factor("jcs", ["kojxp","nnj","kbf","hrrluj","uftz","kwakqp","dbo"])
def is_ojj_qwzph(khg, jcs):
    return khg == "mlbqzo"
def is_ojj_adqp(khg, jcs):
    return khg != "mlbqzo" and jcs == "hrrluj"
def is_ojj_xxmgu(khg, jcs):
    return not (is_ojj_qwzph(khg) or is_ojj_adqp(khg, jcs))
ojj = Factor("ojj", [DerivedLevel("qwzph", WithinTrial(is_ojj_qwzph, [khg])), DerivedLevel("adqp", WithinTrial(is_ojj_adqp, [khg, jcs])), DerivedLevel("xxmgu", WithinTrial(is_ojj_xxmgu, [khg, jcs]))])

design=[khg,jcs,ojj]
crossing=[ojj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_2"))

### END