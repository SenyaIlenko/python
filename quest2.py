


while True:

    article = input('Ведіть статтю, або стоп, аби зупинити пограму:    ')

    if article == 'стоп':
        break

    author = input('Ведіть автора, або стоп, аби зупинити пограму:    ')
    if author == 'стоп':
        break

    with open('quotes.txt', 'a', encoding='utf-8') as doc:
        doc.write('\n')
        doc.write(article)


        doc.write('\n')
        doc.write(author)
