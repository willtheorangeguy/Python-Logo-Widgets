# Python Logo Widgets — Configuration

Almost nothing to configure, by design. One argument.

## `bg`

```python
LogoWidget(parent, bg="white")
```

Sets the background of the image `Label`. Defaults to `"black"`.

The badges have transparent regions, and Tkinter fills transparency with the label's background —
so `bg` is effectively "what colour shows through the logo". Match it to the window behind, or
the widget appears as a black rectangle on a light background.

Any Tkinter colour works: a name (`"white"`), a hex string (`"#f0f0f0"`), or a system colour.

## Everything else goes to `tk.Frame`

```python
LogoWidget(parent, bg="white", borderwidth=2, relief=tk.RIDGE)
```

`**kwargs` are forwarded to `tk.Frame.__init__`, so padding, borders, and relief work as usual.

Note the distinction: `bg` is applied to the inner **label**, and the remaining arguments to the
outer **frame**. Passing `background=` as a keyword sets the frame's, not the image's.

## Sizing

There is no size parameter. Each widget displays its GIF at native resolution, and the label is
packed with `fill=tk.BOTH, expand=True` so the frame follows the image.

Tkinter's `PhotoImage` can only scale by integer factors, via `subsample` and `zoom`:

```python
w = LogoWidget(root)
w._image = w._image.subsample(2)     # half size
w._label.configure(image=w._image)
```

That reaches into private attributes, and half or a third is all you get. Smooth scaling needs
Pillow, which this package deliberately does not depend on. See [Roadmap](./roadmap.md).

Supplying differently-sized images is the practical answer — but note the trademark position on
modifying the logos in [FAQ](./faq.md).

## The images

| File | Widget |
|---|---|
| `imgs/logo.gif` | `LogoWidget` |
| `imgs/length.gif` | `PoweredByLengthWidget` |
| `imgs/width.gif` | `PoweredByWidthWidget` |

GIF because Tkinter's `PhotoImage` reads GIF and PNG only. They are resolved through
`importlib.resources`, not by path, so there is no directory to configure.

## No runtime state

No config file, no environment variable, no cache, and nothing written to disk. The package
reads its own bundled images and draws them.
