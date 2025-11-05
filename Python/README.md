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

This directory contains **2 main files** for MongoDB integration:

```text
Python/
├── README.md                 # This documentation file
├── access-mongo.py           # Main MongoDB integration script
├── pyMongo_cursor_prompts.md # MongoDB cursor and query examples
└── venv/                     # Virtual environment (created during setup)
```

> **📋 Important Note**: The script expects a `data/` directory containing `noise_mapping_round_3.csv`. This file is not included in the repository. You can download it from the [UK Government Data Portal](https://www.data.gov.uk/dataset/d461bbc1-eb51-4852-8a9a-45dbf28aa230/noise-exposure-data-round-3) and place it in a `data/` subdirectory within the `Python/` folder.

## Data Sources and Formats

### Environmental Noise Mapping Data

The project primarily works with environmental noise mapping data that includes the following fields:

- `Location/Agglomeration`:  Geographic location name
- `Road_Pop_Lden>=55dB`:     Population exposed to road noise at 55dB or higher
- `Road_Pop_Lnight>=50dB`:   Population exposed to road noise at night at 50dB or higher
- `Railways_Pop_Lden>=55dB`: Population exposed to railway noise at 55dB or higher
- `Industry_Pop_Lden>=55dB`: Population exposed to industrial noise at 55dB or higher
- `AgglomerationPopulation`: Total population of the agglomeration

### Supported Data Formats

- **CSV Files**: Primary data source format
- **JSON Documents**: MongoDB document structure
- **API Data**: Real-time environmental data feeds
- **Database Exports**: Existing MongoDB collections

## Usage

### 1. Prepare Data

Before loading data, you need to download the CSV file:

1. **Download the dataset**: Visit the [UK Government Data Portal](https://www.data.gov.uk/dataset/d461bbc1-eb51-4852-8a9a-45dbf28aa230/noise-exposure-data-round-3) and download the noise mapping data
2. **Create data directory**: Create a `data/` folder within the `Python/` directory
3. **Place CSV file**: Save the downloaded file as `noise_mapping_round_3.csv` in the `data/` folder

### 2. Loading Data

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

### 3. Running Queries

The main script demonstrates querying for documents where the location name starts with 'M':

```bash
python access-mongo.py
```

This will:

- Display the structure of documents in the collection
- Show the total number of documents
- Query for documents where `Location/Agglomeration` starts with 'M'
- Display the matching documents

### 4. Customising Queries

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
   - Download the CSV file from the [UK Government Data Portal](https://www.data.gov.uk/dataset/d461bbc1-eb51-4852-8a9a-45dbf28aa230/noise-exposure-data-round-3)
   - Create a `data/` directory in the `Python/` folder
   - Place the downloaded file as `noise_mapping_round_3.csv` in the `data/` directory
   - Verify the file path is correct

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
