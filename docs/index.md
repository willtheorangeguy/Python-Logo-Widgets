# Python Logo Widgets — Documentation

Three Tkinter `Frame` subclasses that display the Python logo and the "Python Powered" badges,
with the images bundled so you do not have to ship them yourself.

```text
python_logo_widgets/
├── widgets.py     LogoWidget, PoweredByLengthWidget, PoweredByWidthWidget
├── _compat.py     the original function API, kept working
├── _demo.py       the standalone demo
├── __main__.py    python -m python_logo_widgets
└── imgs/          logo.gif, length.gif, width.gif
```

## Pages

- [Quickstart](./quickstart.md) — embed one in five lines
- [Installation](./installation.md) — pip, or from source
- [Configuration](./configuration.md) — the `bg` argument and sizing
- [Architecture](./architecture.md) — how the images are found and kept alive
- [API](./api.md) — the three classes and the compatibility functions
- [Development](./development.md) — tests and conventions
- [FAQ](./faq.md) — trademarks, sizing, why GIF
- [Troubleshooting](./troubleshooting.md) — blank widgets, missing images
- [Roadmap](./roadmap.md) — direction and non-goals
- [Known issues](./internal/known-issues.md) — recorded defects

## Before you redistribute this

⚠️ **The images are PSF property, not GPL-licensed content.**

The repository's `LICENSE.md` is GPL v3, which grants recipients the right to modify and
redistribute everything it covers. The Python logo and the "Python Powered" badges are trademarks
of the Python Software Foundation, governed by the
[PSF Trademark Usage Policy](https://www.python.org/psf/trademarks/) — they are not the author's
to place under GPL, and the policy restricts modifying them in ways the GPL explicitly permits.

Using the badges to indicate that your software is built with Python is the use the PSF intends.
Treating the image files as GPL content you may alter and redistribute is not.

**The position, decided:** the repository's licence stays GPL v3 for the code, and the images
carry the PSF's own terms. The README states the split, and this page and the
[FAQ](./faq.md) repeat it, so nobody has to infer it from a licence file that does not mention
the marks.

Recorded in [`internal/known-issues.md`](./internal/known-issues.md) for the record.

## The legal documents

`docs/legal/PRIVACY.md` and `docs/legal/TERMS.md` are generated boilerplate describing accounts,
personal data collection, and "the Service". This package has none of those — it opens no
network connection, stores nothing, and reads only its own bundled images.

Same known-issues file.

## What it actually does

Loads three GIFs from the installed package and puts each in a `Label` inside a `Frame`. That is
the whole implementation, and it is about seventy lines.

The value is in the details it gets right: resources resolved through `importlib.resources` so
they are found however the package is installed, and each image bound to `self._image` so Tkinter
cannot garbage-collect it out from under the label. Both are covered in
[Architecture](./architecture.md).
