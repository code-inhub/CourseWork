def change(adj, noun1, verb, noun2):
    with open('inputt.txt', 'r') as file:
        content = file.read()

    content = content.replace('ADJECTIVE', adj)
    content = content.replace('NOUN', noun1, 1)
    content = content.replace('VERB', verb, 1)
    content = content.replace('NOUN', noun2, 1)

    with open('inputt.txt', 'w') as file:
        file.write(content)

adjective=input("Enter an adjective: ")
nou=input("Enter a noun: ")
verb=input("Enter a verb: ")
noun=input("Enter a noun: ")
change(adjective,nou,verb,noun)