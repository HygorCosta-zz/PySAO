*FILE '$IRFFILE'   ** Nome do arquivo de entrada
*SPREADSHEET
*TIME ON                 ** The tables will have no time column,
*TABLE-FOR
		
   *COLUMN-FOR  *GROUPS 'FIELD-PRO'
                *PARAMETERS 'Cumulative Oil SC'
   *COLUMN-FOR  *GROUPS 'FIELD-PRO'
                *PARAMETERS 'Cumulative Water SC'
   *COLUMN-FOR  *GROUPS 'FIELD-PRO'
                *PARAMETERS 'Cumulative Gas SC'
   *COLUMN-FOR  *GROUPS 'FIELD-INJ'
                *PARAMETERS 'Cumulative Water SC'

   *COLUMN-FOR  *GROUPS 'FIELD-PRO'		
				*PARAMETERS 'Oil Rate SC'
   *COLUMN-FOR  *GROUPS 'FIELD-PRO'		
				*PARAMETERS 'Water Rate SC'
   *COLUMN-FOR  *GROUPS 'FIELD-PRO'		
				*PARAMETERS 'Liquid Rate SC'
   *COLUMN-FOR  *GROUPS 'FIELD-INJ'		
				*PARAMETERS 'Liquid Rate SC'

				
   **COLUMN-FOR  *WELLS 'NA1A' 'NA2' 'NA3D'
	**			*PARAMETERS 'Oil Rate SC' 
				
   *COLUMN-FOR  *SPECIALS 'PRES  Average Reservoir Pressure.'
	
*TABLE-END

** *LIST-PARAMETERS causes Results Report to list all the allowed parameters and origins for columns in a table (for first opened file).
