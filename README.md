# tfl-roadside-signs
_history of changes on tfl variable message signs_

<img width="400" alt="image" src="https://user-images.githubusercontent.com/92937667/151003167-f62f5ceb-124a-4305-87fb-07fb6aabcbb0.png">

with a [github action](./.github/workflows/main.yml) running every twenty minutes:

1. use cURL to fetch variable message sign feed [https://roads.data.tfl.gov.uk/trafficstatus/vms.xml](https://roads.data.tfl.gov.uk/trafficstatus/vms.xml)
2. use python to extract the array of `<Sign>` records into a [json file](./signs.json) with the coordinates changed from easting/northing to longitude/latitude, omitting the feed metadata; this keeps the git history free of e.g. metadata changes other than on signs
3. commit the [json file](./signs.json) if the data has changed since the last run
4. create a [git-history](https://github.com/simonw/git-history) instance of [datasette](https://datasette.io/) and publish to [vercel](https://lewisham-tfl-roadside-signs-history.vercel.app/tfl-roadside-signs-history) - this allows you to analyse and plot the changes spatially and temporally, as well checking e.g. [which sign text is shown the most](https://lewisham-tfl-roadside-signs-history.vercel.app/tfl-roadside-signs-history/sign_version_detail?_facet=signtext#facet-signtext)
