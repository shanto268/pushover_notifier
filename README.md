# Pushover Notifier

Pushover Notifier is a Python library that provides a simple way to send notifications via the [Pushover](https://pushover.net/) service. The library can be used to send text messages, images, or a combination of both.

## Installation

You can install the ``pushover_notifier`` library using `pip`:

```shell
cd pushover_notifier
pip install .
```

# Usage

To use the `pushover_notifier` library, you first need to create an instance of the `PushoverNotifier` class:

```python
from `pushover_notifier` import PushoverNotifier

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
Send a text message with an image attachment.
```

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
