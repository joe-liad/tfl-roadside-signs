# tfl-roadside-signs
_history of changes on tfl roadside signs_

with a [github action](./github/workflows/main.yml) running every twenty minutes:

1. fetch `https://roads.data.tfl.gov.uk/trafficstatus/vms.xml`
2. extracts the array of `<Sign>` records into a [json file](./signs.json) omitting the feed metadata; this keeps the git history free of changes other than on signs
3. commits the [json file](./signs.json) if the records have changed
4. creates a [git-history](https://github.com/simonw/git-history) instance of [datasette](https://datasette.io/) and pushes to [vercel](https://lewisham-tfl-roadside-signs-history.vercel.app/tfl-roadside-signs-history)