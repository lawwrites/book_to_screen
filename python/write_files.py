import pandas as pd
import os
import numpy as np
from datetime import date
import dataclasses
import csv

class CreateFile:
    today = date.today().strftime("%Y-%m-%d")
    
    def __init__(self, file_path, file_name, file_type):
        self.file_path = file_path
        self.file_name = file_name
        self.file_type = file_type
    
    def error_log(self, error):
        with open("error.txt", "a+") as error_doc:
            content = error_doc.write(f"{CreateFile.today} ERROR: {error}\n")     

    def create_file(self):
        try:
            #Construct full filename
            self.full_fn = f"{self.file_name}_{CreateFile.today}.{self.file_type}"
            #Construct full filepath
            self.full_path = os.path.join(self.file_path,self.full_fn)
            #Ensure directory exists
            os.makedirs(self.file_path, exist_ok=True)

            #Write to file
            with open(self.full_path, 'a+', newline = '') as csv_file:
                field_names = [
                    "book_id", "book_title", "author", "book_genre", "book_sales", "year",
                    "book_ig", "book_tiktok_book_trailer", "goodreads_score", "featured_lists", "book_awards",
                    "awards_id", "awards_title", "awards_category", "organization",
                    "script_writer_awards", "director_awards", "author_awards",
                    "film_id", "film_title", "film_genre", "director", "script_writer",
                    "film_budget", "box_office", "film_release", "film_youtube_views", "film_ig_follwers",
                    "film_trailer", "imdb_score", "rotten_tomatoes_score", "roger_ebert_score", "letter_boxd_score"]
                writer = csv.DictWriter(csv_file, fieldnames=field_names)
                writer.writeheader()
            print(f"{self.full_fn} successfully created")
        except Exception as e: 
           self.error_log(e)

class WriteFile(CreateFile):
    def __init__(self, file_path, file_name, file_type):
        super.__init__(file_path, file_name, file_type)



new_file = CreateFile('/Users/lawhea1214/Documents/portfolio/data_analysis/book_to_screen/data', 'b-to-p_data', 'csv')
new_file.create_file()