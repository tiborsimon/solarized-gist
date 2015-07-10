# Solarized Embedded Gists

<a title="Latest version" href="https://github.com/tiborsimon/solarized-gist/releases/latest" target="_blank">
   <img src="https://img.shields.io/badge/version-v1.2-green.svg?style=flat" />
</a>
<a title="Goto article" href="http://tiborsimon.github.io/web/solarized-theme-for-embedded-gists/" target="_blank">
   <img src="https://img.shields.io/badge/article-read-blue.svg?style=flat" />
</a>
<a title="Goto discussion" href="http://tiborsimon.github.io/web/solarized-theme-for-embedded-gists/#discussion" target="_blank">
   <img src="https://img.shields.io/badge/discussion-join-orange.svg?style=flat" />
</a>
<a title="Demo" href="http://tiborsimon.github.io/web/solarized-theme-for-embedded-gists#demo" target="_blank">
   <img src="http://img.shields.io/badge/license-MIT-green.svg?style=flat" />
</a>
<a title="License" href="#license">
   <img src="https://img.shields.io/badge/demo-try-green.svg?style=flat" />
</a>

<img src="http://tiborsimon.github.io/images/solarized-gist/solarized-gist-demo-image.png" />

## How to use this theme?

- __Using regular CSS__ - copy the content of the `css` folder to your site's CSS folder and link it to your pages.
- __Using CSS preprocessors__ - copy the content of the `sass` folder to your CSS files and link it to your pages.

And you are done. The included CSS files will override the CSS rules of your embedded Gist snippets.

## Create static CSS from SASS

If you want to create a custom color theme without replacing all the hard coded color codes in one of the static CSS files, there is a solution for you. You can modify the SASS variables according to your needs (even though your site isn't supporting SASS), then you can replace these variables in the generic SASS style sheet, resulting a fully static CSS file. Find the linked `sass2css.py` script to run the conversion.

## Contribution

Feel free to fork and contribute to this project, as the CSS class mapping between Pygments and the Gist CSS may not cover your particular needs.

## License

This project is under the __MIT license__. 
See the included license file for further details.




