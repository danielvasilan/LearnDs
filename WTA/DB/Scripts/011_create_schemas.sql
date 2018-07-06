USE [$(DwhDbName)]
GO


IF NOT EXISTS (SELECT SCHEMA_ID FROM sys.schemas WHERE [name] = 'hub')
BEGIN
	EXEC('CREATE SCHEMA [hub] AUTHORIZATION [dbo]');
	PRINT 'Schema [hub] created';
	END
ELSE
	PRINT 'Schema [hub] already exists';
GO

IF NOT EXISTS (SELECT SCHEMA_ID FROM sys.schemas WHERE [name] = 'lnk')
BEGIN
	EXEC('CREATE SCHEMA [lnk] AUTHORIZATION [dbo]');
	PRINT 'Schema [lnk] created';
	END
ELSE
	PRINT 'Schema [lnk] already exists';
GO

IF NOT EXISTS (SELECT SCHEMA_ID FROM sys.schemas WHERE [name] = 'sat')
BEGIN
	EXEC('CREATE SCHEMA [sat] AUTHORIZATION [dbo]');
	PRINT 'Schema [sat] created';
	END
ELSE
	PRINT 'Schema [sat] already exists';
GO


IF NOT EXISTS (SELECT SCHEMA_ID FROM sys.schemas WHERE [name] = 'dim')
BEGIN
	EXEC('CREATE SCHEMA [dim] AUTHORIZATION [dbo]');
	PRINT 'Schema [dim] created';
	END
ELSE
	PRINT 'Schema [dim] already exists';
GO

IF NOT EXISTS (SELECT SCHEMA_ID FROM sys.schemas WHERE [name] = 'adm')
BEGIN
	EXEC('CREATE SCHEMA [adm] AUTHORIZATION [dbo]');
	PRINT 'Schema [adm] created';
	END
ELSE
	PRINT 'Schema [adm] already exists';
GO

IF NOT EXISTS (SELECT SCHEMA_ID FROM sys.schemas WHERE [name] = 'stg')
BEGIN
	EXEC('CREATE SCHEMA [stg] AUTHORIZATION [dbo]');
	PRINT 'Schema [stg] created';
	END
ELSE
	PRINT 'Schema [stg] already exists';
GO

IF NOT EXISTS (SELECT SCHEMA_ID FROM sys.schemas WHERE [name] = 'bdg')
BEGIN
	EXEC('CREATE SCHEMA [bdg] AUTHORIZATION [dbo]');
	PRINT 'Schema [bdg] created';
	END
ELSE
	PRINT 'Schema [bdg] already exists';
GO
