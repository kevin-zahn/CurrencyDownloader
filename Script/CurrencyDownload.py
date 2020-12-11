import logging
from datetime import date
from pyodbc import connect
import json
from CurrencyDownload_Functions import dwConnection, localODBDdriver, Currency_Check, Update_Currency
import sys

if __name__ == '__main__':
    logging.basicConfig(filename='CC_Downloader ' + str(date.today()) + '.log',
                        format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO)
    logging.info('Downloader started')

    # Load JSON-Config-File
    config = json.load(open('Settings.json'))

    # System-Parameter
    # use this line when you got system_name/ client_name from cubebuilder
    # client = sys.argv[1]
    # use this when you want to use the jdbc entry
    client = config['system_name']

    Daily_SQL = 'InvoicePosition_GE20180101.sql'
    Monthly_SQL = 'InvoicePosition_LE20171231.sql'

    # DataWorld-Information
    dwQuery = 'a10f2ef9-68c0-42b4-82a6-91715c47a3d9'
    dwToken = config["Token"]

    # execute updates
    try:
        # connection to client database
        connection = connect('Driver={' + str(str(localODBDdriver())[1:-1])[1:-1] +
                             '};''Server=' + config['server'] + '\\' + client +
                             ';''UID=' + config['user'] +
                             ';''PWD=' + config['password'] +
                             ';''Trusted_Connection=no;')
        cursor = connection.cursor()

        # Daily-Download
        cursor.execute(open('SQL/'+Daily_SQL, mode='r').read().replace('_CLIENT', '_' + client))
        # print(open('SQL/'+Daily_SQL, mode='r').read().replace('_CLIENT', '_' + client))
        Update_Currency(cursor, dwQuery, dwToken, client)

        # Monthly Download
        cursor.execute(open('SQL/' + Monthly_SQL, mode='r').read().replace('_CLIENT', '_' + client))
        Update_Currency(cursor, dwQuery, dwToken, client)

    except Exception as e:
        logging.critical(e)
