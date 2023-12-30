CREATE TABLE Food (
	id			INT				NOT NULL	IDENTITY	PRIMARY KEY,
	name		VARCHAR(255)	NOT NULL,
);
GO

INSERT INTO Food (name)
VALUES			 ('Bread');
GO

INSERT INTO Food (name)
VALUES			 ('Eggs'),
				 ('Chicken'),
				 ('Potatoes'),
				 ('Milk'),
				 ('Spinach'),
				 ('Onions'),
				 ('Bananas'),
				 ('Cereal');
GO

CREATE TABLE Food_Group (
	id			INT				NOT NULL	IDENTITY	PRIMARY KEY,
	name		VARCHAR(255)	NOT NULL,
);
GO

INSERT INTO Food_Group (name)
VALUES			 ('Grains'),
				 ('Dairy'),
				 ('Poultry'),
				 ('Vegetables'),
				 ('Fruits');
GO

ALTER TABLE Food ADD
	food_group_id INT NOT NULL DEFAULT 1,
	CONSTRAINT FK_Food_Group
	FOREIGN KEY (food_group_id)
	REFERENCES Food_Group (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE;
GO

UPDATE Food
SET food_group_id = (SELECT id FROM Food_Group WHERE name = 'Grains')
WHERE (name = 'Potatoes' OR name = 'Cereal');

UPDATE Food
SET food_group_id = (SELECT id FROM Food_Group WHERE name = 'Dairy')
WHERE (name = 'Eggs' OR name = 'Milk');

UPDATE Food
SET food_group_id = (SELECT id FROM Food_Group WHERE name = 'Poultry')
WHERE (name = 'Chicken');

UPDATE Food
SET food_group_id = (SELECT id FROM Food_Group WHERE name = 'Vegetables')
WHERE (name = 'Spinach' OR name = 'Onions');
GO

UPDATE Food
SET food_group_id = (SELECT id FROM Food_Group WHERE name = 'Fruits')
WHERE (name = 'Bananas');
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

INSERT INTO Recipe (name)
VALUES ('Chicken Salad'),
	   ('Breakfase Burrito');
GO

INSERT INTO Recipe_Food (recipe_id, food_id)
VALUES  (1, 3),
		(1, 6),
		(1, 7),
		(2, 2),
		(2, 4),
		(2, 1);
GO