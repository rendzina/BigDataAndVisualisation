# Python and MongoDB Integration Project

## Overview

This directory contains Python-based examples and tutorials for working with MongoDB databases, focusing on environmental data analysis and noise mapping. The project demonstrates comprehensive database operations, data processing workflows, and integration between Python applications and MongoDB databases.

## Key Features

- **MongoDB Integration**: Complete Python-MongoDB connectivity and operations
- **Environmental Data Analysis**: Specialised noise mapping and environmental data processing
- **Data Pipeline Development**: End-to-end data processing workflows
- **Advanced Querying**: Complex database queries and aggregation pipelines
- **Data Visualisation**: Interactive charts and graphs for data insights
- **Error Handling**: Robust error handling and logging for production environments

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
Python/
├── README.md                 # This documentation file
├── access-mongo.py          # Main MongoDB integration script
├── pyMongo_cursor_prompts.md # MongoDB cursor and query examples
├── data/                    # Data directory (if applicable)
│   └── noise_mapping_round_3.csv  # Environmental noise mapping dataset
└── venv/                    # Virtual environment (created during setup)
```

## Data Sources and Formats

### Environmental Noise Mapping Data

The project primarily works with environmental noise mapping data that includes the following fields:

- `Location/Agglomeration`: Geographic location name
- `Road_Pop_Lden>=55dB`: Population exposed to road noise at 55dB or higher
- `Road_Pop_Lnight>=50dB`: Population exposed to road noise at night at 50dB or higher
- `Railways_Pop_Lden>=55dB`: Population exposed to railway noise at 55dB or higher
- `Industry_Pop_Lden>=55dB`: Population exposed to industrial noise at 55dB or higher
- `AgglomerationPopulation`: Total population of the agglomeration

### Supported Data Formats

- **CSV Files**: Primary data source format
- **JSON Documents**: MongoDB document structure
- **API Data**: Real-time environmental data feeds
- **Database Exports**: Existing MongoDB collections

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

## Educational Objectives

This project is designed for educational purposes and demonstrates:

- **Database Operations**: MongoDB connectivity, CRUD operations, and advanced querying
- **Python Programming**: Professional Python development with database integration
- **Data Processing**: ETL workflows, data transformation, and format conversion
- **Error Handling**: Production-grade error handling and logging practices
- **Code Documentation**: Comprehensive documentation following UK spelling conventions
- **Best Practices**: Industry-standard database programming techniques

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

## Advanced Features

### MongoDB Aggregation Pipelines
- Complex data transformation workflows
- Multi-stage data processing
- Performance optimisation techniques
- Advanced query patterns

### Data Visualisation
- Interactive charts and graphs
- Geographic data mapping
- Real-time data dashboards
- Custom visualisation components

### API Integration
- RESTful API development
- Real-time data streaming
- External service integration
- Data synchronisation workflows

## Contributing

This is an educational project designed for students at MK:U. Contributions that enhance learning outcomes are welcome, including:

- Additional database operation examples
- Enhanced error handling and logging
- New data processing workflows
- Improved documentation and tutorials
- Performance optimisation techniques

## License

This project is for educational purposes. Please ensure you have appropriate permissions for any data used.

## Author

**S. Hallett**  
Course: MKU, Big Data and Visualisation  
Date: 18/06/2025

---

*This README uses UK spelling conventions and code PEP8 conventions. It provides comprehensive documentation for students learning about Python, MongoDB, and data handling.* 