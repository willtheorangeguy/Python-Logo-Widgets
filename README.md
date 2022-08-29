<!-- Logo -->
<h1 align="center">
  <img src="https://raw.githubusercontent.com/willtheorangeguy/Python-Logo-Widgets/master/docs/images/logo.png" height="300px" width="350px" alt="Python Logo Widgets">
  <br>
  Python Logo Widgets
  <br>
</h1>

<!-- Copy -->
<h4 align="center">A group of widgets showing the Python logos, that can easily be added to your Python GUI code!</h4>

<!-- Badges -->
<div align="center">
  <!-- Stability -->
  <img alt="Test State" src="https://github.com/willtheorangeguy/Python-Logo-Widgets/actions/workflows/test.yml/badge.svg">
  <!-- Stability -->
  <img alt="Build State" src="https://github.com/willtheorangeguy/Python-Logo-Widgets/actions/workflows/build.yml/badge.svg">
  <!-- Stability -->
  <img alt="Pylint State" src="https://github.com/willtheorangeguy/Python-Logo-Widgets/actions/workflows/pylint.yml/badge.svg">
  <!-- CodeQL -->
  <img alt="CodeQL State" src="https://github.com/willtheorangeguy/Python-Logo-Widgets/actions/workflows/codeql.yml/badge.svg">
  <!-- Gitleaks -->
  <img alt="Gitleaks State" src="https://github.com/willtheorangeguy/Python-Logo-Widgets/actions/workflows/gitleaks.yml/badge.svg">
  <!-- Version -->
  <img alt="GitHub Version" src="https://img.shields.io/github/v/release/willtheorangeguy/Python-Logo-Widgets">
  <!-- Issues -->
  <img alt="GitHub Issues" src="https://img.shields.io/github/issues/willtheorangeguy/Python-Logo-Widgets">
  <!-- Pull Requests -->
  <img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/willtheorangeguy/Python-Logo-Widgets">
  <!-- Discord -->
  <img alt="Discord Server ID" src="https://img.shields.io/discord/960705680174633021">
  <!-- Downloads -->
  <img alt="Downloads" src="https://img.shields.io/github/downloads/willtheorangeguy/Python-Logo-Widgets/total">
  <!-- Language Count -->
  <img alt="GitHub Languages" src="https://img.shields.io/github/languages/count/willtheorangeguy/Python-Logo-Widgets">
</div>

<!-- Navigation -->
<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#download">Download</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#support">Support</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#changelog">Changelog</a> •
  <a href="#credits">Credits & Contributors</a>
</p>

<!-- Screenshot(s) -->
<div align="center">
  <img alt="Python Logo Widget" src="https://raw.githubusercontent.com/willtheorangeguy/Python-Logo-Widgets/master/docs/images/pythonlogo.png">
  <img alt="Python Powered Height Widget" src="https://raw.githubusercontent.com/willtheorangeguy/Python-Logo-Widgets/master/docs/images/pythonpoweredheight.png">
  <img alt="Python Powered Width Widget" src="https://raw.githubusercontent.com/willtheorangeguy/Python-Logo-Widgets/master/docs/images/pythonpoweredwidth.png">
</div>

## Key Features

* High quality images.
* Easy to integrate into a `Tkinter` GUI project.
* Available as code or as a function.
* Built-in samples.
* Cross platform.

## Download

You can **[download](https://github.com/willtheorangeguy/Python-Logo-Widgets/releases/latest) the source code** to run the script from the command line on Windows, macOS and Linux or add the images to your project. **This will require [Python](https://www.python.org/downloads/).**

You can **[download](https://github.com/willtheorangeguy/Python-Logo-Widgets/releases/latest) the latest executable version** of Python Logo Widgets for Windows. **This does not require Python.**

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/) installed on your computer. If you would rather not use Git, you can just download the code from GitHub above. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/willtheorangeguy/Python-Logo-Widgets.git

# Go into the repository
$ cd Python-Logo-Widgets

# Run the samples
$ python main.py
```

**To add the widgets to your project, just import the code files!** Follow these instructions:

1. Copy the `logo_widget.py`, `python_powered_length_widget.py`, `python_powered_width_widget.py` files, and `logos` folder to your project.
2. Import each of the widgets (and `Tkinter`) into your project:

```python
# Import Statements
from tkinter import *
from logo_widget import *
from python_powered_length_widget import *
from python_powered_width_widget import *
```

3. Call each of the respective widgets:

| Python Logo | Python Powered Length | Python Powered Width |
|-------------|-----------------------|----------------------|
|`logo()` |`python_powered_length()`|`python_powered_width()`|

4. Save and run the file (`F5`). You're all set!

## Support

If you want to save program space, you do not need to copy all of the code and image files, or import all of the widgets into your application. The following table describes the required resources for each widget:

|        | Python Logo | Python Powered Length | Python Powered Width |
|--------|-------------|-----------------------|----------------------|
|Image|`pythonlogogif`|`pythonpoweredlengthgif`|`pythonpoweredwidthgif`|
|File|`logo_widget` |`python_powered_length_widget`|`python_powered_width_widget`|
|Function|`logo()` |`python_powered_length()`|`python_powered_width()`|

Copy and import only the files that are necessary for the widget your project requires.

Customizing the logo and widget sizes can be found in [`CUSTOMIZATION`](https://github.com/willtheorangeguy/Python-Logo-Widgets/blob/master/docs/CUSTOMIZATION.md). Hard-coding the widgets into your project can be found in [`USAGE`](https://github.com/willtheorangeguy/Python-Logo-Widgets/blob/master/docs/USAGE.md). More documentation is available in the **[Documentation](https://github.com/willtheorangeguy/Python-Logo-Widgets/tree/main/docs)** and on the **[Wiki](https://github.com/willtheorangeguy/Python-Logo-Widgets/wiki)**. If more support is required, please open a **[GitHub Discussion](https://github.com/willtheorangeguy/Python-Logo-Widgets/discussions/new)** or join our **[Discord](https://discord.gg/eAZZJzhHrW)**.

## Contributing

Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/willtheorangeguy/Python-Logo-Widgets/compare).

Please read [`CONTRIBUTING`](CONTRIBUTING.md) for details on our [`CODE OF CONDUCT`](CODE_OF_CONDUCT.md), and the process for submitting pull requests to us.

## Changelog

See the [`CHANGELOG`](CHANGELOG.md) file for details.

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

## Contributors

* [@willtheorangeguy](https://github.com/willtheorangeguy) - Sponsor on [PayPal](https://paypal.me/wvdg44?country.x=CA&locale.x=en_US)

## You may also like...

* [Running Calculator](https://github.com/willtheorangeguy/Running-Calculator) - A running speed calculator for any unit of distance.
* [PyWorkout](https://github.com/willtheorangeguy/PyWorkout) - A minimal CLI to keep you inspired during your workout!
* [PyAvatar](https://github.com/willtheorangeguy/PyAvatar) - Easily display all of your creative avatars to keep them consistent across websites.

## License

This project is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html) - see the [`LICENSE`](LICENSE.md) file for details. See the [Privacy Policy](https://github.com/willtheorangeguy/Python-Logo-Widgets/blob/main/docs/legal/PRIVACY.md) and [Terms and Conditions](https://github.com/willtheorangeguy/Python-Logo-Widgets/blob/main/docs/legal/TERMS.md) for legal information.
