from sweetpea import *
import os
_dir=os.path.dirname(__file__)
### REGULAR FACTORS
yCDHuUKKXJHlmw = Factor("yCDHuUKKXJHlmw", ["mwPrApHC", "eRGDxwwQvQm", "en5M*Z", "tlgofwqzft", Level("E}heUMKsJY", 2), "kf!^", "P8;B:DeExt", "adiGESg", "kbdpZW&VkEn", "bPd7zslvhbpnf"])
pNTQUQ_xZYN = Factor("pNTQUQ xZYN", ["jjjru", "LSxy", ")UyqDWjyKp~qZ", "Qdi!bsTMzuE", "OybdpZ", "GmR", "Fdh", "ROgzVknx", "eYatjGpkNdQv"])
m_sldpo_ = Factor("m*sldpo<", ["oacC8VzGFCuwhU", "|oeEvjIxpCdiL", "pfOd", "#Uj~PkG", "SzZbjAT}Fd", "m(x<drnKo", "bFSRxDVXBbhnp", "M^Gs", "ADiFE~"])

design=[yCDHuUKKXJHlmw,pNTQUQ_xZYN,m_sldpo_]
crossing=[yCDHuUKKXJHlmw,pNTQUQ_xZYN,m_sldpo_]

### APPENDIX
block=CrossBlock(design,crossing,[])
experiment=synthesize_trials(block,1)
save_experiments_csv(block,experiment,os.path.join(_dir,"out_code_2/9_3_0"))

### END
