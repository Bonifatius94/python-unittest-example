# Python TDD Example

## About
This project is a boilerplate for a unit-testable Python project.
It uses the official Alpine Docker image with Python 3.8 as runtime.

## Usage
All build + test scripting is abstracted by a Dockerfile.
For creating the Docker image run following command:

```sh
docker build . -t "python-unittest-example"
```

Now, spin up the dockerized Python app you've just built like this:

```sh
docker run "python-unittest-example"
```

*Note: Launching the app should print a 1 to your console.*

## License
There's no license. Feel free to use this boilerplate (at your own risk).
