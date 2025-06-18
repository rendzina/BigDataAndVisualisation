#!/usr/bin/env python3
"""
access-mongo.py

This script demonstrates how to:
- Connect to a local MongoDB database using Python and pymongo
- Load data from a CSV file into a MongoDB collection (deleting any existing data first)
- Query the collection for documents where a specific field starts with a given letter
- Display the structure and contents of documents in a readable format

This example is designed for students learning about Python, MongoDB, and data handling. 
It uses the 'pymongo' library for MongoDB access and the built-in 'csv' module for CSV handling. 

Author: S.Hallett
Course: MKU, Big Data and Visualisation
Date: 18/06/2025
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
import pprint
import csv
import os


def connect_to_mongodb():
    """
    Establish a connection to the local MongoDB server and return the database and collection objects.
    Returns:
        tuple: (database, collection) if successful, (None, None) if failed
    """
    try:
        # Connect to MongoDB running on localhost at the default port 27017
        client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=2000)
        
        # Test the connection by sending a ping command
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        
        # Access the 'environmental' database and 'noise_mapping' collection
        db = client['environmental']
        collection = db['noise_mapping']
        
        return db, collection
        
    except ConnectionFailure:
        print("Could not connect to MongoDB. Please ensure MongoDB is running.")
        return None, None
    except ServerSelectionTimeoutError:
        print("Server selection timeout. Please check if MongoDB is running.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None, None


def load_csv_to_mongodb():
    """
    Load data from a CSV file into the MongoDB collection.
    This function will delete any existing data in the collection prior to loading new data.
    """
    db, collection = connect_to_mongodb()
    
    if db is None or collection is None:
        print("Failed to connect to MongoDB. Cannot load data.")
        return

    # CSV is downloaded from https://www.data.gov.uk/dataset/d461bbc1-eb51-4852-8a9a-45dbf28aa230/noise-exposure-data-round-3
    # Define the path to the CSV file
    csv_file_path = os.path.join('data', 'noise_mapping_round_3.csv')
    
    # Check if the CSV file exists
    if not os.path.exists(csv_file_path):
        print(f"CSV file not found at: {csv_file_path}")
        return
    
    try:
        # Delete all existing documents in the collection
        print("Clearing existing data from noise_mapping collection...")
        collection.delete_many({})
        print("Existing data cleared successfully.")
        
        # Read the CSV file using the built-in csv module
        print(f"Reading CSV file: {csv_file_path}")
        data = []
        
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                # Convert string values to appropriate types where possible
                for key, value in row.items():
                    # Try to convert numeric strings to integers
                    if value.isdigit():
                        row[key] = int(value)
                    # Handle 'n/a' values
                    elif value.lower() == 'n/a':
                        row[key] = None
                
                data.append(row)
        
        # Insert all records into the MongoDB collection
        print(f"Inserting {len(data)} documents into noise_mapping collection...")
        result = collection.insert_many(data)
        
        print(f"Successfully inserted {len(result.inserted_ids)} documents into the collection.")
        
    except Exception as e:
        print(f"Error loading CSV data: {str(e)}")


def main():
    """
    Main function to demonstrate querying MongoDB for documents where the
    'Location/Agglomeration' field starts with the letter 'M'.
    Also prints the structure of a sample document for reference.
    """
    db, collection = connect_to_mongodb()
    
    if db is not None and collection is not None:
        # Display the structure of a sample document to help you understand the data
        print("Checking document structure ...")
        sample_doc = collection.find_one()
        if sample_doc:
            print("Sample document fields:")
            for key in sample_doc.keys():
                print(f"  - {key}")
            #print(f"\nSample document:")
            #pprint.pprint(sample_doc, sort_dicts=False)
        else:
            print("No documents found in the collection to display structure.")
            return
        
        # Count the number of matching unfiltered documents
        total_doc_count = collection.count_documents({})
        print(f"Total number of documents in collection: {total_doc_count}")

        # Query for those documents where 'Location/Agglomeration' starts with 'M' (case-insensitive)
        # and return only the 'Location/Agglomeration' field
        print("\n" + "="*50)
        query_filter = {"Location/Agglomeration": {"$regex": r"^M", "$options": "i"}}
        projection = {"Location/Agglomeration": 1, "_id": 0}  # Only return Location/Agglomeration field
        results = collection.find(query_filter, projection)
        

        # Count the number of matching filtered documents
        filtered_doc_count = collection.count_documents(query_filter)
        print(f"Number of filtered documents starting with 'M': {filtered_doc_count}")
        
        # Print each matching document in a readable format
        print("Documents where 'Location/Agglomeration' starts with 'M':")
        found = False
        for doc in results:
            pprint.pprint(doc, sort_dicts=False)
            found = True
        if not found:
            print("No documents found.")


if __name__ == "__main__":
    # Comment or Uncomment the following line to load data from the CSV file into MongoDB.
    # This can be run once, or whenever you want to refresh the data.
    load_csv_to_mongodb()
    main() 