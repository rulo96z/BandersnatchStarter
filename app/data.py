from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    """
    Database class for interacting with a MongoDB collection.
    
    Attributes:
        client (MongoClient): MongoDB client instance.
        db (pymongo.database.Database): MongoDB database instance.
        collection (pymongo.collection.Collection): MongoDB collection instance.

    Methods:
        __init__(): Initializes the Database object by connecting to MongoDB.
        seed(amount: int): Inserts a specified number of Monster documents into the collection.
        reset(): Deletes all documents in the collection.
        count() -> int: Returns the count of documents in the collection.
        dataframe() -> DataFrame: Retrieves all documents from the collection and returns them as a pandas DataFrame.
        html_table() -> str: Converts the DataFrame obtained from 'dataframe()' to an HTML table representation.
    """

    def __init__(self):
        """
        Initializes the Database object by loading MongoDB connection details from environment variables.
        """
        load_dotenv()

        db_url = getenv("DB_URL")
        db_name = getenv("DB_NAME")
        collection_name = getenv("COLLECTION_NAME")

        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def seed(self, amount):
        """
        Inserts a specified number of Monster documents into the collection.
        
        Args:
            amount (int): The number of Monster documents to insert.
        """
        self.collection.insert_many(
            [Monster().to_dict() for _ in range(amount)]
        )

    def reset(self):
        """
        Deletes all documents in the collection.
        """
        self.collection.delete_many({})

    def count(self) -> int:
        """
        Returns the count of documents in the collection.
        
        Returns:
            int: The count of documents in the collection.
        """
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """
        Retrieve all documents from the collection and convert them into a pandas DataFrame.

        Returns:
            DataFrame:
                A pandas DataFrame containing the documents from the collection.
                The '_id' column is dropped for visualization purposes.
        """
        cursor = self.collection.find()
        data = list(cursor)
        df = DataFrame(data)

        # Drop '_id' column for visualization purposes
        df = df.drop("_id", axis=1)
        return df


    def html_table(self) -> str:
        """
        Converts the DataFrame obtained from 'dataframe()' to an HTML table representation.

        Returns:
            str: HTML representation of the DataFrame as a table.
        """
        df = self.dataframe()
        return df.to_html(index=True)


#if __name__ == '__main__':
    #db = Database()
    #db.seed(1000)
    #db.reset()
