# V5 latent audio field note — GitHub Pages package

This folder is self-contained: `index.html` keeps all ten listening clips inline, while the bundled JSON files are frozen inputs used by this note:

- `data/spine_results.json` (293,153 bytes)
- `data/why5_analysis.json` (8,420 bytes)

The page figures and the probe projections were checked against those frozen files.

## Publish with GitHub Pages

Publish the *contents* of this `site/` folder as the Pages site. For a repository Pages setup, either copy the contents into a `docs/` folder and select **Deploy from a branch → `/docs`**, or use a Pages artifact workflow that uploads this folder as the static artifact. Keep the relative layout (`index.html`, `data/`, and `probe.py`) unchanged.

GitHub Pages serves static files only; it cannot execute Python on the server. Download or clone this folder and run the probe locally instead.

## Local reproduction

From this directory:

```sh
python3 probe.py floor
python3 probe.py oracle
python3 probe.py strata
```

The commands are read-only and load `data/spine_results.json` and `data/why5_analysis.json` through paths relative to `probe.py`. They print the floor/oracle/strata projections used by the note.

The two JSON files are under 0.5 MB combined; audio is already embedded in `index.html`, so no media download is required.
