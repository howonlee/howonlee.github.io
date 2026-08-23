# Ferns

The source for [howonlee.github.io](https://howonlee.github.io), built with Jekyll and GitHub Pages.

## Local development

Install Ruby 3.3.4 and Bundler, then install the pinned dependencies:

```sh
bundle install
```

Preview the site at `http://localhost:4000`:

```sh
bundle exec jekyll serve
```

Build the site and check internal links, images, and scripts:

```sh
bundle exec rake test
```

Audit external links separately, since old sites can be slow or intermittently unavailable:

```sh
bundle exec rake check_external
```
