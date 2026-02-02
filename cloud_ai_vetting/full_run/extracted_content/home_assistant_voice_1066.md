# Home Assistant Voice
**URL:** https://www.home-assistant.io/voice-pe
**Page Title:** Home Assistant Voice Preview Edition - Home Assistant
--------------------


## Bring choice to voice

Limited to a set list of common home control phrases, this allows even low-powered hardware
                      system to process speech locally and offline.
Full speech processing is done locally, requiring high processing power for adequate speed and
                      accuracy.
Your voice is processed privately on Home Assistant Cloud, allowing Assist to run very accurately
                      on low-powered hardware.
- Select your language
- Afrikaans (South Africa)
- Arabic (Jordan)
- Bulgarian (Bulgaria)
- Bengali (Bangladesh)
- Bengali (India)
- Catalan (Spain)
- Czech (Czech Republic)
- Danish (Denmark)
- German (Germany)
- German (Switzerland)
- Greek (Greece)
- English (United States)
- English (United Kingdom)
- Spanish (Spain)
- Spanish (Mexico)
- Estonian (Estonia)
- Basque (Spain)
- Persian (Iran)
- Finnish (Finland)
- French (France)
- Irish (Ireland)
- Galician (Spain)
- Gujarati (India)
- Hebrew (Israel)
- Hindi (India)
- Croatian (Croatia)
- Hungarian (Hungary)
- Indonesian (Indonesia)
- Icelandic (Iceland)
- Italian (Italy)
- Georgian (Georgia)
- Kannada (India)
- Korean (South Korea)
- Luxembourgish (Luxembourg)
- Lithuanian (Lithuania)
- Latvian (Latvia)
- Malayalam (India)
- Mongolian (Mongolia)
- Marathi (India)
- Malay (Malaysia)
- Norwegian Bokmål (Norway)
- Nepali (Nepal)
- Dutch (Belgium)
- Dutch (Netherlands)
- Polish (Poland)
- Portuguese (Portugal)
- Portuguese (Brazil)
- Romanian (Romania)
- Russian (Russia)
- Slovak (Slovakia)
- Slovenian (Slovenia)
- Serbian (Serbia)
- Swedish (Sweden)
- Swahili (Kenya)
- Telugu (India)
- Thai (Thailand)
- Turkish (Turkey)
- Ukrainian (Ukraine)
- Urdu (India)
- Vietnamese (Vietnam)
- Chinese (China)
- Chinese (Hong Kong)
- Chinese (Taiwan)
Fully open software, firmware, and hardware allows you to make it work best for your
            needs.
            It includes a Grove port for connecting sensors and a 3.5mm headphone jack for connecting external speakers.
            With a dedicated community customizing and adding functionality.
Be part of building Assist and preview the future of voice control in the home.
- 84x84x21 mm
- 96 g
- 94x94x30 mm
- 120 g
- Injection-molded Polycarbonate plastic
- White and semi-transparent
- Multipurpose button
- Rotary dial for volume and other input
- Mute switch that physically cuts power to the microphone
- Internal speaker
- Internal dual-mic array
- 3.5mm audio output
- Grove port to connect sensors or other accessories
- Easy to open - no clips, only screws to access internals
- Exposed pads on PCB for modding
- ESP32-S3 SoC with 16 MB of FLASH storage
- 8 MB octal PSRAM
- XMOS XU316
- Featuring: Echo cancellation Stationary noise removal Auto gain control
- Dedicated I2S lines for audio in and out
- USB-C, 5 V DC, 2 A
- 2.4 GHz Wi-Fi
- Bluetooth 5.0
- 3.5 mm (⅛”) stereo headphone jack
- Digital to analog converter (DAC): TI AIC3204 48 kHz sampling rate
- ESPHome preloaded
- Fully open-source firmware for both the ESP32 and XMOS chip
[LINK: open-source](https://github.com/esphome/home-assistant-voice-pe)
- Indoor use only O °C to 30 °C | 32 °F to 86 °F
- Humidity: non-condensing Keep in dry, not excessively dusty environment as this can cause damage to the unit
It is our vision to make open, local, and private voice assistants a reality in any language.
                      While we have made great strides in realizing this, it is such a massive undertaking that we
                      need our worldwide community to participate in its development. An essential ingredient for the
                      community to drive the project forward is a standardized hardware platform for voice, built for
                      Home Assistant from the ground up: Home Assistant Voice Preview Edition.
While for some, the
                      current state of our voice assistant may be all they need, we think there is still more to do
                      before it is ready for every home in every country, and until then, we’ll be selling this
                      Preview of the future of voice assistants. Taking back our privacy isn’t for everyone - it’s a
                      journey - and we want as many people as possible to join us and make it better.
Yes, provided your language is supported. For some languages, you can set up Assist and your
                      Voice Preview Edition to use a Focused Local model, which uses Speech-to-Phrase add-on. It can run
                      locally and accurately on lower-power hardware, by generating a local speech-to-text model
                      specifically for your Home Assistant installation. It is limited to predefined sentences aimed at
                      controlling your home, but not able to process general speech. For instance, it could turn on a
                      device, but would not be able to add something to your shopping list.
For other languages, Speech-to-Phrase may not be supported, which will require Fully Local
                      speech-to-text solution, such as the Whisper add-on. Fully local speech-to-text requires powerful
                      hardware to be accurate and responsive. If you wish to use OpenAI’s Whisper, we recommend using at
                      least an Intel N100 or equivalent processor. This will allow you to use the Whisper Base model for
                      speech-to-text locally. This model runs reasonably fast for languages that have large public
                      datasets to train on, such as English and Spanish. However, for languages with less data
                      available, you will need Whisper’s Small or Large models that require significantly more powerful
                      hardware to run.
You do not need Home Assistant Cloud. However, for some languages, we believe that Home Assistant
                      Cloud provides the best experience. There are languages that are not supported by the local
                      speech-to-text models we leverage (either our focused local Speech-to-Phrase model, or the fully
                      local Whisper by OpenAI), but are well-supported by the speech processing used by Home Assistant
                      Cloud.
Home Assistant Cloud has been designed from the ground up to uphold the core values of the Home
                      Assistant project, with privacy being one of our highest priorities. Home Assistant Cloud
                      leverages the enterprise services of Microsoft Azure for its industry-leading speech processing,
                      which unlike many consumer offerings, is bound by commercial terms and conditions and does not retain or store your data . In addition, Home
                      Assistant Cloud itself does not keep any record of
                      your voice, data, or commands.
Three separate parts are needed for a language to be supported in local operation. Reliable,
                      local speech-to-text models must be available to turn what is said into text commands that can
                      be sent to Home Assistant. Home Assistant then needs to have sentence support for that language,
                      so it knows which actions to perform for each command.
Finally, a local text-to-speech model has
                      to be available for your language, so it can reply to you. If any of these three parts are not
                      available locally, your language is not yet supported. Currently, there is one part that holds
                      back our language support more than the others, and that’s local speech-to-text.
There can be a number of reasons why a language is not supported by Home Assistant Cloud, but
                      most often it is because the sentences have not been translated by a member of our
                      community. If you would like to help translate these sentences and have your language added,
                      please visit here .
[LINK: sentences](https://developers.home-assistant.io/docs/voice/intent-recognition/supported-languages)
[LINK: visit here](https://developers.home-assistant.io/docs/voice/intent-recognition/contributing)
We need your help to improve or add support for your language. Through the help of our global
                      community, ultimately, we aim to support every language possible. In our documentation , we have
                      a list of various ways you can help us advance our open, local, and private voice assistant.
                      Thank you for helping us make voice better in your language.
Yes, Home Assistant can be configured to use any speech-to-text integration that supports the
                      Wyoming protocol. The most commonly used fully local speech-to-text add-on available for Home
                      Assistant users is OpenAI’s Whisper. This has mixed results; specifically, it lacks support for
                      some languages and is hardware-intensive.
Our alternative speech-to-text model, Speech-To-Phrase , can run locally and accurately on
                      lower-power hardware, though this does not provide full speech-to-text capabilities. Based on the Rhasspy project ,
                      it is able to create focused local speech-to-text models, limited to predefined sentences aimed at
                      controlling your home, but not able to process general speech. For instance, it could turn on a
                      device, but would not be able to add something to your shopping list.
[LINK: Speech-To-Phrase](https://github.com/OHF-Voice/speech-to-phrase)
[LINK: Rhasspy project](https://github.com/rhasspy/rhasspy)
Out of the box, the device can listen for “Okay Nabu,” “Hey Jarvis,” or “Hey Mycroft” as wake
                      words. This is provided by the on-device wake word engine called microWakeWord. Creating these
                      wake words requires very powerful hardware and large datasets to train, which is not realistic for
                      most users.
In time we will work with the community to create more wake words, but currently are focused on
                      improving our current wake words to work for a large variety of accents and voice registers.
A wake word should be uncommon in everyday conversations at home or in media, such as music or
                      TV, to minimize the risk of the device activating unintentionally. “Nabu”, “Jarvis”, and
                      “Mycroft” are fairly unique words, as opposed to generic terms such as “computer” or “assist”.
                      That makes these microWakeWord models perform well for most users.
In the future, we intend to match and then surpass the Big Tech voice assistants, but for now,
                      this Preview Edition can not yet do everything those devices can. For some, the current
                      capabilities of our voice assistant will be all they need; especially those who just want to set
                      timers, manage their shopping list, and control their most used devices. For others, we
                      understand they want to ask their voice assistant to make whale sounds or to tell them how tall
                      Taylor Swift is - our voice assistant doesn’t do those things… yet.
Yes, if you plug an external speaker into the 3.5mm audio port. The built-in speaker is meant for
                      voice feedback and is not optimized for listening to music, but the included DAC is capable of
                      playing lossless audio on a suitable external speaker. We recommend using Music Assistant to
                      control music playback.
Yes, if you have paid access to a supported cloud LLM or have a local LLM running on suitable
                      hardware, it is possible to either fully replace our voice assistant’s conversation agent with an
                      LLM or use it as a fallback for commands that Home Assistant does not understand natively.
The benefit of this is being able to ask nearly any query that comes to mind, and speak commands
                      in natural language. Just note, we consider the use of AI in the smart home to be experimental , and would recommend caution when letting it
                      control important aspects of your home. Get started with AI and Assist .
No, the device does not come with a USB-C charger and cable. Sustainability is a core value of
                      the Home Assistant project, and we do not wish to send more chargers or cables into the world
                      when most users already own enough of these.
You can find an overview of everything you can say to the device in our documentation . You may
                      need to expose some devices manually to Assist, in order
                      to let this device control them.

--------------------