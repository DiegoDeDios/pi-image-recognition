# Set up instructions

## Pre-requirements

```bash
Make sure you have installed Python3.6 or greater along with Pip
```

## Setting up environment variables:


### For Linux

```bash
source set_env.sh ./path/to/google/key
```


### For Windows

```bash
set_env.bat ./path/to/google/key
```


## Running the project

```bash
flask run
```

## Testing out with CURL

```bash
curl -F "file=@/path/to/image" http://127.0.0.1:5000/image
```



