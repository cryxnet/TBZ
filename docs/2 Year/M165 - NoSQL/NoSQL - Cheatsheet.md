## Definition
-   NoSQL is a database approach that provides flexible data models and scalability for handling large amounts of unstructured and semi-structured data.
-   NoSQL databases prioritize scalability, performance, and high availability.
- It indicates literally every database that doesn't use SQL.

##  Key Characteristics

-   Schema-less: No predefined schema; allows flexible and dynamic data structures.
-   Distributed Architecture: Data is distributed across multiple nodes to achieve scalability and fault tolerance.
-   High Scalability: Designed to handle massive amounts of data and concurrent users.
-   Flexible Data Models: Supports various data models like key-value, document, columnar, and graph.
-   Horizontal Scaling: Scales horizontally by adding more machines to the system.

##  Common NoSQL Databases

-   Document Databases: MongoDB
-   Key-Value Databases: Redis
-   Columnar Databases: Cassandra, HBase
-   Graph Databases: Neo4j, Amazon Neptune

## MongoDB

### Installation
- Download MongoDB Community Edition: [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)
- Extract the downloaded archive and add the MongoDB binaries to the system PATH.
- Or just run a docker container (its better)

### Starting MongoDB CLI
- Open a command prompt or terminal.
- Run the following command to start the MongoDB CLI:
  ```
  mongo
  ```

### Connecting to MongoDB
- By default, the MongoDB CLI connects to a MongoDB server running on `localhost` and port `27017`.
- Connect to a specific server and port:
  ```
  mongo --host <hostname>:<port>
  ```

### Switching Databases
- Use the `use` command to switch to a specific database:
  ```
  use <database_name>
  ```

### Working with Collections
- **Show all collections in the current database:**
  ```
  show collections
  ```

- **Create a new collection:**
  ```
  db.createCollection("<collection_name>")
  ```

### Querying Documents
- **Find all documents in a collection:**
  ```
  db.<collection_name>.find()
  ```

- **Find documents matching a specific condition:**
  ```
  db.<collection_name>.find({ <field>: <value> })
  ```

- **Find a single document in a collection:**
  ```
  db.<collection_name>.findOne({ <field>: <value> })
  ```

### Inserting Documents
- **Insert a document into a collection:**
  ```
  db.<collection_name>.insertOne({ <field>: <value> })
  ```

### Updating Documents
- **Update a document in a collection:**
  ```
  db.<collection_name>.updateOne({ <field>: <value> }, { $set: { <field>: <new_value> } })
  ```

### Deleting Documents
- **Delete a document from a collection:**
  ```
  db.<collection_name>.deleteOne({ <field>: <value> })
  ```

### Indexing
- **Create an index on a field in a collection:**
  ```
  db.<collection_name>.createIndex({ <field>: 1 })
  ```

### Aggregation Framework

**Aggregation Keys:**

-   `$match`: Filters documents based on specified criteria.
-   `$group`: Groups documents by a specified key and performs aggregations on grouped data.
-   `$project`: Shapes the output documents by specifying the inclusion/exclusion of fields and creating computed fields.
-   `$sort`: Sorts documents based on specified criteria.
-   `$limit`: Limits the number of documents passed to the next stage.
-   `$skip`: Skips a specified number of documents and passes the remaining documents to the next stage.
-   `$unwind`: Deconstructs an array field into multiple separate documents.
-   `$lookup`: Performs a left outer join on two collections.
-   `$addFields`: Adds new fields to the documents with specified values.
-   `$replaceRoot`: Replaces the document with the specified embedded document.
-   `$group` Accumulator Operators: `$sum`, `$avg`, `$min`, `$max`, `$push`, `$addToSet`, `$first`, `$last`, and more.

- **Perform aggregation operations on a collection:**
  ```
  db.<collection_name>.aggregate([ { $match: { <field>: <value> } }, { $group: { _id: "$<field>", count: { $sum: 1 } } } ])
  ```

### Exit MongoDB CLI
- **To exit the MongoDB CLI, run:**
  ```
  exit
  ```
