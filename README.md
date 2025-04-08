# Questions to explore

1. The budget of the films?
2. What genres get made most from book to screen?
3. How does the budget for genres compare?
4. How do fans engage with the books to film? Does one genre do better at satisfying fans than other? Or do fans hate when the genres are made? 
5. Who makes these film to screen adaptations? Agent, talent, agency? Authors? 
6. How big are the books or page count?
7. How did anthologies impact the films? 

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
- `author_tiktok`
- `author_ig`
- `book_genre`
- `featured_lists`
- `awards`
- `author-awards`
- `book_sales`

### **Films**

- `film_id`
- `film_title`
- `imdb_score`
- `rotten_tomatoes_score`
- `roger_ebert_score`
- `letter_boxd_score`
- `youtube_views`
- `ig_followers`
- `film_budget`
- `script_writer`
- `director`
- `film_genre`
- `director-awards`
- `box-office`


### **Relationships**

**1-to-1:**

- `book` to `book_id`
- `film` to `film_id`
- `book` to `production_studio`
- `film` to `imdb_score`
- `film` to `rotten_tomatoes_score`
- `book` to `goodreads_score`
- `film` to `trailers`
- `trailer` to `views`
- `film` to `film_budget`
- `film` to `director`
- `film` to `letterboxd`
- `book` to `sales`
- `book` to `deal`

**1-to-Many:**

- `book` to `films`
- `film` to `script_writers`
- `book` to `featured-lists`
- `book` to `awards`
- `film` to `awards`
- `author` to `awards`
- `director` to `awards`




**Many-to-Many:**

- `series` to `anthologies`

