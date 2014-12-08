Flashlight
==========

_The missing Spotlight plugin system_

<img src='https://raw.github.com/nate-parrott/flashlight/master/Image.png' width='100%'/>

Flashlight is an **unofficial Spotlight API** that allows you to programmatically process queries and add additional results. It's *very rough right now,* and a *horrendous hack*, but a fun proof of concept.

**Installation**

Clone and build using Xcode, or [download Flashlight.app from _releases_](https://github.com/nate-parrott/Flashlight/releases).

## Writing Plugins

**Start with the [tutorial on writing plugins](https://github.com/nate-parrott/Flashlight/blob/master/Docs/Tutorial.markdown).**

## How it works

The `Flashlight.app` Xcode target is a fork of [EasySIMBL](https://github.com/norio-nomura/EasySIMBL) (which is designed to allow loading runtime injection of plugins into arbitrary apps) that's been modified to load a single plugin (stored inside its own bundle, rather than an external directory) into the Spotlight process. It should be able to coexist with EasySIMBL if you use it.

The SIMBL plugin that's loaded into Spotlight, `SpotlightSIMBL.bundle`, patches Spotlight to add a new subclass of `SPQuery`, the internal class used to fetch results from different sources. It runs a bundled Python script, which uses [commanding](https://github.com/nate-parrott/commanding) to parse queries and determine their intents and parameters, then invokes the appropriate plugin's `plugin.py` script and presents the results using a custom subclass of `SPResult`.

Since [I'm not sure how to subclass classes that aren't available at link time](http://stackoverflow.com/questions/26704130/subclass-objective-c-class-without-linking-with-the-superclass), subclasses of Spotlight internal classes are made at runtime using [Mike Ash's instructions and helper code](https://www.mikeash.com/pyblog/friday-qa-2010-11-19-creating-classes-at-runtime-for-fun-and-profit.html).

The Spotlight plugin is gated to run only on versions `911-916.1` (Yosemite GM through 10.10.1 seed). If a new version of Spotlight comes out, you can manually edit `SpotlightSIMBL/SpotlightSIMBL/Info.plist` key `SIMBLTargetApplications.MaxBundleVersion`, restarts Spotlight, verify everything works, and then submit a pull request.

## Credits

Huge thanks to everyone who's contributed translations:

 - [xremix](http://github.com/xremix) for German
 - [matth96](http://github.com/matth96) for Dutch
 - [tiphedor](http://github.com/tiphedor) for French
 - [lipe1966](http://github.com/lipe1966) for Portugese
 - [chuyik](http://github.com/chuyik) for Chinese
 - [suer](http://github.com/suer) for Japanese

If it's not translated to your native language yet, you should [consider helping us localize.](https://github.com/nate-parrott/Flashlight/blob/master/Docs/Internationalization.markdown)

The iOS-style switches in the app (`ITSwitch.h/m`) are [ITSwitch](https://github.com/iluuu1994/ITSwitch), by [Ilija Tovilo](https://github.com/iluuu1994).

The code injection system is forked from [Norio Nomura](Norio Nomura)'s [EasySIMBL](https://github.com/norio-nomura/EasySIMBL).

The [ZipZap library by Glen Low](https://github.com/pixelglow/zipzap) is used internally.

Licensed under the GPL.
