# HouseParty MusicController

This is a Django + React project.

## project tech
Use webpack to bundle all React components to `./static` (in detail, into the `./static/frontend/main.js`), 
and use django to host a `index.html` which imports the `./static` (obviously, import `./static/frontend/main.js`).

## project init

```bash
npm init -y
```

## Preparation


install django related dependencies: 

```bash
  
    # create venv (if needed)
    conda create --name web python=3 -y
    conda activate web
    
    # install packages
    pip3 install -r requirements.txt
    
    # prepare django app
    python manage.py makemigrations
    python manage.py migrate

```

install react related dependencies:

```bash
npm i react react-dom --save-dev
npm i react-router-dom

npm i webpack webpack-cli --save-dev

npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
npm i @babel/plugin-proposal-class-properties 

npm i @material-ui/core
npm i @material-ui/icons
```
