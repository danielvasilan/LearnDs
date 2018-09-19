CREATE VIEW dim.Player
as
select pl.PlayerKey, pl.PlayerId, pa.BirthDate, pa.PlayerHand, pa.PlayerHeight, pa.PlayerName, pc.CountryKey 
from hub.Player pl
inner join sat.Player_Attr pa on pa.PlayerKey = pl.PlayerKey
left join lnk.Player_Country pc on pc.PlayerKey = pl.PlayerKey 
GO

DROP VIEW  dim.Country
GO

CREATE VIEW dim.Country
AS
SELECT countryKey, CountryName
FROM hub.country
GO

CREATE VIEW fact.CountryPlayers
AS
SELECT *
FROM dim.Country c
INNER JOIN 

GO

DROP VIEW dim.Tourney
GO

CREATE VIEW dim.Tourney
AS
SELECT t.TourneyKey, ta.Surface, ta.DrawSize, ta.TourneyDate, ta.TourneyLevel, ta.TourneyName,
	YEAR(TourneyDate) TourneyYear
FROM hub.Tourney t
INNER JOIN sat.Tourney_Attr ta ON ta.TourneyKey = t.TourneyKey
GO

DROP VIEW dim.Surfaces
GO

CREATE VIEW dim.Surfaces
AS
SELECT DISTINCT Surface
FROM sat.Tourney_Attr
GO

DROP VIEW dim.Levels
GO

CREATE VIEW dim.Levels
AS
SELECT DISTINCT TourneyLevel
FROM sat.Tourney_Attr
GO


DROP VIEW dim.TourneyYears
GO

CREATE VIEW dim.TourneyYears
AS
SELECT DISTINCT YEAR(TourneyDate) TourneyYear
FROM sat.Tourney_Attr
GO


/*

select * from dim.Player
select * from dim.Country

*/

select distinct tourney_name
from stg.wta_matches
where tourney_name not like 'Fed Cup%'
