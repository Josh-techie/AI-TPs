<p align="center">
<img src ="https://th.bing.com/th/id/OIP.n_ms1q5YoHAQXXUIfeADKQHaDG?rs=1&pid=ImgDetMain">
</p>
<p aling="center">

---

<h2> Pandas </h2>

- Pandas is a powerful open-source data manipulation and analysis library for Python. It provides easy-to-use data structures and data analysis tools, making it ideal for working with structured data. With Pandas, you can easily load, manipulate, and analyze data from various sources like CSV files, Excel spreadsheets, SQL databases, and more. It offers functionalities for filtering, grouping, merging, and reshaping data, as well as handling missing data. Pandas is widely used in data science, machine learning, and other fields where data processing is essential. It's a valuable tool for anyone working with data in Python projects.

---

<h2> Steps to follow to get started with Pandas </h2>

- Install the library if you're using vscode `pip install pandas`
  **NOTE**: If you're using google colab it's already preinstalled.
- Then import it in your code file
- Write your code using the library refering to it as `pd` and enjoy

---

<h2> DataFrames </h2>

- A dataframe is a two-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes (rows and columns). It is commonly used in data manipulation and analysis. In simple terms, you can think of a dataframe as a table where each column contains data of the same type, and each row represents a unique set of values. Refer to [DataFrames](./DataFrames.py) for the implementation , where we will be implementing this DataFrame.

<p align="center">
<img src ="https://www.notion.so/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F029a1497-45bd-4b48-af71-c2ab8a918091%2Ffc12b35d-334f-4e1e-9e3d-df604ee236fd%2FUntitled.png?table=block&id=9dfd9b48-e232-4066-a773-1260ac7e2129&spaceId=029a1497-45bd-4b48-af71-c2ab8a918091&width=2000&userId=9d08c749-75eb-439d-ad10-2a83e114a53b&cache=v2">
</p>

> You can also create a customed DataFrame for your data in pandas, as this will allow you to structure and organize your data in a way that suits your specific needs and analysis requirements, Refer [DataFrames](./DataFrames.py)

---

<p align="center">
<img src ="https://www.notion.so/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F029a1497-45bd-4b48-af71-c2ab8a918091%2Fa44a817f-0491-46c2-a6b2-311a6083b0c6%2FUntitled.png?table=block&id=d1398cae-cb7c-4344-9b88-b44e21aaac43&spaceId=029a1497-45bd-4b48-af71-c2ab8a918091&width=2000&userId=9d08c749-75eb-439d-ad10-2a83e114a53b&cache=v2">
</p>

<h2> Reading data from Files </h2>

- Reading data from files in pandas refers to the process of loading data into a pandas DataFrame from an external file. This file could be in various formats such as `CSV`, `Excel`, `SQL`, `JSON`, and more.

### Pandas provides several functions to read data from different file formats. For example:

- `pd.read_csv(filename)` is used to read data from a CSV file.
- `pd.read_excel(filename)` is used to read data from an Excel file.
- `pd.read_sql(query, connection_object)` is used to read data from a SQL table/database.
- `pd.read_json(json_string)` is used to read data from a JSON formatted string, URL or file.

> Once the data is loaded into a DataFrame, you can use pandas' powerful data manipulation and analysis capabilities on it.

## Let's try reading data from files, we'll be manipulating `csv` and `json` as examples, refer to [ReadingData](./ReadingData.py)

---

<h2> Real World Scenario </h2>

- In this part, I'll be manipulating a databse entitled [`imdb.csv`](./imdb.csv) which is a collection of movie data from the popular movie database, IMDb. Each row in the database represents a unique movie, with various details about each movie provided in the columns.

**The columns in the database are as follows:**

- `Rank`: The rank of the movie.
- `Title`: The title of the movie.
- `Genre`: The genre(s) of the movie, which can include multiple genres separated by commas.
- `Description`: A brief description or synopsis of the movie.
- `Director`: The director of the movie.
- `Actors`: The main actors in the movie, listed as a comma-separated list.
- `Year`: The year the movie was released.
- `Runtime (Minutes)`: The length of the movie in minutes.
- `Rating`: The IMDb rating of the movie.
- `Votes`: The number of votes the movie received.
- `Revenue (Millions)`: The revenue of the movie in millions of dollars.
- `Metascore`: The Metascore rating of the movie.

> From this database, I'll be performing the following operations: reading the database from the `CSV` file, viewing the database, obtaining information about the database using `info()`, understanding the variables, using `describe()` to get statistical summaries, examining relationships between continuous variables with `corr()`, slicing, selecting, and extracting data from the DataFrame, conditionally selecting data, applying functions to the DataFrame, sorting values, combining data through merging, joining, and concatenating, and grouping data for analysis.

**Don't it seems like a lot, but we'll understand this step by step in our code, refer to [imdb_manipulation](./imdb_manipulation.py) and the databse can be found [imdb.csv](./imdb.csv)**
