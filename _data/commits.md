name: Update Latest Commits

on:
  schedule:
    - cron: '0 0 * * *'  # every day at midnight
  workflow_dispatch:

jobs:
  update_commits:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Fetch commits
        run: |
          curl -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
            https://api.github.com/users/OleksSobol/events/public \
            > commits.json
          # parse JSON into commits.md
      - name: Commit generated file
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add commits.md
          git commit -m "Update latest commits"
          git push
