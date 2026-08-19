# Known Issues — Python-Logo-Widgets

Concrete defects and gaps found while writing this repository's documentation in
August 2026. **Nothing here was changed** — each one needs a code, configuration, or
licensing decision rather than a documentation one.

Ordered by severity. See [`docs/roadmap.md`](../roadmap.md) for the narrative version,
which also covers deliberate non-goals.


**3 open:** 1 high, 1 medium, 1 low.

## 1. GPL v3 is asserted over the Python logo and Python Powered badges, which are PSF trademarks

**Severity:** High  
**Where:** `LICENSE.md`, `README.md` (qualified in this pass), `python_logo_widgets/imgs/*.gif`

**What:** `LICENSE.md` is the GNU GPL v3, and the README stated 'This project is licensed under the [GNU General Public License]' with no carve-out. The three bundled GIFs are the Python logo and the two 'Python Powered' badges -- trademarks of the Python Software Foundation, governed by the [PSF Trademark Usage Policy](https://www.python.org/psf/trademarks/). The package is published to PyPI as `Python-Logo-Widgets`, so the images are redistributed with it. The credits table names the PSF, but as a project credit rather than as a rights holder.

**Why it matters:** The GPL grants every recipient the right to modify and redistribute what it covers -- which is precisely what a trademark policy restricts, and which the author is not in a position to grant over someone else's marks. Anyone taking the licence at face value could reasonably conclude they may alter the Python logo and ship the result, which the PSF policy does not permit. This is the one repository in the sweep whose *entire content* is third-party trademarked artwork, so the mismatch is not a corner case -- it is the whole package.

**Suggested fix:** Owner's decision, not a documentation change. Options: state the split explicitly in `LICENSE.md` (code GPL v3, images PSF trademarks under the PSF policy, redistributed under the nominative use the badges are intended for); add a `NOTICE` or `CONTENT_LICENSE.md` recording the PSF's terms; or replace the bundled marks with the author's own artwork and reference the official badges by URL. The README is qualified in this pass; the licence file itself is untouched.

## 2. The privacy policy and terms describe a service this package is not

**Severity:** Medium  
**Where:** `docs/legal/PRIVACY.md`, `docs/legal/TERMS.md`

**What:** Both are generated boilerplate dated 29 August 2022. `PRIVACY.md` opens 'This Privacy Policy describes Our policies and procedures on the collection, use and disclosure of Your information when You use the Service' and defines Account, Affiliate, and Personal Data. The package is an offline Tkinter widget library: it opens no network connection, creates no account, stores nothing, and reads only three GIFs from inside its own installation. The README links both from its License section.

**Why it matters:** A privacy policy is a statement about data handling, and this one asserts handling that does not occur -- accounts, personal data, disclosure to affiliates. That is misleading in the direction people do not expect documents to be misleading: it makes a package that collects nothing look like one that collects something, and a reader doing due diligence on dependencies has to read seventy lines of source to establish that the legal document is wrong about its own subject. Boilerplate is worse than absence here.

**Suggested fix:** Delete both, or replace them with two sentences: this package collects no data, makes no network requests, and writes nothing to disk. If terms are wanted for the PyPI listing, they should describe a library rather than a Service with Accounts.

## 3. str(files(...)) assumes a filesystem path, so the package breaks when zipped

**Severity:** Low  
**Where:** `python_logo_widgets/widgets.py` -> `_load_image`

**What:** `_load_image` returns `str(files("python_logo_widgets.imgs").joinpath(image_name))` and hands the result to `tk.PhotoImage(file=...)`. `files()` returns a `Traversable`, which only has a real filesystem path when the package is installed unzipped. For a zipimported package -- a zipapp, some frozen builds, an egg -- `str()` produces something that is not a readable path and `PhotoImage` fails.

**Why it matters:** The rest of this module is careful about exactly this class of problem: using `importlib.resources` at all, rather than a path relative to `__file__`, is what makes the widgets work from a wheel and from inside someone else's application. This is the last step of that reasoning left incomplete, and it fails in the packaging scenarios a widget library is most likely to be swept into -- someone bundling their Tkinter app for distribution.

**Suggested fix:** Use `importlib.resources.as_file()`, which materialises a real path for the duration of a context manager:

    with as_file(files("python_logo_widgets.imgs") / image_name) as path:
        image = tk.PhotoImage(file=str(path))

The `PhotoImage` must be constructed inside the block, since the temporary file may be removed on exit.


---

## Also, across every repository

**`.bandit` is present on disk but untracked in git.** Verified in PyWorkout, treklogger,
skyscanner-cli, booking-cli, piggy, and aibot — the config file exists locally in each but
`git ls-files` does not know about it, so none of it reached GitHub.

The August 2026 security sweep therefore looks complete locally and landed nowhere. Worth
checking across all 44 repositories it covered.
