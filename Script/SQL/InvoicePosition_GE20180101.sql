select distinct concat(left(str(key_Date, 8), 4), '-', substring(str(key_Date, 8), 5, 2), '-',right(str(key_Date, 8), 2)) as date, KEY_FCURR, KEY_TCURR from Orpheus_CubebuilderWork_CLIENT.dbo.CURRENCY_DAY__INVOICE_POSITION where NUM_RATE is null and KEY_DATE >= 20210101