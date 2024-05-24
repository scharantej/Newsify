
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = Article.query.get(article_id)
    return render_template('article.html', article=article)

@app.route('/add_article', methods=['POST'])
def add_article():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        date = request.form['date']
        content = request.form['content']

        article = Article(title=title, author=author, date=date, content=content)
        db.session.add(article)
        db.session.commit()
        flash('Article added successfully!')
        return redirect(url_for('index'))

@app.route('/edit_article/<int:article_id>', methods=['POST'])
def edit_article(article_id):
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        date = request.form['date']
        content = request.form['content']

        article = Article.query.get(article_id)
        article.title = title
        article.author = author
        article.date = date
        article.content = content
        db.session.commit()
        flash('Article updated successfully!')
        return redirect(url_for('index'))

@app.route('/delete_article/<int:article_id>')
def delete_article(article_id):
    article = Article.query.get(article_id)
    db.session.delete(article)
    db.session.commit()
    flash('Article deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
