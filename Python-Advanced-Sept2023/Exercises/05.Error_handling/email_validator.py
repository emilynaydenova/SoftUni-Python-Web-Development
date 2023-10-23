EMAIL_NAME_MIN_LEN = 4
VALID_TOP_LEVEL_DOMAINS = ['.com', '.bg', '.net', '.org']

"""
Some custom exceptions for emails validation
"""


class MustContainAtSymbolError(Exception):
    """" Raised when no @ in email"""

    def __init__(self, message="Email must contain @"):
        self.message = message
        super().__init__(message)


class NameTooShortError(Exception):
    """"
    Raised if the name in the email is less than or equal to
    EMAIL_NAME_MIN_LEN
    """

    def __init__(self, message=f"Name must be more than {EMAIL_NAME_MIN_LEN} characters"):
        self.message = message
        super().__init__(message)


class InvalidDomainError(Exception):
    """" Raised when email has no valid domain name"""

    def __init__(self,
                 message=f'Domain must be one of the following: {", ".join(VALID_TOP_LEVEL_DOMAINS)}'):
        self.message = message
        super().__init__(message)


def validate_at(value):
    if not value or '@' not in value:
        raise MustContainAtSymbolError()


def validate_name_length(value):
    if not value or len(value) <= EMAIL_NAME_MIN_LEN:
        raise NameTooShortError()


def validate_top_level_domain(value):
    tld = '.' + value.rsplit('.')[-1]
    if tld not in VALID_TOP_LEVEL_DOMAINS:
        raise InvalidDomainError()


# Main program validating emails
while (email := input()) != 'End':
    # validating if @ Symbol exists
    validate_at(email)

    user_part, domain_part = email.rsplit("@", 1)

    # validating email's user part length
    validate_name_length(user_part)
    # validating email's domain part
    validate_top_level_domain(domain_part)

    print('Email is valid')

""""
Tests:
# valid
peter@gmail.com
pet@r@gmail.com
ivan_petrov@dd.ff.bg
admin@net
End

# invalid
''
abc@abv.bg
petergmail.com
peter@gmail.hotmail
admin@nett
"""
