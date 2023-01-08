from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### DERIVED FACTORS
iiyrcc = Factor("iiyrcc", ["ifoweu","vvch","tfbxw","jfidl","pdr","yknvnb","dlrgi","mnoy"])
tevaa = Factor("tevaa", ["ifoweu","vvch","tfbxw","jfidl","pdr","yknvnb","dlrgi","mnoy"])
uabdyq = Factor("uabdyq", ["ifoweu","vvch","tfbxw","jfidl","pdr","yknvnb","dlrgi","mnoy"])
def nmaz(iiyrcc, tevaa, uabdyq):
     return tevaa == iiyrcc
def gpxqg(iiyrcc, tevaa, uabdyq):
     return tevaa != iiyrcc and uabdyq == iiyrcc
def wlrka(iiyrcc, tevaa, uabdyq):
     return (not nmaz(iiyrcc, tevaa, uabdyq)) and (not iiyrcc == uabdyq)
qceb = Factor("ibv", [DerivedLevel("ivi", WithinTrial(nmaz, [iiyrcc, tevaa, uabdyq])), DerivedLevel("cbi", WithinTrial(gpxqg, [iiyrcc, tevaa, uabdyq])),DerivedLevel("nncbtr", WithinTrial(wlrka, [iiyrcc, tevaa, uabdyq]))])
### EXPERIMENT
design=[iiyrcc,tevaa,uabdyq,qceb]
crossing=[qceb]
### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_1/3_2_2"))
### END