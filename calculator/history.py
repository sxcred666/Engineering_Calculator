import json 
import os 

# The History class manages the history of calculations performed by the calculator application. It allows adding new records, retrieving all records, retrieving the last n records, clearing the history, and saving/loading the history to/from a file in JSON format.
class History:
     MAX_RECORDS = 1000 # maximum number of records to keep in history

     def __init__(self, filename="history.json"):
          #file name - names the file where the history will be stored
          self.filename = filename
          # records - a list that will hold the history of calculations
          self.records = []
          #load histrory from file if it exists
          self.load()

     def add_record(self, expression, result):
          """Adds a new record to the history."""
          record = {
               "expression": expression, # the mathematical expression that was calculated
               "result": result # the result of the calculation
          }
          self.records.append(record) # add the new record to the list of records
          self.save() # save the updated history to the file

     def get_all(self):
          """Returns all records in the history."""
          return self.records
     
     def get_last(self, n=5):
          """Returns the last n records in the history."""
          return self.records[-n:] # return the last n records from the list
     
     def clear(self):
          """Clears the history."""
          self.records = [] # reset the records list to an empty list
          self.save() # save the cleared history to the file

     def save(self):
          """Saves the history to a file."""
          with open(self.filename, "w", encoding="utf-8") as f: # open the file in write mode
               json.dump(self.records, f, ensure_ascii=False, indent=2) # write the records to the file in JSON format

     def load(self):
          """Loads the history from a file."""
          if os.path.exists(self.filename): # check if the file exists
               with open(self.filename, "r", encoding="utf-8") as f: # open the file in read mode
                    self.records = json.load(f) # load the records from the file into the records list
          else:
               self.records = [] # if the file does not exist, initialize an empty records list


          