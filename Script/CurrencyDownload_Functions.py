import logging
import requests
import pycountry
import pyodbc


# Connection to Datawrold
def dwConnection(dwQuery, date, f_Currency, t_Currency, dwToken):
    try:
        return requests.post('https://api.mckinsey.data.world/v0/queries/' + dwQuery + '/results',
                      data='{"parameters": {"date": "' + date + '", "currency1": "' + f_Currency + '", "currency2": "' +
                           t_Currency + '"}, "includeTableSchema": false, "maxRows": 1}',
                      headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + dwToken})
    except Exception as e:
        logging.critical(e)
        logging.critical('Can not connect to McKinsey Data-World')
        raise


# Check local ODBC driver
def localODBDdriver():
    try:
        localODBCDrivers = [x for x in pyodbc.drivers() if x.startswith('ODBC')]
        ODBC_Counter = len(localODBCDrivers)
        if ODBC_Counter == 1:
            ODBC = localODBCDrivers
            logging.info(str(ODBC) + ' will be used for connection')
            return ODBC
        else:
            logging.critical(str(localODBCDrivers) + ' no unique ODBC-driver, please check this manuel')
    except Exception as e:
        logging.critical(e)
        logging.critical('Problem with ODBC-driver')
        raise


# List of valid currencies
def Currency_Check():
    try:
        ISO_Currencies = []
        for currency in pycountry.currencies:
            ISO_Currencies.append(currency.alpha_3)
        return ISO_Currencies
    except Exception as e:
        logging.critical(e)
        logging.critical('Problem with ISO-Currencies')
        raise


def Update_Currency(cursor, dwQuery, dwToken, client):
    try:
        for row in cursor:
            date = row[0]
            if row[1] in Currency_Check():
                f_Currency = row[1]
                if row[2] in Currency_Check():
                    t_Currency = row[2]
                    response = dwConnection(dwQuery, date, f_Currency, t_Currency, dwToken)
                    # cursor.execute('update Orpheus_CubebuilderWork_' + client + '.dbo.CURRENCY_DAY__INVOICE_POSITION set NUM_RATE = '+ str(response.json()[0]['rate'])[:7] +' where NUM_RATE is null and KEY_DATE = '+ date.replace('-','') + ' and KEY_FCURR = \''+ f_Currency +'\' and KEY_TCURR = \''+ t_Currency + '\'')
                    # print("From: " + f_Currency + " to: " + t_Currency + " for date: " + str(date).replace('-','') + " : " + str(response.json()[0]['rate'])[:7])
                    logging.info("From: " + f_Currency + " to: " + t_Currency + " for date: " + str(date).replace('-', '') + " : " + str(response.json()[0]['rate'])[:7])
                    print('update Orpheus_CubebuilderWork_' + client + '.dbo.CURRENCY_DAY__INVOICE_POSITION set NUM_RATE = ' + str(response.json()[0]['rate'])[:7] + ' where NUM_RATE is null and KEY_DATE = ' + date.replace('-', '') + ' and KEY_FCURR = \'' + f_Currency + '\' and KEY_TCURR = \'' + t_Currency + '\'')
    except Exception as e:
        logging.critical(e)
        logging.critical('Problem with update')
        raise
