# Pushover Notifier

Pushover Notifier is a Python library that provides a simple way to send notifications via the [Pushover](https://pushover.net/) service. The library can be used to send text messages, images, or a combination of both.

## Installation

You can install the ``pushover_notifier`` library using `pip`:

```shell
cd pushover_notifier
pip install .
```

## Setup

To change the `APP_TOKEN` and `USER_KEY` API variables in the Pushover Notifier library, you need to update the `.env` file with your own values. The `.env` file is a hidden file that should be located in the root directory of your project. It contains environment variables that can be accessed by your Python code using the os.environ dictionary.

To update the `.env` file, open it in a text editor and replace the existing values for `POVER_USER_KEY` and `POVER_GENERAL_NOTIFYER_APP_TOKEN` with your own values. Once you've updated the file, save it and restart your Python application. Your application should now be using the new API variables.

If you've moved the `.env` file to a different directory, you'll need to update the path in the Python code to reflect the new location. To do this, open the `pushover_notifier.py` file in a text editor and find the line that calls load_do`.env`(). Update the path in the argument to the new location of the `.env` file. Once you've updated the file, save it and restart your Python application.

--- 

# Usage

To use the `pushover_notifier` library, you first need to create an instance of the `PushoverNotifier` class:

```python
from pushover_notifier import PushoverNotifier

notifier = PushoverNotifier()
```

Once you have an instance of the `PushoverNotifier` class, you can use the following methods to send notifications:

`send_message(message)`
Send a text message.

```python
notifier.send_message("Hello, world!")

send_message_with_title(message, title)
```

Send a text message with a title.

```python
notifier.send_message_with_title("Hello, world!", "Important Message")

send_message_with_image(message, image)
```

Send a text message with an image attachment.
```python
notifier.send_message_with_image("Check out this cool picture!", "path/to/image.jpg")
```

`send_message_with_image_and_title(message, image, title)`
Send a text message with an image attachment and a title.

```python
notifier.send_message_with_image_and_title(
    "Check out this cool picture!",
    "path/to/image.jpg",
    "Cool Picture Alert"
)
```

In addition to these methods, you can also set the `APP_TOKEN` and `USER_KEY` class variables to avoid having to pass them in every method call. For example:

```python
from pushover_notifier import PushoverNotifier

PushoverNotifier.APP_TOKEN = "your-app-token"
PushoverNotifier.USER_KEY = "your-user-key"

notifier = PushoverNotifier()

notifier.send_message("Hello, world!")
```
