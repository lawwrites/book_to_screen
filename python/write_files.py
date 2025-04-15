import pandas as pd
import os
import numpy as np
from datetime import date
import dataclasses
import csv
import random

class CreateFile:
    today = date.today().strftime("%Y-%m-%d")
    header = [
                    "book_id", "book_title", "author", "book_genre", "year",
                    "goodreads_score", "featured_lists", "book_awards",
                    "awards_id", "awards_title", "awards_category", "organization",
                    "script_writer_awards", "director_awards", "author_awards",
                    "film_id", "film_title", "film_genre", "director", "script_writer",
                    "film_budget", "box_office", "film_release", 
                    "imdb_score", "rotten_tomatoes_score", "roger_ebert_score", "letter_boxd_score"]
    
    #initialize the object
    def __init__(self, file_path, file_name, file_type):
        self.file_path = file_path
        self.file_name = file_name
        self.file_type = file_type
        #Construct full filename
        self.full_fn = f"{self.file_name}_{CreateFile.today}.{self.file_type}"
        #Construct full filepath
        self.full_path = os.path.join(self.file_path,self.full_fn)
            
    #create an error log that logs the errors
    def error_log(self, error):
        with open("error.txt", "a+") as error_doc:
            content = error_doc.write(f"{CreateFile.today} ERROR: {error}\n")     

    def create_file(self):
        try:
           #Ensure directory exists
            os.makedirs(self.file_path, exist_ok=True)
            #Write to file
            with open(self.full_path, 'a+', newline = '') as csv_file:
          
                writer = csv.DictWriter(csv_file, fieldnames=CreateFile.header)
                writer.writeheader()
            print(f"{self.full_fn} successfully created")
        except Exception as e: 
           self.error_log(e)

class WriteFile(CreateFile):
    def __init__(self, file_path, file_name, file_type, data):
        super().__init__(file_path, file_name, file_type)
        self.data = data

    #Creating the datafile that will write
    def data_writer(self):
        try:
            os.makedirs(self.file_path, exist_ok=True)
            with open(self.full_path, "a", newline='') as output:
                writer = csv.DictWriter(output, fieldnames = self.data[0].keys())
                writer.writerows(self.data) #takes the data
        except Exception as e:
            self.error_log(e)



class ReadFile(CreateFile):
    def __init__(self, file_path, file_name, file_type):
        super().__init__(file_path, file_name, file_type)
       pass

    def file_reader(self):
       pass



test_data = {
    "book_id": 10001,
    "book_title": "Midnight in the Maple Grove",
    "author": "Jordan Blake",
    "book_genre": "Fantasy",
    "year": 2021,
    
    "goodreads_score": 4.5,
    "featured_lists": "Goodreads Choice Awards, Indie Next List",
    "book_awards": "Fantasy Book of the Year",
    
    "awards_id": 301,
    "awards_title": "Best Adapted Screenplay",
    "awards_category": "Screenwriting",
    "organization": "Academy Awards",
    
    "script_writer_awards": "Oscar Nominee",
    "director_awards": "Cannes Jury Prize",
    "author_awards": "Nebula Award Finalist",
    
    "film_id": 70010,
    "film_title": "Midnight in the Maple Grove",
    "film_genre": "Fantasy/Adventure",
    "director": "Sasha Kim",
    "script_writer": "Lee Tran",
    
    "film_budget": 60000000,
    "box_office": 220000000,
    "film_release": "2024-07-12",
    
    "imdb_score": 8.1,
    "rotten_tomatoes_score": 91,
    "roger_ebert_score": 4.0,
    "letter_boxd_score": 4.2
}


new_file = CreateFile('/Users/lawhea1214/Documents/portfolio/data_analysis/book_to_screen/data', 'b-to-p_data', 'csv')
new_file.create_file()
new_file = WriteFile()
new_file.data_writer(test_data)