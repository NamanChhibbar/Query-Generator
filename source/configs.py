# Chat completion model used for generation
MODEL = "gpt-4"

# System message sent to model
SYSTEM_MESSAGE = 'You are a data scientist and work with SQL databases. You will receive some table schemas and atmost 3 sample rows of the table. Each row of a table schema corresponds to an attribute in the table. Ignore attributes of the name "mysql_created_on". Create an SQL query to answer the given question. Provide only the query in the response without any explaination.'

# Set previous messages with model
# A message must be a dictionary with "role" and "content" keys
# "role" can be "user" or "assistant", "content" contains the message by the user/assistant
# First message must be from the user
PREVIOUS_MESSAGES = []

# Set path to env
PATH_TO_ENV = "/Users/naman/Desktop/Code/Python/QueryGeneration/credentials.env"
