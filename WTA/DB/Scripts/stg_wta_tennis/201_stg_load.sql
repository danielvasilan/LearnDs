declare @path varchar(1000) = 'd:\work\github\tennis_wta\'

DECLARE @year INT
SET @year = 2015

WHILE @year >= 1980
BEGIN
	DECLARE @table_name varchar (100) = 'wta_matches_' + CAST(@year AS VARCHAR(10))
	-- create a table 
	IF NOT EXISTS (SELECT * FROM sys.objects where name = @table_name)
	BEGIN
		EXEC( 'SELECT * INTO stg.' + @table_name + ' FROM [stg].[wta_matches] WHERE 1=2')
		PRINT 'Table created ' + @table_name
	END
	ELSE
		PRINT 'Table exists ' + @table_name

	EXEC ('TRUNCATE TABLE stg.' + @table_name)
	EXEC ('BULK INSERT stg.' + @table_name + ' FROM '''+@path+@table_name+'.csv'' WITH (FIRSTROW=2,FIELDTERMINATOR = '','', ROWTERMINATOR = ''\n'' ) ')
	PRINT 'Table loaded ' + @table_name
			
	SET @year = @year - 1

END
GO

