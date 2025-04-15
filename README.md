# Questions to explore

1. The budget of the films?
2. What genres get made most from book to screen?
3. How does the budget for genres compare?
4. How do fans engage with the books to film? Does one genre do better at satisfying fans than other? Or do fans hate when the genres are made? 
5. Who makes these film to screen adaptations? Agent, talent, agency? Authors? 
6. How big are the books or page count?
7. How did anthologies impact the films?
8. Which genres convert best from book to screen?
9. Do award-winning books outperform in film ratings?

# Steps to creating the project From Book to Screen ? 

1. Map out the entities, attributes, and relationships
2. Create a [ERD diagram](https://www.youtube.com/watch?v=UI6lqHOVHic)
3. Create Python Pseudo Code
4. Create the workflow chart
5. Create the Python OOBJ for project
6. Collect data in Excel
7. Export to .csvs
7. Create Jupyter notebook for the data
8. Import python program


# The project

## The business problem

 Focusing solely on books and films by people of color, the data uses Python, pandas, and other analytics libraries, to explore  the performance (financial and audience sentiment) of recent book-to-film adaptations. The goal is to identify patterns and factors contributing to success or failure. Ultimately, this delivers clear, actionable insights that could guide production companies when investing in stories centering people of color. 



## Database solutions

Admittedly even though MongoDB would be better served for the non-structured data, we are going to focus on cleaning and structuring the data with mySQL and Python Pandas.


### Entities:
The books and the films are the entities

### Attributes: 

### **Books**

- `book_id`
- `book_title`
- `author`
- `goodreads_score`
- `book_genre`
- `featured_lists`
- `awards`

### **Films**

- `film_id`
- `film_title`
- `imdb_score`
- `rotten_tomatoes_score`
- `roger_ebert_score`
- `letter_boxd_score`
- `film_budget`
- `script_writer`
- `director`
- `film_genre`
- `box-office`


### **Relationships**

**1-to-1:**

- `book` to `book_id`
- `film` to `film_id`
- `film` to `film_budget`
- `film` to `director`

**1-to-Many:**

- `book` to `films`
- `film` to `rank`
- `book` to `rank`
- `book` to `featured-lists`
- `film` to `awards`
- `book` to `awards`
- `film` to `script_writer`
- `book` to `author`




**Many-to-Many:**

- `series` to `anthologies`



# Pseudo Code

## Write Files

* Define file path: `book_to_screen/data/book-to-screen_data.csv`
* Import libraries: dataclass, pandas, numpy, os, csv, datatime
* Open and write to a `book-to-screen_data.csv`
* Write to `book-to-screen_data.csv` the columns:book_id, book_title, author, book_genre, book_sales, year, book_ig, book_tiktok_book_trailer, goodreads_score, featured_lists, book_awards, awards_id, awards_title, awards_category, organization, script_writer_awards, director_awards, author_awards, film_id, film_title, film_genre, director, script_writer, film_budget, box_office, film_release, film_youtube_views, film_ig_follwers, film_trailer, imdb_score, rotten_tomatoes_score, roger_ebert_score, letter_boxd_score
    * If field is empty, then add Nan values
* Create a dataclass decorator with the class Book
* For each row in book CSV
    * Convert the row to a Book object
    * Write files cleanly to a DB and CSV
* Try: 
    * Open or create `book-to-screen_data.csv` in append mode
    * For each row of data:
        * IF field is missing fill in NULL or NaN
        * Write row to `book-to-screen_data.csv` using column headers
* EXCEPT on error:
    * Create `error_log.txt` that appends errors to film, e.g., [2025-04-01 12:43] ERROR: Missing film_title at row 88 – KeyError: 'film_title'
    * Log the datetime, row index, and fullss
* Append updates to `book-to-screen_data.csv` with data 
* Save updates to `book-to-screen_data.csv` as a backup with datetime, e.g. `book-to-screen_data_YYYYMMDD.csv` 
* After all data is collected use a LEFT join to merge the database
