# network-properties-with-networkx

Python code that uses networkx to calculate some basic properties of the Character Interaction Network for George R. R. Martin's "A Song of Ice and Fire" saga.

Commented out code creates two random graphs using the Erdős-Rényi model (random) and the Watts-Strogatz model (small-world).

```sh
python3 -m virtualenv .
. bin/activate
pip install -r requirements.txt

python asoiaf.py
```
