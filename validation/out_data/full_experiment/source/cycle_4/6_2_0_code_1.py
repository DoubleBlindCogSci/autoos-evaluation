from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### START
ewdwvi = Factor("ewdwvi", ["bvzbbc", "hlv"])
jnz = Factor("jnz", ["nmdg", "mook"])
pdu = Factor("pdu", ["bvzbbc", "hlv"])
zieg = Factor("zieg", ["nmdg", "mook"])
pqogoq = Factor("pqogoq", ["jhn", "kym"])
jck = Factor("jck", ["dghcps", "sfxk"])
def oyty (zieg, jnz):
    return zieg == jnz
def wnszvu (zieg, jnz):
    return not oyty(zieg, jnz)
sni = Factor("sni", [DerivedLevel("lqrzx", WithinTrial(oyty, [zieg, jnz])), DerivedLevel("kcz", WithinTrial(wnszvu, [zieg, jnz]))])
def zwhy (pdu, ewdwvi):
    return pdu == ewdwvi
def szs (pdu, ewdwvi):
    return not zwhy(pdu, ewdwvi)
fodyo = Factor("fodyo", [DerivedLevel("glom", WithinTrial(zwhy, [pdu, ewdwvi])), DerivedLevel("tnxby", WithinTrial(szs, [pdu, ewdwvi]))])
design=[sni,fodyo,ewdwvi,jnz,pdu,zieg,pqogoq,jck]
constraints=[]
crossing=[jck,fodyo]
block=CrossBlock(design,crossing,constraints)
### END
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/6_2_0"))
