from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
vgbnj = Factor("vgbnj", ["mgvnrk","wjeuh","okv","vlm","xerqu","rzmec","lkbnr","jmqwwf"])
def is_jgigg_ocpjh(vgbnj):
    return vgbnj[0] == "xerqu" and vgbnj[-1] != "okv"
def is_jgigg_lzq(vgbnj):
    return vgbnj[0] != "xerqu" and vgbnj[-1] == "okv"
def is_jgigg_vzyhs(vgbnj):
    return not (is_jgigg_ocpjh(vgbnj) or is_jgigg_lzq(vgbnj))
jgigg= Factor("jgigg", [DerivedLevel("ocpjh", Transition(is_jgigg_ocpjh, [vgbnj])), DerivedLevel("lzq", Transition(is_jgigg_lzq, [vgbnj])), DerivedLevel("vzyhs", Transition(is_jgigg_vzyhs, [vgbnj]))])

design=[vgbnj,jgigg]
crossing=[jgigg]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/3_1_1"))

### END
