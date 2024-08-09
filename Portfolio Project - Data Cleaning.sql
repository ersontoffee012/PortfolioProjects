-- SQL Project - Data Cleaning

-- https://www.kaggle.com/datasets/swaptr/layoffs-2022

-- Steps
-- Step 1: Remove duplicates
-- Step 2: Standardize the Data
-- Step 3: Look for Null values or blank values
-- Step 4: Remove any columns aren't necessary


Select*
from layoffs;



-- creating staging table where you can edit data came from raw data this is for do overs
create table layoffs_staging
like layoffs;

Select*
from layoffs_staging;

insert layoffs_staging
select*
from layoffs;

-- Step 1: Remove duplicates
select *,
row_number() over(
partition by company, industry, total_laid_off, percentage_laid_off, 'date' ) as row_num
from layoffs_staging;

with duplicate_cte as
(
select *,
row_number() over(
partition by company, location,
industry, total_laid_off, percentage_laid_off, 'date', stage
, country, funds_raised_millions) as row_num
from layoffs_staging
)
select*
from duplicate_cte
where row_num > 1;

select*
from layoffs_staging
where company = 'Casper' ;

with duplicate_cte as
(
select *,
row_number() over(
partition by company, location,
industry, total_laid_off, percentage_laid_off, 'date', stage
, country, funds_raised_millions) as row_num
from layoffs_staging
)
delete
from duplicate_cte
where row_num > 1;


CREATE TABLE `layoffs_staging2` (
  `company` text,
  `location` text,
  `industry` text,
  `total_laid_off` int DEFAULT NULL,
  `percentage_laid_off` text,
  `date` text,
  `stage` text,
  `country` text,
  `funds_raised_millions` int DEFAULT NULL,
  `row_num` int
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

select*
from layoffs_staging2
where row_num > 1;

insert into layoffs_staging2
select *,
row_number() over(
partition by company, location,
industry, total_laid_off, percentage_laid_off, 'date', stage
, country, funds_raised_millions) as row_num
from layoffs_staging;



delete
from layoffs_staging2
where row_num > 1;

select*
from layoffs_staging2;


-- Step 2: Standardizing data
select company, trim(company)
from layoffs_staging2;

update layoffs_staging2
set company = trim(company);


select distinct industry
from layoffs_staging2
;

update layoffs_staging2
set industry = 'Crypto'
where industry like 'Crypto%';

select distinct country, trim(TRAILING '.' from country)
from layoffs_staging2
order by 1;

update layoffs_staging2
set country = trim(TRAILING '.' from country)
where country like 'United States%';

select `date`
from layoffs_staging2;


update layoffs_staging2
set `date` = str_to_date(`date`, '%m/%d/%Y');


alter table layoffs_staging2
modify column `date` DATE;

-- Step 3: Look for Null values or blank values and removing them
select *
from layoffs_staging2
where total_laid_off is NULL
and percentage_laid_off is NULL;

update layoffs_staging2
SET industry = NULL
where industry = '';

select *
from layoffs_staging2
where industry is NULL
OR industry = '';

select *
from layoffs_staging2
where company like 'Bally%';

select t1.industry, t2.industry
from layoffs_staging2 t1
join layoffs_staging2 t2
	on t1.company = t2.company
where (t1.industry is NULL or t1.industry = '')
and t2.industry is not NULL;

update layoffs_staging2 t1
join layoffs_staging2 t2
	on t1.company = t2.company
set t1.industry = t2.industry
where t1.industry is NULL
and t2.industry is not NULL;

select *
from layoffs_staging2;

select *
from layoffs_staging2
where total_laid_off is NULL
and percentage_laid_off is NULL;


delete
from layoffs_staging2
where total_laid_off is NULL
and percentage_laid_off is NULL;

-- Step 4: Remove any columns aren't necessary
select *
from layoffs_staging2;

alter table layoffs_staging2
drop column row_num;
