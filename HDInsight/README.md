# Microsoft Azure HDInsight Notebooks

## Overview

This directory contains specialised Jupyter notebooks designed for Microsoft Azure HDInsight clusters. These notebooks demonstrate enterprise-grade big data processing using Apache Spark in a cloud-based Hadoop environment, providing scalable and reliable data analytics capabilities.

## What is Azure HDInsight?

Azure HDInsight is a fully managed, full-spectrum, open-source analytics service for enterprises. It provides:
- **Apache Spark**: For fast data processing and machine learning
- **Apache Hadoop**: For distributed data storage and processing
- **Apache Hive**: For data warehousing and SQL-like queries
- **Apache Kafka**: For real-time streaming data processing
- **Enterprise Security**: Integration with Azure Active Directory and enterprise security features

## Getting Started

### Prerequisites

- **Azure Subscription**: Active Azure subscription with billing enabled
- **Azure HDInsight Cluster**: Running Spark cluster (see setup instructions below)
- **Azure Storage Account**: For data storage and notebook persistence
- **Basic Knowledge**: Understanding of Apache Spark and Python

### Setting Up HDInsight Cluster

1. **Create HDInsight Cluster**:
   - Log into Azure Portal
   - Create new HDInsight resource
   - Select Spark cluster type
   - Configure cluster size and settings
   - Set up storage account

2. **Access Jupyter Notebooks**:
   - Navigate to your HDInsight cluster
   - Click on "Cluster dashboards"
   - Select "Jupyter notebook"
   - Use your cluster credentials to log in

3. **Upload Notebooks**:
   - Download notebooks from this repository
   - Upload to Jupyter notebook interface
   - Ensure all dependencies are available

## Available Notebooks

| File | Description | Learning Objectives |
|------|-------------|-------------------|
| **HelloWorld.ipynb** | Basic Spark introduction in HDInsight environment | • HDInsight cluster setup<br>• Spark context initialisation<br>• Basic data operations<br>• Cluster resource management |
| **BristolCityCouncilPropertyExample_hdinsight.ipynb** | Complete property data analysis solution | • Large-scale data processing<br>• Property market analytics<br>• Data transformation pipelines<br>• Performance optimisation<br>• Enterprise data workflows |

## Key Features

### 🏢 **Enterprise-Grade Processing**
- Scalable cluster resources
- High availability and reliability
- Enterprise security integration
- Professional data processing workflows

### ⚡ **Performance Optimisation**
- Distributed computing capabilities
- Memory and CPU optimisation
- Parallel processing techniques
- Resource management strategies

### 🔒 **Security and Compliance**
- Azure Active Directory integration
- Role-based access control
- Data encryption at rest and in transit
- Audit logging and monitoring

### 📊 **Advanced Analytics**
- Machine learning capabilities
- Real-time data processing
- Complex data transformations
- Interactive data exploration

## HDInsight vs Colab Comparison

| Feature | Azure HDInsight | Google Colab |
|---------|----------------|--------------|
| **Environment** | Enterprise cloud cluster | Personal cloud notebook |
| **Scalability** | Highly scalable | Limited resources |
| **Security** | Enterprise-grade | Basic |
| **Cost** | Pay-per-use cluster | Free with limitations |
| **Use Case** | Production workloads | Learning and prototyping |
| **Integration** | Azure ecosystem | Google ecosystem |

## Best Practices

### Cluster Management
- **Right-size clusters**: Choose appropriate VM sizes and node counts
- **Auto-scaling**: Enable auto-scaling for variable workloads
- **Monitoring**: Use Azure Monitor for performance tracking
- **Cost optimisation**: Shut down clusters when not in use

### Data Processing
- **Partitioning**: Optimise data partitioning for performance
- **Caching**: Use Spark caching for frequently accessed data
- **Memory management**: Monitor and optimise memory usage
- **Error handling**: Implement robust error handling and recovery

### Security
- **Authentication**: Use Azure AD for user authentication
- **Authorization**: Implement role-based access control
- **Data protection**: Encrypt sensitive data
- **Audit trails**: Maintain comprehensive audit logs

## Troubleshooting

### Common Issues

1. **Cluster Creation Failures**
   - Check Azure subscription status
   - Verify resource provider registration
   - Ensure sufficient quota limits
   - Review network configuration

2. **Performance Issues**
   - Monitor cluster metrics
   - Optimise Spark configurations
   - Check data partitioning
   - Review resource utilisation

3. **Authentication Problems**
   - Verify Azure AD configuration
   - Check user permissions
   - Review cluster access policies
   - Ensure proper credential setup

### Getting Help

- **Azure Documentation**: Comprehensive HDInsight guides
- **Azure Support**: Professional support for enterprise issues
- **Community Forums**: Azure community discussions
- **Course Materials**: Refer to MK:U course resources

## Cost Considerations

### Cluster Costs
- **Compute costs**: VM instances and processing time
- **Storage costs**: Azure Storage for data and notebooks
- **Network costs**: Data transfer and bandwidth
- **Management overhead**: Cluster setup and maintenance

### Optimisation Strategies
- **Auto-scaling**: Scale down during idle periods
- **Spot instances**: Use lower-cost spot VMs when possible
- **Reserved instances**: Commit to longer-term usage
- **Resource monitoring**: Track and optimise resource usage

## Educational Objectives

These notebooks support learning in:
- **Enterprise Big Data**: Production-scale data processing
- **Cloud Computing**: Azure cloud platform utilisation
- **Distributed Computing**: Spark cluster management
- **Data Engineering**: Building data processing pipelines
- **Performance Tuning**: Optimising big data workloads

## Author

**S. Hallett**  
Course: MK:U, Big Data and Visualisation  
Date: 18/06/2025

---

*All notebooks use UK spelling conventions and follow enterprise coding standards for production environments.*
