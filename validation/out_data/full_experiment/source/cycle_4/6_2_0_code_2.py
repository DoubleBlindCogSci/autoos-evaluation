from sweetpea import *
import os
_dir = os.path.dirname(__file__)
### START
ewdwvi = Factor("ewdwvi", ["bvzbbc", "hlv"])
jnz = Factor("jnz", ["nmdg", "mook"])
pdu = Factor("pdu", ["bvzbbc", "hlv"])
zieg = Factor("zieg", ["nmdg", "mook"])
pqogoq = Factor("pqogoq", ["jhn", "kym"])
jck = Factor("jck", ["dghcps", "sfxk"])
def is_sni_lqrzx(zieg, jnz):
    return zieg == jnz
def is_sni_kcz(zieg, jnz):
    return not is_sni_lqrzx(zieg, jnz)
sni = Factor("sni", [DerivedLevel("lqrzx", WithinTrial(is_sni_lqrzx, [zieg, jnz])), DerivedLevel("kcz", WithinTrial(is_sni_kcz, [zieg, jnz]))])
def is_fodyo_glom(pdu, ewdwvi):
    return pdu == ewdwvi
def is_fodyo_tnxby(pdu, ewdwvi):
    return not is_fodyo_glom(pdu, ewdwvi)
fodyo = Factor("fodyo", [DerivedLevel("glom", WithinTrial(is_fodyo_glom, [pdu, ewdwvi])), DerivedLevel("tnxby", WithinTrial(is_fodyo_tnxby, [pdu, ewdwvi]))])
constraints = []
crossing = [jck, fodyo]

design=[ewdwvi,jnz,pdu,zieg,pqogoq,jck,sni,fodyo]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/6_2_0"))
