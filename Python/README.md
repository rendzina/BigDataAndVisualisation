# MongoDB Noise Mapping Project

## Overview

This project demonstrates how to work with MongoDB using Python to store and query environmental noise mapping data. The project includes functionality to load CSV data into MongoDB collections and perform queries to extract specific information.

## Features

- **MongoDB Connection**: Connect to a local MongoDB instance
- **CSV Data Loading**: Load noise mapping data from CSV files into MongoDB collections
- **Data Querying**: Query documents based on specific criteria (e.g., location names starting with certain letters)
- **Data Visualisation**: Display document structure and contents in a readable format
- **Error Handling**: Comprehensive error handling for database connections and data operations

## Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.7+**: The project uses Python 3.13
- **MongoDB**: A local MongoDB instance running on the default port (27017)
- **Git**: For cloning the repository

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd test-mongo
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install required packages**:
   ```bash
   pip install pymongo pandas
   ```

## Project Structure

```
test-mongo/
├── README.md                 # This file
├── access-mongo.py          # Main Python script
├── data/                    # Data directory
│   └── noise_mapping_round_3.csv  # CSV data file
└── venv/                    # Virtual environment (created during setup)
```

## Data Format

The project works with noise mapping data that includes the following fields:

- `Location/Agglomeration`: Geographic location name
- `Road_Pop_Lden>=55dB`: Population exposed to road noise at 55dB or higher
- `Road_Pop_Lnight>=50dB`: Population exposed to road noise at night at 50dB or higher
- `Railways_Pop_Lden>=55dB`: Population exposed to railway noise at 55dB or higher
- `Industry_Pop_Lden>=55dB`: Population exposed to industrial noise at 55dB or higher
- `AgglomerationPopulation`: Total population of the agglomeration

## Usage

### 1. Loading Data

To load the CSV data into MongoDB:

```python
# In access-mongo.py, uncomment this line:
load_csv_to_mongodb()
```

This will:
- Connect to MongoDB
- Clear any existing data in the `noise_mapping` collection
- Load data from `data/noise_mapping_round_3.csv`
- Insert all records into the collection

### 2. Running Queries

The main script demonstrates querying for documents where the location name starts with 'M':

```bash
python access-mongo.py
```

This will:
- Display the structure of documents in the collection
- Show the total number of documents
- Query for documents where `Location/Agglomeration` starts with 'M'
- Display the matching documents

### 3. Customising Queries

You can modify the query in the `main()` function to search for different criteria:

```python
# Example: Find documents where location starts with 'L'
query_filter = {"Location/Agglomeration": {"$regex": r"^L", "$options": "i"}}

# Example: Find documents with population over 100,000
query_filter = {"AgglomerationPopulation": {"$gt": 100000}}
```

## Database Configuration

- **Database Name**: `environmental`
- **Collection Name**: `noise_mapping`
- **MongoDB Connection**: `mongodb://localhost:27017/`

## Error Handling

The script includes comprehensive error handling for:

- MongoDB connection failures
- Missing CSV files
- Data loading errors
- Query execution errors

## Educational Notes

This project is designed for educational purposes and demonstrates:

- **MongoDB Operations**: Connecting, inserting, querying, and counting documents
- **Python Database Programming**: Using the `pymongo` library
- **Data Processing**: Loading CSV data and converting between formats
- **Error Handling**: Graceful handling of common database and file operations
- **Code Documentation**: Comprehensive comments and docstrings using UK spelling conventions

## Troubleshooting

### Common Issues

1. **MongoDB Connection Failed**
   - Ensure MongoDB is running on your system
   - Check that it's accessible on port 27017
   - Verify your MongoDB installation

2. **CSV File Not Found**
   - Ensure the `data/noise_mapping_round_3.csv` file exists
   - Check the file path is correct

3. **Virtual Environment Issues**
   - Make sure the virtual environment is activated
   - Reinstall packages if needed: `pip install -r requirements.txt`

### Getting Help

If you encounter issues:

1. Check the error messages in the terminal output
2. Verify all prerequisites are installed
3. Ensure MongoDB is running
4. Check that the virtual environment is activated

## Contributing

This is an educational project. Feel free to:

- Add new query examples
- Improve error handling
- Add additional data processing features
- Enhance documentation

## License

This project is for educational purposes. Please ensure you have appropriate permissions for any data used.

## Author

**S. Hallett**  
Course: MKU, Big Data and Visualisation  
Date: 18/06/2025

---

*This README uses UK spelling conventions and code PEP8 conventions. It provides comprehensive documentation for students learning about Python, MongoDB, and data handling.* 