## Flask Application Design for News Articles Display

### HTML Files

- **index.html**: The main HTML file that displays the recent news articles. It includes a header, a body section to show the articles, and a footer.
- **article.html**: A template for displaying individual news articles. It includes the article's title, author, date, and content.

### Routes

- **@app.route('/')**: The root route that serves the `index.html` file.
- **@app.route('/article/<int:article_id>')**: A route to display an individual news article. It takes the article's ID as a parameter and uses it to fetch the article from the database. The route then renders the `article.html` template with the fetched article.
- **@app.route('/add_article', methods=['POST'])**: A route to add a new news article. It handles POST requests and validates the form data before adding the article to the database.
- **@app.route('/edit_article/<int:article_id>', methods=['POST'])**: A route to edit an existing news article. It takes the article's ID as a parameter, fetches the article from the database, and allows the user to edit it. The route handles POST requests to update the article.
- **@app.route('/delete_article/<int:article_id>')**: A route to delete an existing news article. It takes the article's ID as a parameter, fetches the article from the database, and deletes it.