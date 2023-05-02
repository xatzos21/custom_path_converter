class PhoneNumberConverter:
    regex = '\(?\+?[49]+([0-9]|\/|\(|\)|\-| ){10,}'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return str(value)