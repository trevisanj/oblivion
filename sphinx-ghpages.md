# Sphinx building into gh-pages branch

:notes: Make clone of repository somewhere, but new directory has to be named `html`

:notes: Modify Sphink `Makefile` to build into that new directory

:notes: Enter directory `html` and switch to branch gh-pages

:notes: Touch `.nojekyll`

:notes: Create file 404.html with contents:

    <meta http-equiv="refresh" content="0; url=http://example.com/" />

This thing will allow access to `http://username.github.io/projectname` without `index.html`

References:

https://daler.github.io/sphinxdoc-test/includeme.html

http://stackoverflow.com/questions/5411538/redirect-from-an-html-page
