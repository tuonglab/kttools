# tools
Miscellaneous python tools


### Install
```bash
git clone https://github.com/clatworthylab/kttools.git
echo 'export PYTHONPATH=/path/to/kttools:$PYTHONPATH' >> ~/.bash_profile # or ~/.bashrc
source ~/.bash_profile # or ~/.bashrc
```

### Usage
```python
import tools
```


### jupyterhub issue

Edit your `kernel.json` file like so:

```bash
vi /home/jovyan/.local/share/jupyter/kernels/dandelion/kernel.json 
```

add in the `$PATH` and `$PYTHONPATH` bits:
```bash
{
 "argv": [
  "/home/jovyan/my-conda-envs/dandelion/bin/python",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ],
 "env": {
     "PATH": "/home/jovyan/scripts/kttools:$PATH",
     "PYTHONPATH": "/home/jovyan/scripts/kttools:$PYTHONPATH"
 },
 "display_name": "Python (dandelion)",
 "language": "python"
}
```
