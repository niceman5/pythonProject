USE test
GO

IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'test1') AND type in (N'P', N'PC'))
    DROP PROCEDURE dbo.test1
GO

CREATE PROCEDURE [dbo].[test1]
AS
SET NOCOUNT ON;
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

SELECT * FROM test.dbo.Student WHERE [Std_No] = 1
SELECT * FROM test.dbo.Student WHERE [Std_No] = 2
