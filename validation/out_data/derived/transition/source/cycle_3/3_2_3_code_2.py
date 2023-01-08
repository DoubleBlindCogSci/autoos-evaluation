from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
imgt = Factor("imgt", ["auik","ykvp","cnzw","ynk","cuzq","fwhui","rcuu","cdjwaz"])
ffi = Factor("ffi", ["sqx","dzsh","vgg","qnoc","pwdesb","wpsnra","nmsxqv","mbn"])
def is_sfhdj_kssc(imgt, ffi):
    return imgt[-1] == "rcuu" and ffi[0] != "mbn"
def is_sfhdj_zaui(imgt, ffi):
    return imgt[-1] != "rcuu" and ffi[0] == "mbn"
def is_sfhdj_nqwa(imgt, ffi):
    return not (is_sfhdj_kssc(imgt, ffi) or is_sfhdj_zaui(imgt, ffi))
sfhdj= Factor("sfhdj", [DerivedLevel("kssc", Transition(is_sfhdj_kssc, [imgt, ffi])), DerivedLevel("zaui", Transition(is_sfhdj_zaui, [imgt, ffi])), DerivedLevel("nqwa", Transition(is_sfhdj_nqwa, [imgt, ffi]))])

design=[imgt,ffi,sfhdj]
crossing=[sfhdj]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_2_3"))

### END
