# Known Issues — Python-Logo-Widgets

Concrete defects and gaps found while writing this repository's documentation in
August 2026. **Nothing here was changed** — each one needs a code, configuration, or
licensing decision rather than a documentation one.

Ordered by severity. See [`docs/roadmap.md`](../roadmap.md) for the narrative version,
which also covers deliberate non-goals.


**3 open:** 1 medium, 2 low.

## 1. The privacy policy and terms describe a service this package is not

**Severity:** Medium  
**Where:** `docs/legal/PRIVACY.md`, `docs/legal/TERMS.md`

**What:** Both are generated boilerplate dated 29 August 2022. `PRIVACY.md` opens 'This Privacy Policy describes Our policies and procedures on the collection, use and disclosure of Your information when You use the Service' and defines Account, Affiliate, and Personal Data. The package is an offline Tkinter widget library: it opens no network connection, creates no account, stores nothing, and reads only three GIFs from inside its own installation. The README links both from its License section.

**Why it matters:** A privacy policy is a statement about data handling, and this one asserts handling that does not occur -- accounts, personal data, disclosure to affiliates. That is misleading in the direction people do not expect documents to be misleading: it makes a package that collects nothing look like one that collects something, and a reader doing due diligence on dependencies has to read seventy lines of source to establish that the legal document is wrong about its own subject. Boilerplate is worse than absence here.

**Suggested fix:** Delete both, or replace them with two sentences: this package collects no data, makes no network requests, and writes nothing to disk. If terms are wanted for the PyPI listing, they should describe a library rather than a Service with Accounts.

## 2. The GPL licence file does not mention the PSF marks it ships alongside

**Severity:** Low  
**Where:** `LICENSE.md`, `README.md` (warning added in this pass), `python_logo_widgets/imgs/*.gif`

**What:** `LICENSE.md` is the GNU GPL v3 with no carve-out, and the three bundled GIFs are the Python logo and the two 'Python Powered' badges -- copyright and trademarks of the Python Software Foundation, governed by the [PSF Trademark Usage Policy](https://www.python.org/psf/trademarks/). The package is published to PyPI, so the images are redistributed with it. Read alone, the licence file implies the GPL's modify-and-redistribute permission extends to the marks; it does not.

**Why it matters:** **Resolved -- the owner has decided the licence stays as it is, with a warning added instead.** The remaining exposure is that `LICENSE.md` is the file a redistributor reads first and it still says nothing about the marks, so the correction lives only in the README and these docs. That is a documentation-shaped mitigation for a licence-shaped ambiguity, which is why this stays on the list rather than being closed outright.

**Suggested fix:** Done in this pass: the README carries a prominent warning that the images are PSF property and not covered by the GPL, repeated in the documentation index and the FAQ. If it ever becomes worth strengthening, a short `NOTICE` file beside `LICENSE.md` -- naming the marks, the PSF, and the trademark policy -- would put the same statement where a redistributor actually looks, without altering the licence itself.

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
