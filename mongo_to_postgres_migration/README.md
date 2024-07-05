# MongoDB to PostgreSQL Migration Guide

This guide provides detailed instructions on how to migrate data from MongoDB to PostgreSQL using the provided Python script.

<br>

## Prerequisites
- Ensure both MongoDB and PostgreSQL are installed and running. Otherwise, you can use cloud-based services like MongoDB Atlas and Amazon RDS.
- Have the necessary access credentials for both databases.

<br>

## Steps

1. **Configure MongoDB and PostgreSQL Connections:**
   - Update the `config.yaml` file with the correct MongoDB URI, database name, and collection name.
   - Provide the PostgreSQL database name, user, password, host, and port.

2. **Define Field Mapping:**
   - In the `config.yaml`, map the MongoDB fields to the corresponding PostgreSQL columns.

3. **Run the Migration Script:**
   - Execute the script using the following command:
     ```bash
     python mongo_to_postgres_migration.py
     ```

4. **Verify the Migration:**
   - Check the PostgreSQL database to ensure the data has been migrated correctly.

<br>

## Troubleshooting
- **Connection Issues:**
  - Ensure MongoDB and PostgreSQL are running and accessible.
  - Verify the connection details in `config.yaml`.

- **Data Issues:**
  - Ensure the field mappings in `config.yaml` are correct.
  - Check the logs for any errors during migration.

<br>

## Best Practices
- **Backup Data:**
  - Always backup your data before performing any migration.

- **Test Migration:**
  - Perform the migration on a test database first to ensure everything works as expected.

<br>

## Additional Resources
- [MongoDB Documentation](https://docs.mongodb.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

