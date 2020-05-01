# GrocerEase

![grocerEase logo](https://raw.githubusercontent.com/orfeasa/grocerease/master/main/static/media/full-logo-horizontal.png)

A web application helping consumers plan their shopping, by estimating the quantity of each item in order do avoid going to the super market for a desired time period.

## Development

This is a [Django](https://www.djangoproject.com/) codebase. Check out the
[Django docs](https://docs.djangoproject.com/) for general technical documentation.

### Structure

The Django project is `grocerease`. There is one Django app, `main`, with all business logic.

### Dependencies

Using [venv](https://docs.python.org/3/library/venv.html):

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Code linting & formatting

```
black . && isort -rc && flake8
```

## License

This software is licensed under the MIT license.
For more information, read the [LICENSE](LICENSE) file.
