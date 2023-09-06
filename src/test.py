import os
from modules.QuoteEngine.ingestor import Ingestor


def test_01():
    cwd = os.getcwd().replace('\\', '/')
    for path in [
        f'{cwd}/src/_data/DogQuotes/DogQuotesTXT.txt',
        f'{cwd}/src/_data/DogQuotes/DogQuotesCSV.csv',
        f'{cwd}/src/_data/DogQuotes/DogQuotesDOCX.docx',
        f'{cwd}/src/_data/DogQuotes/DogQuotesPDF.pdf',
    ]:
        data = Ingestor.parse(path)
        assert len(data) > 0
        print(f'{path}: PASSED')


if __name__ == '__main__':
    test_01()
