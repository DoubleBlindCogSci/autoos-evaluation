import os
import pandas as pd
from rouge_score import rouge_scorer

### random code was not compileable (exclude without mention):
EXCLUDES_CODE_1 = [(5,2,2)]

### NO_COMPILE
NO_COMPILE = []

### NO_SCORE (couldn't get sequence for 1 and 2)
NO_SCORE = [(4,1,2), (4,2,0), (5,0,2), (5,1,2), (5,2,1), (6,0,1), (6,1,2)]

### ERROR IN CODE_2
ERROR_2 = [(5,2,0), (6,1,0), (6,1,1),(6,2,0), (6,2,1), (6,2,2)]
