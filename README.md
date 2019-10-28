## How to run
### Using Docker (recommended)
1. Run the docker container `docker run --rm -it -v $(pwd):/source python:3.8 bash`
2. Change directories to source code `cd /source`
3. Install dependencies `pip install -r requirements.txt`
4. Run tests `pytest`

### Using System
1. Install dependencies `pip install -r requirements.txt` (probably use a virtualenv)
2. Run tests `pytest`