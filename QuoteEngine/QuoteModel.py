class QuoteModel():

    def __init__(self,body,author):
        self.body = QuoteModel.format_body(body)
        self.author = author

    def __str__(self):
        return f"{self.body} by {self.author}"

    @classmethod
    def format_body(cls,body):
        return body.replace('"','')

