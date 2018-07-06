for %%G in (Scripts/*.sql) do sqlcmd -S .\EDW -U sa -P Lasting123 -i"Scripts/%%G" -v DwhDbName = WTA
pause
