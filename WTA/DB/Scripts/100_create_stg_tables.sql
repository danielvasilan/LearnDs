IF NOT EXISTS (SELECT * FROM sys.objects where name = 'wta_matches')
CREATE TABLE [stg].[wta_matches](
	[tourney_id] [varchar](50) NULL,
	[tourney_name] [varchar](50) NULL,
	[surface] [varchar](50) NULL,
	[draw_size] [varchar](50) NULL,
	[tourney_level] [varchar](50) NULL,
	[tourney_date] [varchar](50) NULL,
	[match_num] [varchar](50) NULL,
	[winner_id] [varchar](50) NULL,
	[winner_seed] [varchar](50) NULL,
	[winner_entry] [varchar](50) NULL,
	[winner_name] [varchar](50) NULL,
	[winner_hand] [varchar](50) NULL,
	[winner_ht] [varchar](50) NULL,
	[winner_ioc] [varchar](50) NULL,
	[winner_age] [varchar](50) NULL,
	[winner_rank] [varchar](50) NULL,
	[winner_rank_points] [varchar](50) NULL,
	[loser_id] [varchar](50) NULL,
	[loser_seed] [varchar](50) NULL,
	[loser_entry] [varchar](50) NULL,
	[loser_name] [varchar](50) NULL,
	[loser_hand] [varchar](50) NULL,
	[loser_ht] [varchar](50) NULL,
	[loser_ioc] [varchar](50) NULL,
	[loser_age] [varchar](50) NULL,
	[loser_rank] [varchar](50) NULL,
	[loser_rank_points] [varchar](50) NULL,
	[score] [varchar](50) NULL,
	[best_of] [varchar](50) NULL,
	[round] [varchar](50) NULL,
	[minutes] [varchar](50) NULL,
	[w_ace] [varchar](50) NULL,
	[w_df] [varchar](50) NULL,
	[w_svpt] [varchar](50) NULL,
	[w_1stIn] [varchar](50) NULL,
	[w_1stWon] [varchar](50) NULL,
	[w_2ndWon] [varchar](50) NULL,
	[w_SvGms] [varchar](50) NULL,
	[w_bpSaved] [varchar](50) NULL,
	[w_bpFaced] [varchar](50) NULL,
	[l_ace] [varchar](50) NULL,
	[l_df] [varchar](50) NULL,
	[l_svpt] [varchar](50) NULL,
	[l_1stIn] [varchar](50) NULL,
	[l_1stWon] [varchar](50) NULL,
	[l_2ndWon] [varchar](50) NULL,
	[l_SvGms] [varchar](50) NULL,
	[l_bpSaved] [varchar](50) NULL,
	[l_bpFaced] [varchar](50) NULL
) ON [PRIMARY]
GO

IF NOT EXISTS (SELECT * FROM sys.objects where name = 'wta_players')
CREATE TABLE [stg].[wta_players](
	[player_id] [varchar](50),
	player_firstname varchar(100),
	player_lastname varchar(100),
	player_hand varchar(1),
	player_birthdate_str varchar(20),
	country_code varchar(5)
	)
GO


IF NOT EXISTS (SELECT * FROM sys.objects where name = 'Country_iso')
CREATE TABLE [stg].[Country_iso](
	country_name varchar(100) ,
	iso_code_2 varchar(2),
	iso_code_3 varchar(3),
	num_code varchar(10), 
	avg_lat numeric,
	avg_long numeric
)
GO

CREATE UNIQUE NONCLUSTERED INDEX stg_country_iso_code_3 on stg.country_iso(iso_code_3)
GO

select iso_code_3, count(1) from [stg].[Country_iso] group by iso_code_3
having count(1) > 1

select * from [stg].[Country_iso] 
where iso_code_3 = 'LBY'