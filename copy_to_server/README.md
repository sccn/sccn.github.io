# copy_to_server

Server-side file for the EEGLAB download flow. Not part of the Jekyll build
(excluded in `_config.yml`); copy it manually to the `sccn.ucsd.edu` web root.

```
cd /home/arno/www/html/eeglab
curl -O https://github.com/sccn/sccn.github.io/blob/master/copy_to_server/downloadeeglab.ph
```

## Flow

1. `https://eeglab.org/others/How_to_download_EEGLAB.html` — download form.
2. Form POSTs to `https://sccn.ucsd.edu/eeglab/downloadeeglab.php` (this file).
3. Handler logs the request, does optional mailing-list subscriptions, then
   303-redirects to `https://eeglab.org/others/Download_Success.html`.

## Install `downloadeeglab.php`

- Place in the `eeglab/` directory so it resolves to `https://sccn.ucsd.edu/eeglab/downloadeeglab.php`.
- Requires PHP with `mail()` configured (mailing-list subscriptions).
- Ensure `/var/local/eeglab/` exists and is writable by the web user
  (log file `eeglablog.txt`, kept outside the web root).

## EEGLAB files that must exist on `sccn.ucsd.edu`

The links on `Download_Success.html` point to these files/folders:

- `/eeglab/currentversion/eeglab_current.zip` — latest MATLAB release
- `/eeglab/download/daily/` — older releases archive
- `/eeglab/eeglab4.5b.teaching.tar.gz` — legacy version (MATLAB < 2014)
- `/eeglab/currentversion/eeglab_compiled_windows.exe` — compiled Windows
- `/eeglab/currentversion/eeglab_compiled_macos.zip` — compiled macOS
- `/eeglab/currentversion/eeglab_compiled_ubuntu.zip` — compiled Ubuntu (legacy)
- `/eeglab/download/daily/compiled` — older compiled versions
