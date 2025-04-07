from tabulate import tabulate

def show_code(table, algorithm):
    headers = ['CHAR', 'DECIMAL', 'BINÁRIO (' + algorithm + ')']
    print(tabulate(table, headers=headers, tablefmt='grid'))

def show_decode(table, algorithm):
    headers = ['BINÁRIO', 'DECIMAL', 'CHAR (' + algorithm + ')']
    print(tabulate(table, headers=headers, tablefmt='grid'))