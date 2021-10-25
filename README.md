# init

python 3.8 was used

## no_1

Change directory to no_1 folder

```
cd no_1
```

Run this to generate the problem with m(Nat instances) and n(Subnets) accordingly, it will generates a files named "problem.txt"

```
python3 problem_generator.py 3 4
```

Run this to solve the problem, it will automatically read the file named "problem.txt"
```
python3 run.py
```
## no_2

Change directory to no_2 folder

```
cd no_2
```

Install requirements, create virtual environment yourself if needed

```
pip3 install -r requirements.txt
```

Run this for the result, it will write to the file named 'output.json'

```
python run.py example.json
```

## no_3
Set appropriate access key in env

```
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
export AWS_DEFAULT_REGION=ap-southeast-1
```

Assumption:
- One team has one maintainer
- No policies were implimented
