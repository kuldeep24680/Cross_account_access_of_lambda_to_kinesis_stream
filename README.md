This project is used to establish a cross aws account access from account1 (AccountID:1111111) to account2 (AccountID:2222222). Here, the objective is to allow the lambda function in account1 to ingest JSON format datarecords into Kinesis stream in account2.

The project contains:
1. Policy in account2 to allow access to stream
2. Trust Relationship for account2 IAM role
3. policy in account1 to establish STS connection from account1 to account2
4. Trust relationship for account1 IAM role
5. Python code for lambda fucntion to ingest sample datarecords to kinesis stream in account2.

