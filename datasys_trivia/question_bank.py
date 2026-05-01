"""
CompTIA Data Systems Trivia - Question Bank
Contains all trivia questions and helper functions for topic management.
"""

QUESTION_BANK = [
    {
        "id": 1,
        "question": "Which database type uses tables, rows, and columns?",
        "options": ["A. Non-relational", "B. Graph", "C. Relational", "D. Columnar"],
        "answer": "C",
        "topic": "Database Fundamentals",
        "difficulty": "Easy",
        "explanation": "Relational databases organize data into tables with rows and columns."
    },
    {
        "id": 2,
        "question": "Which NoSQL type stores data as key-value pairs?",
        "options": ["A. Graph", "B. Document", "C. Column", "D. Key-value"],
        "answer": "D",
        "topic": "Database Fundamentals",
        "difficulty": "Easy",
        "explanation": "Key-value stores use simple pairs for fast retrieval."
    },
    {
        "id": 3,
        "question": "Which database is best for relationship-heavy data like social networks?",
        "options": ["A. Relational", "B. Graph", "C. Key-value", "D. Column"],
        "answer": "B",
        "topic": "Database Fundamentals",
        "difficulty": "Medium",
        "explanation": "Graph databases focus on relationships between nodes."
    },
    {
        "id": 4,
        "question": "What does normalization primarily reduce?",
        "options": ["A. Data redundancy", "B. Data security", "C. Query speed", "D. Index size"],
        "answer": "A",
        "topic": "Database Design",
        "difficulty": "Easy",
        "explanation": "Normalization removes redundant data and improves structure."
    },
    {
        "id": 5,
        "question": "Which key uniquely identifies a record in a table?",
        "options": ["A. Foreign key", "B. Primary key", "C. Composite key", "D. Candidate key"],
        "answer": "B",
        "topic": "Database Design",
        "difficulty": "Easy",
        "explanation": "Primary keys uniquely identify records."
    },
    {
        "id": 6,
        "question": "Which ensures foreign keys match existing primary keys?",
        "options": ["A. Normalization", "B. Referential integrity", "C. Indexing", "D. Partitioning"],
        "answer": "B",
        "topic": "Database Design",
        "difficulty": "Easy",
        "explanation": "Referential integrity prevents invalid relationships."
    },
    {
        "id": 7,
        "question": "Which SQL command retrieves data?",
        "options": ["A. INSERT", "B. DELETE", "C. SELECT", "D. UPDATE"],
        "answer": "C",
        "topic": "SQL",
        "difficulty": "Easy",
        "explanation": "SELECT is used to query data."
    },
    {
        "id": 8,
        "question": "Which SQL command modifies existing data?",
        "options": ["A. UPDATE", "B. SELECT", "C. CREATE", "D. DROP"],
        "answer": "A",
        "topic": "SQL",
        "difficulty": "Easy",
        "explanation": "UPDATE modifies existing records."
    },
    {
        "id": 9,
        "question": "Which SQL clause filters rows?",
        "options": ["A. GROUP BY", "B. WHERE", "C. ORDER BY", "D. JOIN"],
        "answer": "B",
        "topic": "SQL",
        "difficulty": "Easy",
        "explanation": "WHERE filters rows based on conditions."
    },
    {
        "id": 10,
        "question": "Which SQL operation groups data for aggregation?",
        "options": ["A. WHERE", "B. GROUP BY", "C. ORDER BY", "D. JOIN"],
        "answer": "B",
        "topic": "SQL",
        "difficulty": "Easy",
        "explanation": "GROUP BY is used for aggregations."
    },
    {
        "id": 11,
        "question": "Which ACID principle ensures transactions are all-or-nothing?",
        "options": ["A. Consistency", "B. Atomicity", "C. Isolation", "D. Durability"],
        "answer": "B",
        "topic": "Transactions",
        "difficulty": "Medium",
        "explanation": "Atomicity ensures complete success or failure of a transaction."
    },
    {
        "id": 12,
        "question": "Which ACID principle ensures data is permanently saved after commit?",
        "options": ["A. Atomicity", "B. Consistency", "C. Isolation", "D. Durability"],
        "answer": "D",
        "topic": "Transactions",
        "difficulty": "Medium",
        "explanation": "Durability guarantees persistence after commit."
    },
    {
        "id": 13,
        "question": "Which ACID principle prevents transactions from interfering?",
        "options": ["A. Atomicity", "B. Consistency", "C. Isolation", "D. Durability"],
        "answer": "C",
        "topic": "Transactions",
        "difficulty": "Medium",
        "explanation": "Isolation ensures transactions are independent."
    },
    {
        "id": 14,
        "question": "Which backup type captures only changes since last backup?",
        "options": ["A. Full", "B. Differential", "C. Incremental", "D. Snapshot"],
        "answer": "C",
        "topic": "Backup & Recovery",
        "difficulty": "Medium",
        "explanation": "Incremental backups store only changes since the last backup."
    },
    {
        "id": 15,
        "question": "Which backup type requires only one additional file to restore after full?",
        "options": ["A. Incremental", "B. Differential", "C. Snapshot", "D. Synthetic"],
        "answer": "B",
        "topic": "Backup & Recovery",
        "difficulty": "Medium",
        "explanation": "Differential backups simplify restore process."
    },
    {
        "id": 16,
        "question": "Which encryption protects data during transmission?",
        "options": ["A. AES", "B. TLS", "C. RSA", "D. SHA"],
        "answer": "B",
        "topic": "Security",
        "difficulty": "Easy",
        "explanation": "TLS secures data in transit."
    },
    {
        "id": 17,
        "question": "Which masking technique is reversible?",
        "options": ["A. Anonymization", "B. Encryption", "C. Pseudonymization", "D. Tokenization"],
        "answer": "C",
        "topic": "Security",
        "difficulty": "Medium",
        "explanation": "Pseudonymization allows reversal under conditions."
    },
    {
        "id": 18,
        "question": "Which attack injects malicious SQL queries?",
        "options": ["A. DoS", "B. SQL Injection", "C. Phishing", "D. MITM"],
        "answer": "B",
        "topic": "Security",
        "difficulty": "Easy",
        "explanation": "SQL injection manipulates database queries."
    },
    {
        "id": 19,
        "question": "Which tool allows scripting multiple commands in Windows?",
        "options": ["A. CMD", "B. Bash", "C. PowerShell", "D. SQLCMD"],
        "answer": "C",
        "topic": "Scripting",
        "difficulty": "Easy",
        "explanation": "PowerShell supports multi-command scripting."
    },
    {
        "id": 20,
        "question": "Which language is primarily used for querying relational databases?",
        "options": ["A. Python", "B. SQL", "C. Java", "D. Bash"],
        "answer": "B",
        "topic": "Scripting",
        "difficulty": "Easy",
        "explanation": "SQL is the standard query language."
    },
    {
        "id": 21,
        "question": "Which architecture hosts databases on vendor-managed infrastructure?",
        "options": ["A. On-prem", "B. IaaS", "C. PaaS", "D. SaaS"],
        "answer": "C",
        "topic": "Deployment",
        "difficulty": "Medium",
        "explanation": "PaaS manages infrastructure for you."
    },
    {
        "id": 22,
        "question": "Which model represents tables, fields, and relationships logically?",
        "options": ["A. Conceptual", "B. Logical", "C. Physical", "D. Relational"],
        "answer": "B",
        "topic": "Database Design",
        "difficulty": "Medium",
        "explanation": "Logical models include fields and relationships."
    },
    {
        "id": 23,
        "question": "Which system aggregates data from multiple sources for reporting?",
        "options": ["A. Data lake", "B. Data mart", "C. Data warehouse", "D. OLTP"],
        "answer": "C",
        "topic": "Data Systems",
        "difficulty": "Medium",
        "explanation": "Data warehouses centralize data for reporting."
    },
    {
        "id": 24,
        "question": "Which system stores raw structured and unstructured data?",
        "options": ["A. Data warehouse", "B. Data mart", "C. Data lake", "D. OLAP"],
        "answer": "C",
        "topic": "Data Systems",
        "difficulty": "Medium",
        "explanation": "Data lakes store raw, unprocessed data."
    },
    {
        "id": 25,
        "question": "Which principle limits user access to only what is needed?",
        "options": ["A. Encryption", "B. Least privilege", "C. Authentication", "D. Isolation"],
        "answer": "B",
        "topic": "Security",
        "difficulty": "Easy",
        "explanation": "Least privilege minimizes access risk."
    },
    {
        "id": 26,
        "question": "A DBA needs to delete all records from a table quickly and without logging individual row deletions. Which command should be used?",
        "options": ["A. DELETE", "B. DROP", "C. TRUNCATE", "D. REMOVE"],
        "answer": "C",
        "topic": "SQL",
        "difficulty": "Medium",
        "explanation": "TRUNCATE removes all rows efficiently and does not log individual row deletions like DELETE."
    },
    {
        "id": 27,
        "question": "A database must support fast analytical queries across large datasets such as sales trends. Which database type is BEST suited?",
        "options": ["A. Row-based relational", "B. Column-oriented", "C. Graph", "D. Key-value"],
        "answer": "B",
        "topic": "Database Fundamentals",
        "difficulty": "Medium",
        "explanation": "Column-oriented databases are optimized for analytics and OLAP workloads."
    },
    {
        "id": 28,
        "question": "A DBA creates an index on a frequently queried column. What is the primary benefit?",
        "options": ["A. Increased storage capacity", "B. Faster data retrieval", "C. Improved data security", "D. Reduced normalization"],
        "answer": "B",
        "topic": "Performance",
        "difficulty": "Easy",
        "explanation": "Indexes improve query performance by enabling faster data lookup."
    },
    {
        "id": 29,
        "question": "Which join returns only matching records between two tables?",
        "options": ["A. LEFT JOIN", "B. RIGHT JOIN", "C. FULL JOIN", "D. INNER JOIN"],
        "answer": "D",
        "topic": "SQL",
        "difficulty": "Easy",
        "explanation": "INNER JOIN returns only rows with matching values in both tables."
    },
    {
        "id": 30,
        "question": "A company wants to ensure that database changes can be reversed if an error occurs during processing. Which SQL feature supports this?",
        "options": ["A. Indexing", "B. Transactions", "C. Views", "D. Constraints"],
        "answer": "B",
        "topic": "Transactions",
        "difficulty": "Medium",
        "explanation": "Transactions allow rollback to undo changes if errors occur."
    },
    {
        "id": 31,
        "question": "Which type of data model shows high-level relationships without detailed attributes?",
        "options": ["A. Physical", "B. Logical", "C. Conceptual", "D. Dimensional"],
        "answer": "C",
        "topic": "Database Design",
        "difficulty": "Medium",
        "explanation": "Conceptual models provide a high-level overview without detailed fields."
    },
    {
        "id": 32,
        "question": "A system automatically deletes related child records when a parent record is removed. What is this called?",
        "options": ["A. Referential integrity", "B. Cascade delete", "C. Normalization", "D. Indexing"],
        "answer": "B",
        "topic": "Database Design",
        "difficulty": "Medium",
        "explanation": "Cascade delete removes related records automatically."
    },
    {
        "id": 33,
        "question": "Which scripting environment is native to Linux systems?",
        "options": ["A. PowerShell", "B. Bash", "C. CMD", "D. SQLCMD"],
        "answer": "B",
        "topic": "Scripting",
        "difficulty": "Easy",
        "explanation": "Bash is the primary shell scripting environment in Linux."
    },
    {
        "id": 34,
        "question": "A DBA monitors CPU, memory, and disk usage to identify performance bottlenecks. What is this process called?",
        "options": ["A. Load balancing", "B. Monitoring resource utilization", "C. Normalization", "D. Indexing"],
        "answer": "B",
        "topic": "Performance",
        "difficulty": "Easy",
        "explanation": "Monitoring resource utilization helps identify performance issues."
    },
    {
        "id": 35,
        "question": "A company uses multiple servers to distribute database traffic evenly. What technique is being used?",
        "options": ["A. Replication", "B. Load balancing", "C. Normalization", "D. Partitioning"],
        "answer": "B",
        "topic": "Performance",
        "difficulty": "Medium",
        "explanation": "Load balancing distributes workloads across servers to improve performance and availability."
    }
]

# Generate topics dynamically from question bank
# Note: TOPICS is computed at module load time and assumes QUESTION_BANK is static
# If QUESTION_BANK is modified at runtime, TOPICS will become stale
TOPICS = sorted({q["topic"] for q in QUESTION_BANK})

# Generate difficulties dynamically from question bank
DIFFICULTIES = sorted({q["difficulty"] for q in QUESTION_BANK})


def get_questions_by_topic(topics):
    """Filter questions by selected topics."""
    if not topics:
        return QUESTION_BANK
    return [q for q in QUESTION_BANK if q["topic"] in topics]


def get_questions_by_difficulty(difficulty):
    """Filter questions by difficulty level."""
    return [q for q in QUESTION_BANK if q["difficulty"] == difficulty]
