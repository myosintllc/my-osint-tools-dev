# Introduction

Bookmarklets are awesome for assisting with tedious OSINT task.

Therefore **myosint.training** [maintain](https://tools.myosint.training/) a nice collection suited to automate those boring tasks that would otherwise pile up minutes here and there in your day to day OSINT work. Instead of having to go through source code to find those pesky IDs on various social media sites bookmarklets - small snippets of Javascript - can find and output them for you with a simple click.

All you have to do get up and running is drag and drop those you might have use of to the bookmarks bar of your browser.

However if you have 30+ of these your browser bar quickly gets filled and at some point you get lost. Which ones should be updated because they were patched on the bookmarklets' webpage? WHich ones should be deleted because the method - or the site - they utilized simply no longer works or exists?

Well, this is where a *userscript* for Tampermonkey might come in handy. Using this framework you can add [userscript.js](userscript.js) from this repository and now you'll have all the bookmarklets from **myosint.training** installed and available in your browser in one simple step.

They'll auto update from our repository whenever the drag and drop-versions are updated on the website. You'll never have to do that manually again.

Before you go all *hell year! gimme the codez!*, please read the [warning](#a-warning-about-the-implications-of-userscripts) in the bottom of this guide and make sure you understand the implications of installing all of the bookmarklets in one simple step from this repository.


# Installation

[Tampermonkey](https://www.tampermonkey.net/) is a browser extension available for both all major browser versions. It's an amazing tool.
Tampermonkey is a cross browser compatible extension that allows you to do all sorts of cool stuff with the browser.

Think of it as a way to write your own extensions - without actually knowing how to put an actual extension together. Tampermonkey handles all the boilerplate for you.

Just write the lines of Javascript you want the extension to run, paste it into Tampermonkeys IDE and tell it which sites you want to *tamper* with (i.e. inject the Javascript into) - *BOOM* you now have your own custom extension for that particular site.

Pretty awesome.

Install the extention from whatever store is avaialble for your browser, but make sure to take a look at the guide on the official website too.

The chromium based browsers now needs to allow *Developer Mode* to run Tampermonkey, as the Manifest v3 broke a lot of cool stuff in the name of improved security. This, however, also broke some extensions like uBlock, Tampermonkey and others.

Toggling the browser into *Developer Mode* can bring back the parts that Tampermonkey require to function. If you're on, say Brave, there might be an extra step involved going into Extensions (through the menu), viewing Details of Tampermonkey and toggle a switch there to "Allow User Scripts".

## Setup a userscript

Once installed in the browser open Tampermonkey. Now you can do one of two things:

1) Create a new extension (by pressing the '+' symbol). Delete the boiler plate Tampermonkey presents you and copy/paste the content of [userscript.js](./userscript.js) into the blank userscript and press *Save*, or:

2) Press the "Raw" button for [userscript.js](./userscript.js) on Github and copy the URL. Under the "Utilities" pane in Tampermonkey paste the URL into the **Import from URL** field and press "Install". This will load the userscript directly from the Github repository and auto update the userscript automatically from Github with future updates.

That's really all there is to it.

When you right click on e.g. TikTok now, the bookmarklets - plus the global ones - should be accessible through a _right click_-context menu. You can also click the Tamper

<img alt="image" src="assets/tiktok.png" />

You can also click on the Tampermonkey extension icon to get faster access to the scripts as shown below.

<img alt="image" src="assets/tiktok2.png" />

## Special atrributes used to generate userscript.js

A bookmarklet is a bookmark that consist of Javascript and not a URL.

The [userscript.js](userscript.js) consist of all the bookmarklets found on [index.html](../index.html). The userscript is automatically compiled using Github Actions when this page changes by running [build_userscript.py](./build_userscript.py).

In order for this to work each bookmarklet must have at couple of `data-` attributes.

The purpose of each of these are explained below:

- `data-name` (required): The build script will compile a list of Javascript functions. The value of this attribute is used to declare the bookmarklet as a function.
- `data-domain`(required): The scope for the bookmarklet, e.g. "instagram.com". If set to "*" the bookmarklet will be available on every domain.
- `data-replace-open`(optional): If set (and set to "true") the build script will replace all occurences of `window.open` with `GM_openInTab` for the particular bookmarklet. Browsers typically block attempts to open a bunch of new tabs in one go using `window.open` - extensions, however, do not have this limitation and Tampermonkey enables you to open as many new tabs as you'd like using the method `GM_openInTab`.

All bookmarklets on the page are and must be written as [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE) (Immediately Invoked Function Expression) to confine the content and not polute the global scope. Not adhering to this will cause the userscript to break.

# A warning about the implications of userscripts

Browser extensions can be awesome. But they sure can also be malicious. Extensions might be able to read (and alter) all requests your browser make, screenshot it etc. And they might also be able to transmit those data to someone else without you knowing about it.

Recently an extension that did also provide [Free VPN](https://www.techradar.com/vpn/vpn-privacy-security/this-free-chrome-vpn-extension-found-to-spy-on-its-100k-users-uninstall-it-now) secretly also screenshottet all pages the user visited and sent those to the creator.

That's bad.

Typically extensions auto update. An extension you install today after vetting it thorougly might not have the same owner or content tomorrow. All it takes is one malicious update and your p0wned.

The same goes for userscripts.

In this guide we showcase two different methods to add the userscript to Tampermonkey. The first one does not automatically update the userscript. If a bookmarklet is updated on [the tools page](https://tools.myosint.training/) and in the Github repository you will need to grab (and in the best of all worlds) vet it manually before allowing it to run in your browser.

If you chose to install it by importing it directly as a URL from Github you will get auto updates whenever the repository updates. This requires you to trust the authors of the userscript.

A third way would be for you to fork the repository on Github (create your own copy that you and you alone control) and add that URL to Tampermonkey instead.

If the userscript changes the original Github page you'll be alerted by Github. You can then review the changes and pull them into your own fork if you agree there are just harmless snippets of Javascript that will be helpfull to your day to day OSINT task.