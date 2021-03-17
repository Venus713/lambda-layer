# lambda-layer

## Structure
```
my-layers
├── layers
│   └── tools
│       └── aws_requirements.txt
└── serverless.yml
```

## Install Dependendies from `aws_requirements.txt` in `layers/tools` before deploy
```
$ cd layers/tools
$ pip install -t python/lib/python3.7/site-packages -r aws_requirements.txt
```