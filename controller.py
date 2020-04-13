import dominate, pandas as pd, csv, os
from dominate.tags import *

def extractDataFromTxt():
    df = pd.read_csv('output.txt', delimiter= '\s+', index_col=False)
    df.to_csv('output.csv')
    data = []
    with open("output.csv") as f:
        row1 = next(csv.reader(f))
        header = " ".join(row1[1:]).split(" ")
        for row in csv.reader(f):
            row_data = " ".join(row[1:]).split(" ")
            data.append(row_data)
    return header, data

def createHTML(header, data):
    table_headers = header
    doc = dominate.document(title='Fundamental Analysis Table ')
    with doc.head:
        link(rel='stylesheet', href='style.css')
        link(rel='icon', type='image/png', href='favicon.ico')
    with doc:
        with div(cls='container'):
            h1('This is a table to show data from the stock market')
            h2('Brasilian Stocks')
            with table(id='acoes', cls='table'):
                with thead():
                    with tr():
                        for table_head in table_headers:
                            th(table_head)
                with tbody():
                    for i in range (len(data)):
                        with tr(id=data[i][0]):
                            for j in range(len(data[i])):
                                td(data[i][j], id=table_headers[j])
    return doc

def main():
    header, data = extractDataFromTxt()
    doc = createHTML(header, data)
    with open('index.html', 'w') as file:
        file.write(doc.render())

if __name__ == '__main__':
    main()