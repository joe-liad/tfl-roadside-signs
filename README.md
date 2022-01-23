# tfl-roadside-signs
_history of changes on tfl roadside signs_

with a [github action](./github/workflows/main.yml) running every twenty minutes:

1. fetch [https://roads.data.tfl.gov.uk/trafficstatus/vms.xml](https://roads.data.tfl.gov.uk/trafficstatus/vms.xml)
2. extract the array of <code><Sign></code> records into a [json file](./signs.json) omitting the feed metadata; this keeps the git history free of changes other than on signs
3. commit the [json file](./signs.json) if the records have changed
4. create a [git-history](https://github.com/simonw/git-history) instance of [datasette](https://datasette.io/) and push to [vercel](https://lewisham-tfl-roadside-signs-history.vercel.app/tfl-roadside-signs-history)