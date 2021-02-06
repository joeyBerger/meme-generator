import Ingestor

Ingestor = Ingestor.Ingestor
quote_models = Ingestor.parse('../_data/DogQuotes/DogQuotesDOCX.docx')
quote_models = Ingestor.parse('../_data/DogQuotes/DogQuotesTXT.txt')
for quote_model in quote_models:
    print(quote_model)


