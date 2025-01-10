-- Step 1: Create the database
CREATE DATABASE procore_db;

-- Step 2: Connect to the new database
use procore_db;

show databases;
use procore_db;
show tables;

DROP TABLE IF EXISTS projects;

select * from projects;


DROP TABLE projects;



-- Step 3: Create the projects table
CREATE TABLE projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    project_id VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    status VARCHAR(100) NOT NULL,
    company_id VARCHAR(255) NOT NULL,
    updated_at DATETIME
);

INSERT INTO projects (id, project_id, name, status, company_id, updated_at)
VALUES (1, '1', 'Project A', 'On Hold', '12345', NOW());


DELETE FROM projects
WHERE id IN ('1', '7', '8', '9','10');

DELETE FROM projects WHERE id IN (1,2,3,7,8,9,10);


ALTER TABLE projects MODIFY id INT NOT NULL;

desc projects;



-- CREATE TABLE projects (
--     id INT PRIMARY KEY,
--     project_id VARCHAR(255) NOT NULL UNIQUE,
--     name VARCHAR(255) NOT NULL,
--     status VARCHAR(100) NOT NULL,
--     company_id VARCHAR(255) NOT NULL,
--     updated_at DATETIME
-- );

-- ALTER TABLE projects MODIFY id INT AUTO_INCREMENT;

