create table stg.wta_matches
as 
go
select * into stg.wta_matches from [dbo].[wta_matches_2018]
where 1=2

select * from [dbo].[wta_matches_1968]


BULK INSERT stg.wta_matches_2018 FROM 'd:\work\github\tennis_wta\wta_matches_2018.csv' WITH (FIRSTROW=2,FIELDTERMINATOR = ',', ROWTERMINATOR = '\n')
GO