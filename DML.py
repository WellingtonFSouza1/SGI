import pymysql

try:

    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='Zeus1367',
        db='ex_01')
    cursor = conexao.cursor(pymysql.cursors.DictCursor)

except TypeError as error:

    print(f'{error}')


def select(fields, tables, where=None):

    global cursor

    query = 'SELECT ' + fields + ' FROM ' + tables
    if where:
        query += ' WHERE ' + where

    cursor.execute(query)

    return cursor.fetchall()


def insert(values, table, fields=None):
    global cursor, conexao
    query = 'INSERT INTO ' + table
    if fields:
        query += ' ('+fields+')'
    query += ' VALUES ' + '('+values+')'

    try:

        cursor.execute(query)
        conexao.commit()
        conexao.close()

        return True

    except ValueError as Error:

        return Error


def update(table, field, values, where):

    global cursor, conexao

    query = 'UPDATE ' + table + ' SET ' + field + " = '" + values + "'" ' WHERE ' + where

    cursor.execute(query)
    conexao.commit()
    conexao.close()


def delete(table, where):

    global cursor, conexao

    query = 'DELETE FROM ' + table + ' WHERE ' + where

    cursor.execute(query)
    conexao.commit()
    conexao.close()

    return conexao.commit
