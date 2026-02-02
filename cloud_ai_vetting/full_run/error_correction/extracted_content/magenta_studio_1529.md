# Magenta Studio
**URL:** https://magenta.tensorflow.org/studio
**Page Title:** Magenta Studio - Ableton Live Plugin
--------------------


## Magenta Studio (Ableton Live Plugin) (v2.0)

[LINK: Download Ableton Live Plugin](https://storage.googleapis.com/magenta-studio/releases/magenta_studio-2.0.0.amxd)
[LINK: View on GitHub](https://github.com/tensorflow/magenta-studio)
Magenta Studio is an Ableton Live plugin built
      on Magenta’s open source tools and models.
      They use cutting-edge machine learning techniques for music generation.
Magenta Studio was formerly available as a collection of standalone applications. They are
      not actively maintained but may still work on your operating system. For more information,
      please see Magenta Studio v1.0 .

## Table of Contents

- Overview
- Installation
- Usage
- Continue
- Generate
- Interpolate
- Groove
- Drumify

## Overview

Magenta Studio is a MIDI plugin for Ableton Live. It contains 5 tools: Continue , Groove , Generate , Drumify , and Interpolate , which let you apply Magenta models on your MIDI clips from the Session View.

## Installation

## Requirements

- Ableton Live 10.1 Suite* or greater

## Installation

Drag the downloaded Magenta Studio amxd file into any available MIDI track within Live.

## Usage

## Launching the plugin

Each of the tools can be launched by clicking on its name within the plugin.

## Clip selection

All of the plugins work by choosing one or more clips from Ableton's Session View.
      You must choose a track before selecting your clip. Only MIDI tracks will show up as options.
      Once all of your selections are made, the Generate button will become enabled.

## Temperature

All of the plugins have a temperature slider. Temperature is a parameter used for sampling
      in the last layer of the neural network. You can think of it as controlling randomness:
      higher values produce more variation and sometimes even chaos, while lower values are more
      conservative in their predictions.

## Limitations

Melody input is limited to monophonic melodies (one note at a time), and drums input uses this
      MIDI mapping. Notes outside this range will be mapped to these 9 instruments:

## Continue

Continue uses the predictive power of recurrent neural networks (RNN) to generate notes that are likely to follow your drum beat or melody. Give it an input clip and it
      can extend it by up to 32 measures. This can be helpful for adding variation to a
      drum beat or creating new material for a melodic track. It typically picks up on things
      like durations, key signatures and timing. It can
      be used to produce more random outputs by increasing the temperature.

## How to use

Select a clip which you would like to extend, then click Generate . The output
      clips will be added to the clip slots after your selected clip.
Note: This video uses the v1 version of Magenta Studio. The interface now
      launches within the Ableton Live window, but the functionality is the same.

## Generate

Generate is similar to Continue , but it generates a 4 bar phrase
      with no input necessary. Choose where you would like the output to go,
      the number of variations, temperature, and click Generate . This can be helpful for breaking a creative
      block or as a source of inspiration for an original sample.
Under the hood, Generate uses a Variational Autoencoder (VAE) that has been trained on millions of melodies and rhythms to learn a summarized
      representation of musical qualities. Generate chooses a random combination of these summarized
      qualities and decodes it back to MIDI to produce a new musical clip.

## How to use

Generate does not require any input files, so the clip selection determines where you'd like the output clips to go.
Note: This video uses the v1 version of Magenta Studio. The interface now
      launches within the Ableton Live window, but the functionality is the same.

## Interpolate

Unlike the other plugins, Interpolate takes two drum beats or two melodies
      as inputs. It then generates up to 16 clips which combine the qualities of these two clips.
      It's useful for merging musical ideas, or creating a smooth morphing between them.
Interpolate also uses a Variational Autoencoder (VAE) similar to Generate .
      One way to think of the VAE is as a mapping from MIDI to a compressed space in which similar
      musical patterns are clustered together. Each of your input patterns is represented by a position
      on this map. Interpolate draws a line between these positions and returns clips along this line.
      The number of returned clips is set by the "steps" slider.

## How to use

Interpolate requires two inputs, and these inputs must be on the same track.
      The outputs are inserted after the second clip. The clips should be the same length and less
      than 4 measures.
Note: This video uses the v1 version of Magenta Studio. The interface now
      launches within the Ableton Live window, but the functionality is the same.

## Groove

Groove adjusts the timing and velocity of an input drum clip to produce the "feel"
      of a drummer's performance. This is similar to what a “humanize" plugin does, but achieved
      in a totally different way.
We recorded 15 hours of real drummers performing on MIDI drum kits. These recordings
      were quantized, removing all velocity and microtiming and were used to train a neural network
      to predict the unquantized beats as the output.

## How to use

Groove takes one clip as an input and places the output clip one slot below the input.
Note: This video uses the v1 version of Magenta Studio. The interface now
      launches within the Ableton Live window, but the functionality is the same.

## Drumify

Drumify creates grooves based on the rhythm of any input. It can be used to generate
      a drum accompaniment to a bassline or melody, or to create a drum track from a tapped rhythm.
      It works best with performed inputs, but it can also handle quantized clips.
We used the same dataset of drum performances as Groove to train Drumify. However,
      instead of learning a translation from quantized drum patterns to performances, here we map from
      rhythms to performances. We extract a rhythm from each performance by removing the
      pitches and velocities, while keeping the precise timing details. When you provide an input sequence --
      be it a melody, bassline, chord progression, or drum pattern -- we extract a rhythm in the same way and have the model
      turn it into a groove.

## How to use

Drumify takes one clip as an input and places the output clip one slot below the input.
Note: This video uses the v1 version of Magenta Studio. The interface now
      launches within the Ableton Live window, but the functionality is the same.

--------------------