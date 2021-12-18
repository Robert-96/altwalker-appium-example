# altwalker-appium-example

A simple example of how to use [AltWalker](https://altom.gitlab.io/altwalker/altwalker/) with tests written with [Appium](https://appium.io/).

You can clone this repository and run the example tests provided. The android app is provided by the [Appium Python Client](https://github.com/appium/python-client) project. You'll need to make sure that you set up your environment properly using the [Appium documentation](https://appium.io/).

## Setup

1. Prerequisites:

    * Python3
    * AltWalker: Checkout the [installation guide](https://altom.gitlab.io/altwalker/altwalker/installation.html) from the AltWalker documentations.
    * Appium: Checkout the [installation guide](https://appium.io/docs/en/about-appium/getting-started/?lang=en#installing-appium) form the Appium documentation.

2. Install python dependencies:

    ```
    $ pip install -r requirements.txt
    ```

## File overview

* `app/selendroid-test-app.apk`: is an android test provided by the [Appium Python Client](https://github.com/appium/python-client)


## Running the tests

```
$ altwalker online tests -m models/default.json "random(vertex_coverage(100))"
```

## License

This project is licensed under the [MIT License](LICENSE).
