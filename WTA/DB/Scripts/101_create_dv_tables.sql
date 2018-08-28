USE [WTA]
GO

IF NOT EXISTS (select * from INFORMATION_SCHEMA.TABLES  where TABLE_SCHEMA = 'hub' and table_name = 'Tourney')
BEGIN

	CREATE TABLE [hub].[Tourney](
		TourneyKey varchar(100) NOT NULL,
		TourneyId varchar(50) NOT NULL,
		RecSrc varchar(1) not null ,

		CONSTRAINT [PK_Tourney] PRIMARY KEY CLUSTERED ( TourneyKey )

	)

	PRINT 'Table created: [hub].[Tourney] ';
END
ELSE
	PRINT 'Table exists:  [hub].[Tourney] ';
GO

IF NOT EXISTS (select * from INFORMATION_SCHEMA.TABLES  where TABLE_SCHEMA = 'sat' and table_name = 'Tourney_Attr')
BEGIN

	CREATE TABLE [sat].[Tourney_Attr](
		TourneyKey varchar(100) NOT NULL,
		TourneyName varchar(50) NOT NULL,
		TourneyDate date,
		Surface varchar(50),
		DrawSize varchar(50),
		TourneyLevel varchar(5),
		
		RecSrc varchar(1) not null ,

		CONSTRAINT [PK_Tourney_Attr] PRIMARY KEY CLUSTERED ( TourneyKey )

	)

	PRINT 'Table created: [sat].[Tourney_Attr] ';
END
ELSE
	PRINT 'Table exists:  [sat].[Tourney_Attr] ';
GO

IF NOT EXISTS (select * from INFORMATION_SCHEMA.TABLES  where TABLE_SCHEMA = 'hub' and table_name = 'Player')
BEGIN

	CREATE TABLE [hub].[Player](
		PlayerKey varchar(100) NOT NULL,
		PlayerId varchar(50) NOT NULL,
		RecSrc varchar(1) not null ,

		CONSTRAINT [PK_Player] PRIMARY KEY CLUSTERED ( PlayerKey )

	)

	PRINT 'Table created: [hub].[Player] ';
END
ELSE
	PRINT 'Table exists:  [hub].[Player] ';
GO

IF NOT EXISTS (select * from INFORMATION_SCHEMA.TABLES  where TABLE_SCHEMA = 'sat' and table_name = 'Player_Attr')
BEGIN

	CREATE TABLE [sat].[Player_Attr](
		PlayerKey varchar(100) NOT NULL,
		PlayerName varchar(50) NOT NULL,
		PlayerHand varchar(1),
		PlayerHeight numeric,
		BirthDate date,
				
		RecSrc varchar(1) not null ,

		CONSTRAINT [PK_Player_Attr] PRIMARY KEY CLUSTERED ( PlayerKey )

	)

	PRINT 'Table created: [sat].[Player_Attr] ';
END
ELSE
	PRINT 'Table exists:  [sat].[Player_Attr] ';
GO


