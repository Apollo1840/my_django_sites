# My Django Sites

This repository:
- records my practicing process of utilizing django
- provide several django projects template.


## Projects:

| Project | Description |
|----------|----------|
| django_init   | A hello world app without utility. |
| CommunityBlogs   | A basic django project with User system & Blog system.  |
| CommunityBlogs2    | **(Django + MongoDB)** BlogCommunity with mongoDB as database. |
| HousePart  | **(Django + React)** A basic django project with React components. |
| TaskManagement  | **(Django + React + MongoDB)** A simple project. |
| TaskManagementD  | Dockerize TaskManagement. |

## Technologies

There are two ways to incorporate Django and React:
- (Django / React) Frontend fully supported by React, Django serve as Data API.
- (Django + React) Framework of the Frontend supported by Django. Frontend has some React components.

### Django + React

A typical approach is: 
Use **Webpack** to bundle all **React** components to `./static` (in detail, into the `./static/frontend/main.js`), 
and use **Django** to host a `index.html` which imports the `./static` (obviously, import `./static/frontend/main.js`).


## Reference

---

Django Tutorial: https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&ab_channel=CoreySchafer
Code: 

---

React + Django Tutorial: https://www.youtube.com/watch?v=JD-age0BPVo&list=PLzMcBGfZo4-kCLWnGmK0jUBmGLaJxvi4j&ab_channel=TechWithTim
Code: https://github.com/techwithtim/Music-Controller-Web-App-Tutorial