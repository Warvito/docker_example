import numpy as np
import pandas as pd
from pathlib import Path

# dataset_dir = Path("/dataset") # to access datasets

print(f"Numpy Version: {np.__version__}")
print(f"Pandas Version: {pd.__version__}")

df = pd.DataFrame(columns=['module', 'version'])
df = df.append({"module": "numpy", "version": str(np.__version__)}, ignore_index=True)
df = df.append({"module": "pandas", "version": str(pd.__version__)}, ignore_index=True)

df.to_csv("/outputs/report.csv", index=False)

