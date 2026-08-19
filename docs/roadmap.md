# Python Logo Widgets — Roadmap

Direction, not a schedule. Defects are in
[`internal/known-issues.md`](./internal/known-issues.md).

## Where it is

Three embeddable widgets, images bundled and resolved correctly, references held properly, the
original function API preserved, and tests for both. It does what it says.

## Considered

**Settling the licence position on the images.** The most important item, and it is a decision
rather than a code change: the repository is GPL v3, and the logo and badges are PSF trademarks
that cannot be relicensed that way. Stating the split explicitly — code GPL, marks PSF — is the
minimum; the README now does, and the repository's own licensing should follow.

**Replacing the boilerplate legal documents.** A privacy policy describing account creation and
personal data collection, for a package that opens no connection, is worse than none — it implies
data handling that does not exist.

**`importlib.resources.as_file()`** instead of `str(files(...))`, so the package works when
zipped.

**PNG instead of GIF.** Tkinter reads both, and PNG handles transparency better — which is the
one visual rough edge, since `bg` currently has to be matched by hand.

**A size argument.** Only integer scaling is available without Pillow, so this means either
bundling several sizes or accepting a dependency. Worth deciding rather than leaving as an
absence.

## Non-goals

**Pillow, or any runtime dependency.** A package that draws three static images should not pull
an imaging library into everything that uses it. That constraint is why the implementation is
seventy lines.

**More logos.** The Python marks are the point. A general badge widget is a different package,
and one without this one's trademark complications.

**Anything beyond display.** No animation, no theming engine, no state. `bg` and the standard
`Frame` arguments are the whole surface, deliberately.

**Granting rights to the trademarks.** Not possible, and worth saying plainly: this package makes
the badges convenient to display and confers nothing. The PSF's policy governs.

**Porting to another toolkit.** Qt and GTK have their own resource and image handling; the value
here is specific to Tkinter's `PhotoImage` pitfalls.

## Contributing

Issues and pull requests welcome — see the
[Contributing Guide](https://github.com/willtheorangeguy/.github/blob/main/CONTRIBUTING.md) or
the [Discord](https://discord.gg/eAZZJzhHrW). Code contributions are GPL v3.

Please do not open a pull request against the trademark question; that is the repository owner's
call.
