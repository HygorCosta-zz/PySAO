*FILE '$IRFFILE'   ** Nome do arquivo de entrada
**LINES-PER-PAGE 10000    ** Don't have any page breaks in a table.
**TABLE-WIDTH     300     ** Produce a wide table if many producers,
**NO-BLANKS               ** Always have a value in every column,
**WIDTH 18
**PRECISION 10            ** with four significant digits.
*SPREADSHEET
*TIME OFF                 ** The tables will have no time column,
**DATE OFF                ** but will have a date column
*TABLE-FOR
		
   *COLUMN-FOR  *GROUPS 'FIELD-PRO'
                *PARAMETERS 'Cumulative Oil SC'
   *COLUMN-FOR  *GROUPS 'FIELD-PRO'
                *PARAMETERS 'Cumulative Water SC'
   *COLUMN-FOR  *GROUPS 'FIELD-INJ'
                *PARAMETERS 'Cumulative Water SC'

   *COLUMN-FOR  *GROUPS 'FIELD-PRO'		
				*PARAMETERS 'Oil Rate SC'
   *COLUMN-FOR  *GROUPS 'FIELD-PRO'		
				*PARAMETERS 'Water Rate SC'
   **COLUMN-FOR  *GROUPS 'FIELD-PRO'		
	**			*PARAMETERS 'Liquid Rate SC'
   *COLUMN-FOR  *GROUPS 'FIELD-INJ'		
				*PARAMETERS 'Liquid Rate SC'

				
   **COLUMN-FOR  *WELLS 'NA1A' 'NA2' 'NA3D'
	**			*PARAMETERS 'Oil Rate SC' 
				
   **COLUMN-FOR  *SPECIALS 'PRES  Average Reservoir Pressure.'
	
*TABLE-END

** *LIST-PARAMETERS causes Results Report to list all the allowed parameters and origins for columns in a table (for first opened file).
