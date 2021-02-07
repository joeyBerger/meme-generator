import Ingestor

Ingestor = Ingestor.Ingestor
# quote_models = Ingestor.parse('../_data/DogQuotes/DogQuotesDOCX.docx')
# quote_models = Ingestor.parse('../_data/DogQuotes/DogQuotesTXT.txt')
# quote_models = Ingestor.parse('../_data/DogQuotes/DogQuotesCSV.csv')
quote_models = Ingestor.parse('../_data/DogQuotes/DogQuotesPDF.pdf')
for quote_model in quote_models:
    print(quote_model)


