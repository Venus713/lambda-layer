# How to use layers with function in same service?

## Example Serverless.yml
```
layers:
  test:
    path: layer
functions:
  hello:
    handler: handler.hello
    layers:
      - { Ref: TestLambdaLayer }
```
Noted: The name of your layer in Cloudformation template will be your layer name TitleCased and have `LambdaLayer` appended to the end.
For example:
> test -> TestLambdaLayer

## Invoke
```
$ sls invoke -f hello
```