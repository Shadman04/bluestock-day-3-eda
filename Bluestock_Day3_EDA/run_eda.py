"""Execute the Day 3 EDA notebook and export charts."""
from pathlib import Path
import nbformat
from nbclient import NotebookClient
root=Path(__file__).resolve().parent
p=root/"notebooks"/"EDA_Analysis.ipynb"
nb=nbformat.read(p,as_version=4)
executed=NotebookClient(nb,timeout=1800,kernel_name="python3",resources={"metadata":{"path":str(root)}}).execute()
nbformat.write(executed,p)
print("Done. Charts: outputs/charts/")
