from schema import schema


if __name__ == '__main__':
    result = schema.execute('{ hello }')
    print(result.data['hello']) # "Hello World"
