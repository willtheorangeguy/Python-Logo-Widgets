# Python Logo Widgets — FAQ

### Can I use the Python logo in my application?

The PSF's [Trademark Usage Policy](https://www.python.org/psf/trademarks/) governs that, not this
package's licence. Broadly, the "Python Powered" badges exist to indicate that software is built
with Python, and that use is what they are for. Modifying the marks, or using them in ways that
suggest PSF endorsement, is not.

This package makes the badges convenient to display. It does not — and cannot — grant you rights
to them.

### The repository is GPL. Does that cover the images?

**No.** `LICENSE.md` is GPL v3 and covers the code. The Python logo and the "Python Powered"
badges are copyright and trademarks of the Python Software Foundation, included here under the
PSF's [Trademark Usage Policy](https://www.python.org/psf/trademarks/) — which is what governs
them.

So: the GPL's permission to modify and redistribute applies to the source, not to the marks.
Display them; do not alter them or ship altered versions.

The licence file is deliberately left as it is; the split is stated in the README, the
[documentation index](./README.md), and here.

### Why is there a privacy policy?

Boilerplate, and it does not describe this package. `docs/legal/PRIVACY.md` talks about accounts,
personal data, and "the Service"; this is an offline widget library that opens no connection and
stores nothing.

Recorded in the same file. Read the code — it is seventy lines.

### My widget shows a black box.

`bg` defaults to `"black"`, and the badges have transparent regions that take the label's
background colour. Pass `bg` matching your window:

```python
LogoWidget(root, bg="white")
```

### The widget is blank.

Unlikely with these classes — each binds its `PhotoImage` to `self._image` specifically to
prevent it. If you see it anyway, you have probably reassigned `_image` without updating
`_label`. See [Troubleshooting](./troubleshooting.md).

### How do I resize a widget?

There is no size parameter. `PhotoImage` scales only by integer factors (`subsample`, `zoom`),
which means half or a third and nothing between. Smooth scaling needs Pillow, which this package
deliberately does not depend on.

Supplying your own image is the practical route — subject to the trademark point above.

### Why GIF and not PNG or SVG?

Tkinter's `PhotoImage` reads GIF and PNG only. PNG would work equally well; SVG and everything
else needs Pillow or a converter.

### Can I embed these in a `ttk` layout?

Yes. They are `tk.Frame` subclasses, and `ttk` containers accept them like any other widget.

### Do the old functions still work?

Yes — `logo_widget()`, `length_widget()`, `width_widget()` in `python_logo_widgets._compat`. They
open their own window and block, so they cannot be embedded. New code should use the classes.

### Does it need internet, or write anything?

Neither. It reads three files from inside its own package.

### Why depend on this at all rather than copying the GIFs?

Because the images resolve correctly however the package is installed, and each widget keeps its
image alive — two things that are easy to get wrong by hand, and that fail silently when you do.
