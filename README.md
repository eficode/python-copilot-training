# Copilot Practice With Python

Practice using copilot by implementing a simple Python application.

## Exercise: Create a TODO file for yourself

Here is a sample first prompt to Copilot:

> @workspace /explain How would I begin to build a Flask app based on the example features #file:README.md?
> Don't implement any code yet. Suggest me a good architecture for the application.
> Don't modify requirements.txt file. Include an implementation strategy.

Next, you can use for example the following prompt to generate the TODO file for you:

> Create me a TODO.md file with the suggested implementation strategy as small individual steps.
> Include also architectural diagram and dataflow diagram. Use mermaid syntax.

:grey_exclamation: Note! The `mermaid` syntax is just an example. You can prompt it to generate whatever syntax you wish.

Review the generated steps and modify them as needed.
Now that you have your `TODO.md` file, you can start implementing the features in small steps. Happy coding!

## Exercise: Create a Flask Application

Your task is to create a Flask application that can parse any form of .csv data and visualize it inside the app. Follow these steps:

1. Set up a new Flask project.
2. Create a route that allows users to upload a .csv file.
    * Sample data can be found from the `data` directory.
3. Parse the uploaded .csv file and store the data.
4. Create a route to visualize the parsed data (e.g., using a table or a chart).

It's fine if you don't know how to use Flask or Copilot. The whole purpose of this repository is to learn how
to approach new topics with the help of Copilot.
Feel free to explore and utilize GitHub Copilot's features to assist you in writing the code for this exercise. Happy coding!

If you're struggling to get started, you can find a minimalistic example app from the `example_app` branch.

## Example Feature Enhancements

Here are some example features you can add to your application, ranging from beginner-friendly to more advanced:

**Easy:**

* **Display Basic Table:**
    * Enhance the visualization to display the CSV data in a basic HTML table.
    * **Resource:** Explore Jinja2 templating in Flask to render HTML tables.
* **Handle Different Delimiters:**
    * Allow users to specify the delimiter of the CSV file (e.g., comma, semicolon, tab).
    * **Resource:** `pandas.read_csv()` function has a `delimiter` parameter.
* **Display First N Rows:**
    * Add a feature to display only the first `N` rows of the CSV data.
    * **Resource:** Use `pandas.DataFrame.head(n)` to get the first n rows.

**Intermediate:**

* **Column Selection:**
    * Allow users to select which columns to display from the CSV file.
    * **Resource:** Use HTML checkboxes or a multi-select dropdown and Pandas column selection.
* **Data Filtering:**
    * Implement basic filtering functionality to allow users to filter the data based on column values.
    * **Resource:** Use Pandas boolean indexing to filter DataFrames.
* **Data Sorting:**
    * Add sorting capabilities to the table, allowing users to sort by column values.
    * **Resource:** Use `pandas.DataFrame.sort_values()` to sort DataFrames.
* **Simple Charts:**
    * Use a Python charting library like Matplotlib or Seaborn to create simple charts (e.g., bar charts, line charts) from the CSV data.
    * **Resource:** Matplotlib: `matplotlib.pyplot`, Seaborn.

**Advanced:**

* **Interactive Charts:**
    * Integrate an interactive charting library like Plotly or Bokeh to create dynamic visualizations.
    * **Resource:** Plotly, Bokeh.
* **REST API for Data Queries:**
    * Create a REST API endpoint to allow users to query specific data from the uploaded CSV file.
    * **Resource:** Flask-RESTful, Flask-API.
* **Advanced Filtering and Searching:**
    * Implement more advanced filtering and searching capabilities, such as regular expression matching or multiple filter criteria.
    * **Resource:** Pandas string methods, regular expressions.
* **Pagination:**
    * For large CSV files, implement pagination to display data in manageable chunks.
    * **Resource:** Implement pagination logic in your Flask routes and templates.
* **User Authentication:**
    * Add user authentication to restrict access to the application and uploaded data.
    * **Resource:** Flask-Login, Flask-Security.
* **Download Filtered Data:**
    * Allow users to download the filtered data as a new CSV file.
    * **Resource:** `pandas.DataFrame.to_csv()`, Flask `send_file()`.
