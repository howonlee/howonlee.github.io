require "html-proofer"

SITE_DIR = "./_site"

task :build do
  sh "bundle exec jekyll build --strict_front_matter"
end

desc "Build the site and validate internal links, images, and scripts"
task test: :build do
  HTMLProofer.check_directory(
    SITE_DIR,
    disable_external: true,
    enforce_https: false,
    allow_missing_href: true,
    ignore_missing_alt: false
  ).run
end

desc "Build the site and audit external links"
task check_external: :build do
  HTMLProofer.check_directory(
    SITE_DIR,
    enforce_https: false,
    only_4xx: true,
    allow_missing_href: true,
    ignore_status_codes: [403, 429],
    ignore_missing_alt: false,
    typhoeus: {
      connecttimeout: 10,
      timeout: 30,
      followlocation: true
    }
  ).run
end
