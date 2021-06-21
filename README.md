# [liu2z2.github.io]((https://liu2z2.github.io/))

My personal ePortfolio and blog.
- Powered by [Pelican](https://blog.getpelican.com/) - a static site generator written in Python
- Using Pelican theme [Elegant](https://elegant.oncrashreboot.com/)
- Using open-source privacy-focused analytics tool [Nulltics](https://nullitics.com/).
- Using open-source PDF Viewer [ViewerJS](https://viewerjs.org/)

## Branches
I am not an expert in web development so I used a static site generator in a language I am familiar with.
- Source code and source content available at [main](../../tree/main) branch.
- Rendered HTML available at [pelican-src](../../tree/pelican-src) branch.

## Dependencies
A confirmed working set of environment is built with conda in linux-64.
- [Pelican](https://blog.getpelican.com/) to generate HTML from source
- [Elegant](https://elegant.oncrashreboot.com/) as theme, a local copy is kept in `pelican-themes/elegant`
- Pelican plugins, they are either available from pip3 or kept as local copy in `plugins/`
  - [Web Assets](https://github.com/pelican-plugins/webassets)
  - [Tipue Search](https://github.com/getpelican/pelican-plugins/tree/master/tipue_search)
  - [Post Statistics](https://github.com/getpelican/pelican-plugins/tree/master/post_stats)
  - [Neighbor Articles](https://github.com/pelican-plugins/neighbors)
  - [Extract Table of Content](https://github.com/getpelican/pelican-plugins/tree/master/extract_toc)
  - [Render Math](https://github.com/pelican-plugins/render-math)
  - [Sitemap](https://github.com/pelican-plugins/sitemap)

## Example Build
1. Checkout [pelican-src](../../tree/pelican-src) branch.
2. Install Python 3 and [dependencies](#dependencies), confirmed working set is listed in `environment.yml` (installation see [Managing conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)).
3. Build content according to [pelican wiki](https://docs.getpelican.com/en/latest/publish.html) or with `Makefile` (`make help` for more info).

## Contact
For any questions regarding the repository, please open a [issue ticket](../../issues/new), or [contact me](https://github.com/liu2z2#contact-me) personally.
I do not have too much experience on web front-end but I will try to help as much as I can.
