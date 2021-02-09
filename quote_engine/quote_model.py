class QuoteModel():
    """ Class that manipulates and stores quote information """

    def __init__(self, body, author):
        """ Store body and author of quote """

        self.body = QuoteModel.format_body(body)
        self.author = QuoteModel.format_author(author)

    def __str__(self):
        """ Returns readable string """

        return f"{self.body} by {self.author}"

    @classmethod
    def format_body(cls, body):
        """ Removes extraneous characters from body """

        return body.replace('"', '')

    @classmethod
    def format_author(cls, author):
        """ Removes extraneous characters from given author """

        name = author.replace(' ', '').replace('-', '')
        return name
