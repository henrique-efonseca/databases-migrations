# Databases Migrations

Scripts and tools for migrating data between different databases. This repository currently includes a migration script for MongoDB to PostgreSQL, with plans to support more database migrations in the future.

<br>

## Features
- Easy configuration using a YAML file
- Error handling during the migration process
- Flexible and extensible to support multiple database types

<br>

## Available Migrations
| Source Database | Target Database | Script Reference                       |
|-----------------|-----------------|----------------------------------------|
| MongoDB         | PostgreSQL      | [MongoDB to PostgreSQL Migration](./mongo_to_postgres_migration/README.md) |

<br>

## Requirements
- Python 3.x
- pymongo
- psycopg2
- pyyaml

<br>

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/databases-migrations.git
   cd databases-migrations
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Configure the migration script as per the instructions in the respective migration guide.

<br>

## Usage
1. Configure the migration script as per the instructions in the respective migration guide.
2. Run the migration script using the appropriate command. Example :
    ```bash
    cd mongo_to_postgres_migration
    python mongo_to_postgres_migration.py
    ```
3. Verify the migration by checking the target database.

<br>

## Contributing
Contributions are welcome!
Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

<br>

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

