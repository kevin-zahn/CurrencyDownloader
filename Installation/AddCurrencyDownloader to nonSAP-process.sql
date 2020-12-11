use orpheus_cubebuilder   

   Execute admin.P_OS_AddOrUpdateWIDByPredecessorName 
          @phdName = 'non sap ${SYS_KEY}'
        , @pidName = 'Build Currency Conversion'
        , @whdName = 'Currency Conversion: Invoice Position'
        , @widName = 'DataWorld Download'
        , @widDescription = 'DataWorld Download'
        , @predWidName = 'Fill CurrencyDay Table'
        , @flgTracking = 'n'
        , @flgManual = 'n'
        , @wcdName = 'DataWorld Download'
        , @wceName = 'DefaultErrorHandler'
        , @staName = null

    Execute admin.P_OS_DeleteAllWIPsByWCD 
          @phdName = 'non sap ${SYS_KEY}'
        , @pidName = 'Build Currency Conversion'
        , @whdName = 'Currency Conversion: Invoice Position'
        , @widName = 'DataWorld Download'
        , @wcdName = 'DataWorld Download'

    Execute admin.P_OS_AddOrUpdateWIPByWCD 
          @phdName = 'non sap ${SYS_KEY}'
        , @pidName = 'Build Currency Conversion'
        , @whdName = 'Currency Conversion: Invoice Position'
        , @widName = 'DataWorld Download'
        , @wcdName = 'DataWorld Download'
        , @wipName = 'File'
        , @wipValue = '${OrpheusHome}/Python/CurrencyDownloader/CurrencyDownloader.bat'
		
	Execute admin.P_OS_AddOrUpdateWIDByPredecessorName 
          @phdName = 'non sap ${SYS_KEY}'
        , @pidName = 'Build Currency Conversion'
        , @whdName = 'Currency Conversion: Invoice Position'
        , @widName = 'Fix Factor CurrencyDay'
        , @widDescription = 'Fix Factor CurrencyDay'
        , @predWidName = 'DataWorld Download'
        , @flgTracking = 'n'
        , @flgManual = 'n'
        , @wcdName = 'CurrencyConversionFactorFix'
        , @wceName = 'DefaultErrorHandler'
        , @staName = null
