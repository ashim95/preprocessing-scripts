# preprocessing-scripts


## Running the langid parallel tool

Parallelization of langid using joblib

1. Clone the langid repo: `git clone https://github.com/saffsd/langid.py.git`

2. `cd langid/langid.py/langid` 

3. Install requirements : `pip install -r requirements.txt`

4. Create a directory `parallel_runs/` and `n` directories inside this. `n: number of parallel runs`. Generally, for a 48 core server, you can safely use around 40 threads. Simply do this with a bash loop. 
