from faker import Faker


class Fake:
    """Class for generating random test data usingFaker library."""

    def __init__(self, faker: Faker):
        """
        Initialize data generator with a Faker instance.

        :param faker: Faker instance to generate test data. """
        self.faker = faker

    def text(self) -> str:
        """
        Generates random text.

        :return: Random text.
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Generates random UUID4.

        :return: Random UUID4.
        """
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        Generates random email.

        :param domain: Domain (e.g. "example.com").
        If not specified random domain will be used.
        :return: Random email.
        """
        return self.faker.email(domain=domain)

    def sentence(self) -> str:
        """
        Generates random sentence.

        :return: Random sentence.
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Generates random password.

        :return: Random password.
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Generates random last name.

        :return: Random last name.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Generates random name.

        :return: Random name.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Generates random middle name.

        :return: Random middle name.
        """
        return self.faker.first_name()

    def estimated_time(self) -> str:
        """
        Generate a random estimated duration in weeks.

        :return: A string representing a random duration between 1 and 10 weeks.
        """
        return f"{self.integer(1, 10)} weeks"

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Generates random integer within specified range.

        :param start: Start range (including).
        :param end: End range (including).
        :return: Random integer.
        """
        return self.faker.random_int(start, end)

    def max_score(self) -> int:
        """
        Generates random max score between 50 and 100.

        :return: Random score between 50 and 100.
        """
        return self.integer(50, 100)

    def min_score(self) -> int:
        """
        Generates random min score between 1 and 30.

        :return: Random score between 1 and 30.
        """
        return self.integer(1, 30)


fake = Fake(faker=Faker())
