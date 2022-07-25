# Full-stack App

## Lesson
Today, we'll be building a full-stack application, using React and Django.


### create django project

- create a django project as usual:
    - `python -m django startproject <project_name>`
    - set up custom user model
    - set `AUTH_USER_MODEL` in `settings.py`
    - create/run migrations
    - declare `STATICFILES_DIRS` in `settings.py`
- create a react project: `npm create vite`
- build the react project
    - vite needs to place static assets in a folder that django will serve them from, and vite needs to write URLs in our `index.html` that our django server will recognize. 
    - your index.html will be copied from `./index.html` to `<outDir>/index.html`
    - your compiled static assets (js, css) will minified, concatenated, and copied from `./src/*` to `<outDir>/assets/*`
    - your uncompiled static assets (images, sounds, videos) will be copied, unmodified, from  `./public/*` to  `./dist/*`

> Your `config.json` for vite might look a little like this:

```javascript
export default defineConfig({

  // vite uses this as a prefix for href and src URLs
  base: '/static/',
  build: {
    // this is the folder where vite will generate its output. Make sure django can serve files from here!
    outDir: '../shoe_proj/static',

    // delete the old build when creating the new build. 
    // this is the default behavior, unless outDir is outside of the current directory
    emptyOutDir: true,
  },
  plugins: [react()]
})
```