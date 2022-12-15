from fastapi import FastAPI,Request,Depends
from BlogPosts.routers import blog
from BlogPosts.routers import user
from BlogPosts.routers import authentication
from BlogPosts.routers import password_reset
from BlogPosts.routers import store
from BlogPosts.routers import item
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from BlogPosts.models import BlogPost,User,Item,Store,ItemImage,UserImage,PostImage
from sqlalchemy.orm import Session
from BlogPosts.database import get_db


app= FastAPI(
    docs_url = "/docs",
    redoc_url= "/redocs",
    title="SIRMUSO BLOGSITE API",
    description="FRAMEWORK FOR SIRMUSO BLOGSITE API",
    version="4.0",
    openapi_url="/api/v2/openapi.json"
    
)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)
app.include_router(store.router)
app.include_router(item.router)
app.include_router(password_reset.router)

templates = Jinja2Templates(directory="BlogPosts/templates")
app.mount("/static",StaticFiles(directory="Blogposts/static"),name="static")

@app.get('/',response_class=HTMLResponse,tags=["Display"])
def home(request: Request, db:Session = Depends(get_db)):
    blogs = db.query(BlogPost).all()
    images = db.query(UserImage).all()
    pimages = db.query(PostImage).all()
    return templates.TemplateResponse("home.html",{"request":request,"blogs":blogs,"pimages":pimages,"images":images})

@app.get('/users',response_class=HTMLResponse,tags=["Display"])
def get_users(request: Request, db:Session = Depends(get_db)):
    users = db.query(User).all()
    images = db.query(UserImage).all()
    return templates.TemplateResponse("users.html",{"request":request,"users":users,"images":images})

@app.get('/items',response_class=HTMLResponse,tags=["Display"])
def get_items(request: Request, db:Session = Depends(get_db)):
    items = db.query(Item).all()
    images = db.query(ItemImage).all()
    return templates.TemplateResponse("items.html",{"request":request,"items":items,"images":images})

@app.get('/store',response_class=HTMLResponse,tags=["Display"])
def get_stores(request: Request, db:Session = Depends(get_db)):
    stores = db.query(Store).all()
    return templates.TemplateResponse("store.html",{"request":request,"stores":stores})

@app.get('/content/{id}',response_class=HTMLResponse,tags=["Display"])
def get_items(id:int,request: Request, db:Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == id).first()
    image = db.query(ItemImage).filter(ItemImage.id == id).first()
    return templates.TemplateResponse("content.html",{"request":request,"item":item,"image":image})