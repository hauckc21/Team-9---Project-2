CREATE TABLE alliances(
   alliances_id serial PRIMARY KEY,
   full_name VARCHAR (255) UNIQUE NOT NULL,
   num_countries INT NOT NULL
);

CREATE TABLE countries (
   countries_id serial PRIMARY KEY,
   name VARCHAR (255) UNIQUE NOT NULL,
   region VARCHAR (255) NOT NULL,
   area INT NOT NULL,
   population FLOAT );
	
CREATE TABLE details (
  details_id serial PRIMARY KEY,
  alliances_id INT NOT NULL,
  countries_id INT NOT NULL,
	
  FOREIGN KEY (alliances_id)
      REFERENCES alliances (alliances_id),
  FOREIGN KEY (countries_id)
      REFERENCES countries (countries_id)
);