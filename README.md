<!-- Logo -->
<h1 align="center">
  <img src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/Python-Logo-Widgets/logo.png" height="250px" width="400px" alt="Python Logo Widgets">
  <br>
  Python Logo Widgets
  <br>
</h1>

<!-- Copy -->
<h4 align="center">Drop-in Tkinter widgets for the Python logo and the "Python Powered" badges.</h4>

<!-- Badges -->
<div align="center">
  <img alt="GitHub Version" src="https://img.shields.io/github/v/release/willtheorangeguy/Python-Logo-Widgets?include_prereleases">
  <img alt="GitHub Issues" src="https://img.shields.io/github/issues/willtheorangeguy/Python-Logo-Widgets">
  <img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/willtheorangeguy/Python-Logo-Widgets">
  <img alt="License" src="https://img.shields.io/github/license/willtheorangeguy/Python-Logo-Widgets">
</div>

<!-- Navigation -->
<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#support">Support</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

<!-- Screenshot(s) -->
<div align="center">
  <img alt="Python Logo Widget" src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/Python-Logo-Widgets/pythonlogo.png">
  <img alt="Python Powered Height Widget" src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/Python-Logo-Widgets/pythonpoweredheight.png">
  <img alt="Python Powered Width Widget" src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/Python-Logo-Widgets/pythonpoweredwidth.png">
</div>

## Key Features

- Three embeddable `tkinter.Frame` subclasses — put them straight into your own windows.
- Images bundled with the package and resolved through `importlib.resources`, so they work however you install it.
- Each widget keeps its own image reference, so nothing renders blank.
- A standalone demo, and backward-compatible wrappers for the original function API.
- Pure standard library — Tkinter only.
- Cross-platform.

## Installation

```bash
pip install Python-Logo-Widgets
```

## Usage

```python
import tkinter as tk
from python_logo_widgets import LogoWidget, PoweredByWidthWidget

root = tk.Tk()
LogoWidget(root, bg="white").pack(pady=10)
PoweredByWidthWidget(root).pack(side=tk.BOTTOM)
root.mainloop()
```

| Widget | Image |
|---|---|
| `LogoWidget` | The Python logo |
| `PoweredByLengthWidget` | "Python Powered", tall |
| `PoweredByWidthWidget` | "Python Powered", wide |

Each takes a parent and an optional `bg` (default `"black"`). Demo: `python-logo-widgets` or `python -m python_logo_widgets`.

## Documentation

Full documentation lives in [`docs/`](docs/index.md):
[Quickstart](docs/quickstart.md) · [Installation](docs/installation.md) · [Configuration](docs/configuration.md) · [Architecture](docs/architecture.md) · [API](docs/api.md) · [Development](docs/development.md) · [FAQ](docs/faq.md) · [Troubleshooting](docs/troubleshooting.md) · [Roadmap](docs/roadmap.md)

## Support

Open a [GitHub Discussion](https://github.com/willtheorangeguy/Python-Logo-Widgets/discussions/new), file an [issue](https://github.com/willtheorangeguy/Python-Logo-Widgets/issues/new/choose), or join the [Discord](https://discord.gg/eAZZJzhHrW).

## Contributing

Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/willtheorangeguy/Python-Logo-Widgets/compare).

See the org-wide [Contributing Guide](https://github.com/willtheorangeguy/.github/blob/main/CONTRIBUTING.md) and [Code of Conduct](https://github.com/willtheorangeguy/.github/blob/main/CODE_OF_CONDUCT.md).

## Credits

This software uses the following open source packages, projects, services or websites:

<!-- Credits Table -->
<table>
  <tr>
    <th align="center"><img src="https://applets.imgix.net/https%3A%2F%2Fassets.ifttt.com%2Fimages%2Fchannels%2F2107379463%2Ficons%2Fmonochrome_large.png?w=240&h=240&s=8a19bbc158996d098e2fb18310ba7f33" width="150" height="150" alt="GitHub"/></th>
    <th align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/182px-Python-logo-notext.svg.png" width="150" height="150" alt="PSF"/></th>
    <th align="center"><img src="https://pyinstaller.readthedocs.io/en/v4.2/_static/pyinstaller-draft1a.ico" width="150" height="150" alt="PyInstaller"/></th>
  </tr>
  <tr>
    <td align="center">GitHub</td>
    <td align="center">Python Software Foundation</td>
    <td align="center">PyInstaller</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/">Web</a> - <a href="https://github.com/pricing">Plans</a></td>
    <td align="center"><a href="https://www.python.org/">Web</a> - <a href="https://psfmember.org/civicrm/contribute/transact?reset=1&id=2">Donate</a></td>
    <td align="center"><a href="https://pyinstaller.readthedocs.io/en/stable/">Web</a> - <a href="https://www.pyinstaller.org/funding.html#funding-by-individuals">Donate</a></td>
</table>

Sponsor [@willtheorangeguy](https://github.com/willtheorangeguy) on [PayPal](https://paypal.me/wvdg44?country.x=CA&locale.x=en_US).

## License

The **code** in this repository is licensed under the [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.en.html) — see [`LICENSE.md`](LICENSE.md).

> ⚠️ **The bundled images are not covered by that licence.** The Python logo and the "Python Powered" badges are copyright and trademarks of the [Python Software Foundation](https://www.python.org/psf/trademarks/). They are included here under the PSF's [Trademark Usage Policy](https://www.python.org/psf/trademarks/), which is what governs their use — not the GPL.
>
> In practice: displaying the badges to show your software is built with Python is the use the PSF intends and this package makes convenient. **Modifying the marks, or redistributing altered versions, is not permitted**, whatever rights the GPL would otherwise grant over files in this repository.

[Privacy Policy](docs/legal/privacy.md) · [Terms and Conditions](docs/legal/terms.md)
