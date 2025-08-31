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


## Special properties used to generate userscript.js

A bookmarklet is a bookmark that consist of Javascript and not a URL.

The [userscript.js](userscript.js) consist of all the bookmarklets found on [index.html](../index.html). The userscript is automatically compiled using Github Actions when this page changes by running [build_userscript.py](./build_userscript.py).

In order for this to work each bookmarklet must have at couple of `data-` properties.

The purpose of each of these are explained below:

- `data-name` (required): The build script will compile a list of Javascript functions. The value of this property is used to declare the bookmarklet as a function.
- `data-domain`(required): The scope for the bookmarklet, e.g. "instagram.com". If set to "*" the bookmarklet will be available on every domain.
- `data-replace-open`(optional): If set (and set to "true") the build script will replace all occurences of `window.open` with `GM_openInTab` for the particular bookmarklet. Browsers typically block attempts to open a bunch of new tabs in one go using `window.open` - extensions, however, do not have this limitation and Tampermonkey enables you to open as many new tabs as you'd like using the method `GM_openInTab`. 

All bookmarklets on the page are and must be written as [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE) (Immediately Invoked Function Expression) to confine the content and not polute the global scope. Not adhering to this will cause the userscript to break.

## Typical challenges when writing bookmarklets in drag and drop-format

At the **osint.training** website the bookmarklets are presented in a `<a href="javascript:(function(){BOOKMARKLET CODE_GOES HERE})()">`. This allows them to be drag and dropped into the bookmarks bar in the browser.

This, however, means that you can't use a double quote inside the bookmarklet as this would terminate the `href`.

This can give you quite some headaches when you try to write Javascript that will work inside the `href`.

Below are two common issues and solutions.

### multiple quotes required

Image you need to fetch the element shown below using Javascript:

```html
<div role="list">Juicy stuff to extract</div>
```

Using Javascript this could normally be achived like so:

```javascript
let div = document.querySelector('div[role="list"]');
let juicyStuff = div.textContent;
```

This, however, will not work inside an `href` as the `"` will terminate the `href`. One solution is to use single quotes consistently and escape the inner ones like so:

```javascript
let div = document.querySelector('div[role=\'list\']')
```

This will not break the `href` and will work inside a bookmarklet.

## matching double quotes using regex

Sometimes you find yourself in a situation where you need to match a double quote for instance using a regular expression.

Say you have a string like this in a HTML body and you need to match it to extract an id:

``'html
"community","shouldUseFXIMProfilePicEditor":false,"userID":"4"}, "queryName":"ProfileCometHeaderQuery"}
``'

Matching and extracting the value of the userID (`4`) with a regex might look something like this:

```javascript
document.body.innerHTML.match(/"userID":"(\d+)"/)
```

The issue here is that we can't use double quotes within the `href="...."`. How do we match it then? 

One solution is to do a switcharoo in the HTML. Use single quotes on the outside of the `href` and double quotes inside. Instead of `<a href="...">` you can use `<a href='....'>` this, however, is not the best way to go about it, since the convention is to use double quotes for attributes in HTML.


The better - and somewhat contra intutitve - solution to this headache is to replace the double quotes with HTML entities.

The HTML entity for `"` is `&quot,`. So when ever you want to write a bookmarklet and place it within `href="...."` because you want to drag and drop it into the bookmarks bar like on the **myosint.training**, you need to replace `"` with `&quot;` like so:

```javascript
document.body.innerHTML.match(/&quot;userID&quot;:&quot;(\d+)&quot;/)
```

Note that this code will NOT work if you run it in the Javascript console of the browser (unless that sentence is actually present in the source of the page). But if you place it inside `href="..."` and drag and drop it to your bookmarks bar it will.

The reason for this is that the browser will decode the HTML entities (`&quot;` becomes `"`) and all of a sudden you end up with exactly the right code in your bookmarklet, which is this one:

```javascript
document.body.innerHTML.match(/"userID":"(\d+)"/)
```

Pretty fantastic.

Replacing `"` with an HTML entity will by the way not break the userscript since it extracts the bookmarklets from [index.html](../index.html) using the Python library [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) which also decodes the HTML-entities from the `href`s.


## A warning about the implications of userscripts

Browser extensions can be awesome. But they sure can also be malicious. Extensions might be able to read (and alter) all requests your browser make, screenshot it etc. And they might also be able to transmit those data to someone else without you knowing about it.

Recently an extension that did also provide [Free VPN](https://www.techradar.com/vpn/vpn-privacy-security/this-free-chrome-vpn-extension-found-to-spy-on-its-100k-users-uninstall-it-now) secretly also screenshottet all pages the user visited and sent those to the creator.

That's bad.

Typically extensions auto update. An extension you install today after vetting it thorougly might not have the same owner or content tomorrow. All it takes is one malicious update and your p0wned.

The same goes for userscripts. 

In this guide we showcase two different methods to add the userscript to Tampermonkey. The first one does not automatically update the userscript. If a bookmarklet is updated on [the tools page](https://tools.myosint.training/) and in the Github repository you will need to grab (and in the best of all worlds vet) it manually before allowing it to run in your browser.

If you chose to install it by importing it directly as a URL from Github you will get auto updates whenever the repository updates. This requires you to trust the authors of the userscript.

A third way would be for you to fork the repository on Github (create your own copy that you and you alone control) and add that URL to Tampermonkey instead. 

If the userscript changes the original Github page you'll be alerted by Github. You can then review the changes and pull them into your own fork if you agree there are just harmless snippets of Javascript that will be helpfull to your day to day OSINT task.