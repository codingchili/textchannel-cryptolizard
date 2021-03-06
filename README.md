# textchannel-cryptolizard
Gateway for sending and receiving sms messages through your browser or using our API, using your own Android phone or someone elses.

Status: Planned

![terminal](https://raw.githubusercontent.com/codingchili/textchannel-cryptolizard/master/terminal.png)

#### Background
This project allows anyone to turn their Android phone into an SMS gateway. Why would anyone like to do this? For starters, this makes it possible to send SMS in ways you could never dream of. With this piece of software it is possible to send and receive text messages in your browser. For example if you are sitting at your computer and receiving a text; it is now possible to avoid unlocking a slow Android device when you could have used your mechanical keyboard! Time saver! 

There is an additional problem, cell providers will often bake the costs of thousands of text messages into your monthly bill. In the meantime, SMS gateway providers are selling SMS at 0.15$ each. What if you could sell your unspent SMS messages to someone else? We are creating a marketplace to do this, driven by the power of crypto currency! Money saver! (This is problematic, we should only allow trusted gateways as there is no way to ensure end-to-end for plain sms messages in stock apps. Alternatively, let the market decide which actors are trusted. Gateway providers should provide a public key for clients to encrypt message contents, the broker should not have read access.)

There is already products on the market that allows me to turn my phone into an SMS gateway?
- yes, some of which has severe security issues observed. Sending your username and password in plaintext, essentially allowing ANYONE in the world to send free texts from your phone. 

This repository contains the following
1. A webserver with the SMS gateway API
2. A website to interact with the API in a chat-like manner.
3. A terminal app written in python with curses.
4. The Android SMS gateway client application (required)

Features
- Send and receive sms messages in a chat-like manner using the web interface.
- API support for UDP/TCP/REST and Websocket connections for time critical SMS!
- Schedule sending of a single text

Experimental poweruser features
- Ability to sell and buy SMS for Ether at the SMS auction.

Who would use this?
- You, Me, the cat.
