CREATE TABLE Food_Group (
	id			INT				NOT NULL	IDENTITY	PRIMARY KEY,
	name		VARCHAR(255)	NOT NULL,
);
GO

CREATE TABLE Food (
	id			INT				NOT NULL	IDENTITY	PRIMARY KEY,
	name		VARCHAR(255)	NOT NULL,
);
GO

ALTER TABLE Food ADD
	food_group_id INT NOT NULL DEFAULT 1,
	CONSTRAINT FK_Food_Group
	FOREIGN KEY (food_group_id)
	REFERENCES Food_Group (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE;
GO

CREATE TABLE Recipe (
	id			INT				NOT NULL	IDENTITY	PRIMARY KEY,
	name		VARCHAR(255)	NOT NULL,
);
GO

CREATE TABLE Recipe_Food (
	recipe_id	INT		NOT NULL,
	food_id		INT		NOT NULL
	FOREIGN KEY (recipe_id) REFERENCES Recipe(id)
		ON DELETE CASCADE,
	FOREIGN KEY (food_id) REFERENCES Food(id)
		ON DELETE CASCADE
);
GO

ALTER TABLE Recipe_Food ADD
	CONSTRAINT PK_RF PRIMARY KEY (recipe_id, food_id);
GO

CREATE TABLE Recipe_Comment (
	id			INT				NOT NULL	IDENTITY	PRIMARY KEY,
	comment		VARCHAR(255)	NOT NULL,
);
GO

ALTER TABLE Recipe_Comment ADD
	recipe_id INT NOT NULL,
	CONSTRAINT FK_Recipe
	FOREIGN KEY (recipe_id)
	REFERENCES [dbo].[Recipe] (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE;
GO