from fastapi import FastAPI
from fastapi.responses import HTMLResponse

blog_posts: list[dict] = [
    {
        "id": 1,
        "author": "Pat Thompson",
        "title": "Learning FastAPI",
        "content": "This is dummy content for learning purposes.",
        "date_posted": "1st August 2026"
    },
    {
        "id": 2,
        "author": "Lisa Thompson",
        "title": "Always tippy-tapping",
        "content": "You're a dummy Pazza!",
        "date_posted": "1st August 2026"
    }
]

app = FastAPI() 

# home route displaying as HTML with the number of blog posts available
@app.get("/", response_class=HTMLResponse, include_in_schema=False)  
def home():  
    return f"<h1>Welcome to this Blog!</h1><p>There are currently {len(blog_posts)} blog posts available.</p>" 

# api/blogposts route to get all blog posts - presented in JSON format if needed for programmatic access
@app.get("/api/blogposts")
def get_blog_posts():
    return {"data": blog_posts}

'''
posts route displaying specific blog post content
The function creates a variable called html_content that holds an H1 element.
The function then loops through the content of the blog_posts list and adds subsequent HTML elements for each post.
'''
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False) 

def posts():
    html_content = "<h1>Blog Posts</h1>"
    for post in blog_posts:
        html_content += f"<h2>{post['title']}</h2>"
        html_content += f"<p><strong>Author:</strong> {post['author']}</p>"
        html_content += f"<p><strong>Date Posted:</strong> {post['date_posted']}</p>"
        html_content += f"<p>{post['content']}</p>"
        html_content += "<hr>"
    return html_content


