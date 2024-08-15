class Document:
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Pdf(Document):
    def show(self):
        return "show PDF content"

class Word(Document):
    def show(self):
        return "Show Word Content"

docs = [Pdf(), Word()]
for doc in docs:
    print(doc.show())