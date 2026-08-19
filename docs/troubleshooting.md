# Python Logo Widgets — Troubleshooting

## The widget is a black rectangle

`bg` defaults to `"black"`, and the badges have transparent areas that show the label's
background. Match it to your window:

```python
LogoWidget(root, bg="white")
```

## The widget is blank

The classic Tkinter cause is a garbage-collected `PhotoImage` — but these classes bind it to
`self._image` precisely to prevent that, so it should not happen through normal use.

If it does, check you have not reassigned `_image` without updating `_label`:

```python
w._image = w._image.subsample(2)
w._label.configure(image=w._image)     # both, or the label keeps the old one
```

## `RuntimeError: Too early to create image`

You instantiated a widget before creating a `Tk()` root. `PhotoImage` needs a live interpreter:

```python
root = tk.Tk()          # first
LogoWidget(root)        # then
```

## `ModuleNotFoundError: No module named 'tkinter'`

Separate package on most Linux distributions:

```bash
sudo apt install python3-tk        # Debian, Ubuntu
sudo dnf install python3-tkinter   # Fedora
```

## `FileNotFoundError` for a bundled image

The package's `imgs/` directory did not install. Reinstall:

```bash
pip install --force-reinstall Python-Logo-Widgets
```

If you are running from a source checkout, confirm `python_logo_widgets/imgs/` contains
`logo.gif`, `length.gif`, `width.gif`, and `__init__.py` — the last is what makes the directory
addressable by `importlib.resources`.

## It fails inside a zipped package or a frozen build

`_load_image` returns `str(files(...).joinpath(name))`, which assumes the resource has a real
filesystem path. A zipimported package has none. Recorded in
[`internal/known-issues.md`](./internal/known-issues.md); `importlib.resources.as_file()` is the
fix.

Normal pip installs are unzipped, so this only affects unusual packaging.

## The demo does nothing

```bash
python-logo-widgets
python -m python_logo_widgets
```

Both should open a window. If neither does, check the install placed the console script on your
`PATH` — `python -m` works regardless.

## Tests fail on a headless machine

Tkinter needs a display:

```bash
xvfb-run -a pytest
```

## The image is too large for my layout

There is no size parameter, and `PhotoImage` scales only by integer factors. See
[Configuration](./configuration.md) — and note the trademark position on modifying the marks in
[FAQ](./faq.md).

## `pack` and `grid` conflict

Each widget uses `pack` **internally**, for its own label. That does not constrain how you place
the widget itself — mixing managers in one container is the error, and these keep theirs inside
their own frame.

## Still stuck

[Open an issue](https://github.com/willtheorangeguy/Python-Logo-Widgets/issues/new/choose) or ask
on the [Discord](https://discord.gg/eAZZJzhHrW), with your OS, Python version, and how you
installed it.
