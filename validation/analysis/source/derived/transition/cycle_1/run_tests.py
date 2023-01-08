import os
from rouge_score import rouge_scorer
import pandas as pd
EXCLUDES = [(3, 1, 0), (3, 1, 1), (3, 1, 2), (3, 1, 3), (3, 1, 4)]
NO_COMPILE = [(3, 2, 0), (3, 2, 1), (3, 2, 2), (3, 2, 3), (2, 2, 4), (3, 2, 4)]
