from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI() 

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


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

@app.get("/", include_in_schema=False, name ="home") 
@app.get("/posts", include_in_schema=False, name ="posts") 
def home(request: Request):  
    return templates.TemplateResponse(request, "home.html", {"posts": blog_posts, "title": "Awesome Page!!!"})


@app.get("/api/blogposts")
def get_blog_posts():
    return {"data": blog_posts}


@app.get("/posts", include_in_schema=False) 
def posts():
    return blog_posts

