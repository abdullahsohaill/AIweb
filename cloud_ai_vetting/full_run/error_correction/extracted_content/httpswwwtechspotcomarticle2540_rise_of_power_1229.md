# https://www.techspot.com/article/2540-rise-of-power/
**URL:** https://www.techspot.com/article/2540-rise-of-power
**Page Title:** The Rise of Power: Are CPUs and GPUs Becoming Too Energy Hungry? | TechSpot
--------------------

- Facebook
- Twitter
- Reddit
- RSS
- Comments
Every couple of years, a new generation of computer processors is launched. For a long time, CPUs seemed to stick to the same level of power, whereas GPUs only increased by a relatively small amount. But these days it appears that top-end models from all vendors are releasing models that require huge amounts of power.
Is 250W for a CPU and 450W for a GPU far too high? Do manufacturers even care about this? In this article, we'll peel off the heatsinks to look at the truth behind power figures and see exactly what's going on.

## Why chips need power and get hot

CPUs and GPUs are classed as Very Large Scale Integration circuits (VLSI) – enormous collections of transistors, resistors, and other electronic components, all microscopic in size.
Such chips require electricity to flow through them in order to perform the tasks they are designed to do. Arithmetic logic units carry out math by switching a host of transistors, to change various voltages elsewhere in the circuit.
Modern processors use a type of transistor called a FinFET ( Fin Field-Effect Transistor ). Think of these like a bridge between two islands, where the application of a small voltage lowers a road, allowing current to pass from one place to another.
Clearly, this involves a current passing through the islands and through the bridge, hence the need for electrical power – without it, the chips simply wouldn't do anything. But why do they then get hot?
Unfortunately, all of these components have a resistance to this flow of electricity. The actual amount is truly tiny, but given that the number of transistors in CPUs and GPUs runs into the billions, the cumulative effect is very pronounced.
Three billion transistors on a fingertip. Credit: Fritzchens Fritz
A typical CPU might only have a total internal resistance of a dozen or so milliohms, but once it has 80A or more of current flowing through it, the energy dissipated due to the resistance will be over 90 joules every second (or watts, W).
That energy is transferred to the materials that make up the whole chip, which is why every processor gets hot while it's working . Big chips need to be actively cooled to prevent their temperature from rising too high, so all of that heat needs to go elsewhere.
There are other factors that affect the amount of heat dissipated, such as current leakage , but if a processor is 'losing' energy (in the form of heat), it will need to constantly 'consume' it, to stay functional.
In other words, the amount of heat being lost is pretty much the same as the power rating of the chip. So let's begin by taking a look at the central processing unit and seeing how their power requirements have changed over the years.

## The hidden truth behind CPU's power figures

For many years, CPU vendors have been stating the power consumption of their processors via a simple figure: Thermal Design Power or TDP. This number has gone through various definitions, unfortunately, as chip designs have evolved.
Intel's current definition is:
"The time-averaged power dissipation that the processor is validated to not exceed during manufacturing while executing an Intel-specified high complexity workload at Base Frequency and at the maximum junction temperature"
In other words, if your Intel CPU has a base frequency of 3.4 GHz and a maximum temperature of 95 °C (203 °F), then its power rating will be equal to the TDP as long as it chip is operating at those limits.
So let's take a look at some examples of CPUs over the past 17 years. We've taken the most power-hungry desktop models released each year, over that period, ignoring ones that were aimed at workstations and the like.
Apart from a few isolated cases, such as AMD's FX-9590 from 2013 (with a TDP of 220W!), CPUs seem to have been very consistent in their power requirements.
At face value, it looks like there's no sign of them getting increasingly greedy for power, which is clearly a good thing. The advances made in semiconductor manufacturing, as well as optimal integrated circuit design, have to be the reasons for this.
The only problem with that is almost every CPU on the market can run at speeds much higher than its base frequency. The FX-9590 mentioned above has a base frequency of 4.7 GHz, but can increase the clock rate up to 5.0 GHz. So what happens then?
You might think it's a simple answer: it will dissipate more power, drawing a higher amount of current from the motherboard. Unfortunately, that's not always the case, as it depends on what settings have been enabled in the motherboard's BIOS.
Both Intel and AMD have a number of options, all of which can be activated or deactivated (depending on whether there's an option to do it, in the BIOS) that will let the CPU manage its own power and frequency.
Sticking with Intel for a moment, the primary system for doing this is called Turbo Boost Technology . 1980s-style name aside, what this does is actively control how much power the CPU can dissipate for a given load, over a certain amount of time.
Intel's CPUs typically have two such power limits, PL1 (a.k.a. TDP) and PL2, although more are available...
Note how the orange power curve can spike to significantly higher-than-PL1 levels and rise to PL2 for a certain amount of time. Here, the CPU is operating above its base frequency, but not necessarily at its maximum clock rate.
Since Intel disables PL3 and PL4 by default, we can take PL2 to be the actual maximum power consumption of the CPU – it may well only be for a few seconds (or depending on the BIOS settings, it could run like that forever), but it's still the highest wattage possible.
So how much higher is PL2 than PL1? This value has fluctuated with each new processor model, but let's just examine the ones from the last few years of our TDP chart above.
Seven years ago, with the likes of the Core i7-8700K , there was only a 30W difference between PL1 and PL2, but now it's over 100W – effectively doubling the power requirement, in some cases.
AMD doesn't use the same labels and definitions as Intel, but their CPUs can dissipate more power than the TDP limit as well.
The upper limit is given as Package Power Tracking (PPT) – the maximum power that the CPU can dissipate under any given load. For all Ryzen desktop processors with a TDP of 95W or more, the PPT is equal to 1.34 x TDP.
So one thing is now clear: top-end CPUs have definitely risen in their absolute maximum power requirements over the past few years, despite TDPs being relatively static.
Motherboard vendors make matters worse, though, by overriding the likes of Intel's default power limits and time constraints, and setting their own values in the BIOS. In other words, a CPU in one motherboard might max out at 120W, but hit 200W in another.
But we should take stock at this point, as all of the figures shown so far have been for the top-end models – those with the highest clock speeds and most number of cores.
Mid-range and budget CPUs have fortunately changed very little, simply because they've always had far fewer cores than the show-stoppers.
Down towards the bottom end of the desktop CPU market, Intel's popular Core i3-12100F has a TDP of 58W (and a PL2 of 89W), while AMD's Ryzen 3 4100 is rated to a TDP of 65W – pretty much the same as those product lines have always been.
However, AMD's latest mid-range Ryzen 7600X has a TDP of 105W, forty more than its immediate predecessor, the 5600X. And Intel's Core i5-12600K has the TDP of a high-end chip: 125W.
All of this points to there being a clear creep in power consumption, mostly towards the top-end models but not exclusively so. If you want a CPU that has the most number of cores and the highest clock speeds, then there's a significant energy demand that comes along with it.
Unfortunately, those folks wanting to upgrade to the latest mid-range product may well have to accept a notable energy hike, too.

## Enter the hungry hippos of power: GPUs

Where CPUs have been fairly gentle in terms of power, even accounting for the recent hike in the maximum limit, there's one chip in desktop PCs that's just got bigger and hungrier with each new generation. The graphics processing chip (GPU) is by far the largest and most complex semiconductor device that most people will ever own, in terms of the sheer number of transistors, die size, and processing capability.
The level of graphics fidelity in games today is of a scale that could only be dreamt of 17 years ago, but the power cost for all those polygons, textures, and pixels makes CPUs look lightweight, by comparison.
We've done the same thing in this chart, as we did for the CPU one – taking the most power-demanding consumer-grade graphics cards from the top vendors, for each year.
The likes of AMD's Ryzen 9 7950X might top out at 230W, but high-end GPUs were dissipating that level of power nearly 15 years ago.
And as the graph demonstrates, there's little sign that the trend for the most powerful graphics cards to require ever higher amounts of power will decrease at all, as the trends for both vendors are clearly non-decreasing, despite the correlation not being very strong.
With Nvidia's launch of the GeForce RTX 4090 , boasting a chip with 76 billion transistors and a TDP of 450W, the bar has taken a significant leap higher.
So are GPU vendors really not bothered about power requirements at all?
The above graph shows how the same chips as before have scaled in terms of the number of transistors packed into each square millimeter of the die, against the TDP of the graphics card.
The die density scale is logarithmic because there has been a colossal leap in density in recent years – a linear scale would have almost all of the data points packed into a small region.
We can see that as GPUs have packed ever more nano-sized switches into their circuits, the power requirements have steadily risen – but not in a constant manner (yes, the AMD line looks straight, but remember the log scale).
The non-linear trends are both increasing but the rate of the increase itself has decreased each year. This pattern between density and TDP is down to vendors releasing new chips that get are manufactured on an improved process node .
This is the name given to the fabrication method used by a semiconductor foundry to make the chips. Each new node provides a variety of benefits over its predecessor: higher density, lower power, better performance, and so on.
Newer process nodes are why GPUs have billions of transistors.
Not all of these improvements can be applied at the same time, but in the case of GPUs, it has allowed vendors to create truly enormous processors, with exceptional number-crunching levels, for a reasonable power requirement.
For example, if the Navi 21 was fabricated using the same node as that used for the R520, the power required would run well into the kW region. So while the energy levels are pretty high right now, they could be much worse.
And the benefits the new process nodes and GPU designs bring are more than just keeping power levels down.
The computational ability, per unit of power, of all top-end GPUs has seen a near-constant increase, at an astonishing rate, ever since the first unified shader models appeared back in 2006.
If one takes the above figures, the mean increase in TDP since 2006 has been 102%, whereas the rise in FP32 performance-per-watt has been an astonishing 5,700%
While FP32 processing throughput isn't the defining quality of a graphics card, it's one of the most important capabilities for gaming and 3D graphics. We only have games with incredible graphics and features today, because the best GPUs have got larger and more complex.
But even though graphics processors are better than ever, and their power levels actually aren't as bad as they could be, their level of energy consumption is still rising. Even ultra-budget GPUs, normally utilizing 30W or lower, have seen significant increases in TDP over the past few years.
If one wishes to purchase an Nvidia graphics card that can draw all of its current just through the PCI Express slot, then the entire Ampere inventory effectively needs to be skipped. The GeForce RTX 3050 has a TDP of 100W and since the slot has a limit of 75W, additional power connectors are required.
Such cards, like their much bigger brothers, have vastly more processing power than they ever used to, but for people wanting to build ultra-low power systems, there are increasingly fewer options to choose from, when it comes to the graphics card.
And there doesn't seem to be any signs of the rise in power demand slowing down, let alone decreasing. For example, Intel's newest foray into the graphics card market, the Arc series, is currently headed by its A770.
This card sports a chip with 21.4 billion transistors, 16GB of GDDR6, and a TDP of 225W. While it's targeted at the mid-range sector, that power demand is the same as AMD and Nvidia's biggest chips from four years ago.
It's a little better for the mid-range GeForce and Radeon cards, where the RTX 3060 requires 170W and the RX 6600 XT consumes 160W, but all sectors have risen in energy demand – far more so than CPUs.
If it wasn't for better engineering that demand would obviously be far higher, but an important question that really needs answering here is whether CPUs and GPUs are requiring too much power for what they're offering.

## How much is too much?

Two of the most common complaints about the rise in power demand of CPUs and GPUs are the cost of electricity and the amount of heat generated – let's take a look at the former, to begin with.
Let's say you have a very highly specified gaming PC, replete with some of the best components that money can afford you. Let's also assume that you're using an AMD Ryzen 9 5950X , backed up by a mildly overclocked Nvidia GeForce RTX 3090 Ti .
Naturally, there will be other parts in there, too (at the very least, a motherboard, some RAM, and a storage drive), but we can leave them aside because their combined energy consumption will be far lower than either the CPU or GPU. So, what kind of power will that PC be demanding, in the middle of some hectic gaming? How does 670W to 700W sound?
Now imagine that you use your PC in this way for 2 hours, each day, for every day of the year. The amount of energy consumed by the PC would be around 500 kWh (0.7 x 2 x 365) – equivalent to running a 1.5 kW electric kettle for almost two weeks, non-stop.
Depending on where you live in the world, and what rates you're paying for your electricity, the use of a PC like this might be anywhere from $70 to $280 (taxes and additional charges not included), each year.
But compared to the total cost of the PC itself, which would be several thousand dollars, it's a relatively small amount. Taking the higher value and calculating the electricity cost per hour of gaming only equates to $0.38 per hour.
Nvidia's new GeForce RTX 4090 has a TDP of 450W
A worst-case scenario of a computer with the most energy-hungry CPU and GPU combination you can get right now (the card above and Intel's Core i9-13900K ), with both running at their highest default power limits, would still only cost around $0.50 per hour, for the same gaming routine.
You might argue that 50 cents per hour of gaming is far too high, and for millions of people around the world, that is almost certainly true. But they're unlikely to have such a PC in the first place.
Home consoles are more popular than gaming PCs, in terms of units shipped per year, and they contain far less capable hardware than the examples given above. But in terms of power demand, something like Microsoft's Xbox Series X will only consume 153W during active gameplay.
Even if you account for a large OLED TV that might add another 100W, the two devices combined would actually use 44% less energy than the GeForce RTX 4090 alone . So if the cost of electricity is a genuine concern, then consoles are a good alternative for gaming.
Not that you need to use the latest or most powerful PC parts to enjoy games, of course. There are plenty of older or mid-range components that don't have excessively high power demands, which will still give lots of performance.
Second-hand Radeon RX 5700 XT, GeForce RTX 2060 Super, or even GeForce GTX 1080 Ti graphics cards are still very capable and all three have TDPs 250W or lower.
In short, the argument that the rise in power is an issue, purely because of the cost of electricity, is somewhat moot – too much depends on the local price for a unit of electricity, gaming habits, etc. to conclusively resolve such a debate.
But what about the heat?
As mentioned at the start of this article, pretty much every joule of electrical energy ends up being dissipated as heat, transferred to the environment mostly through the mechanism of convection.
If it uses electricity, it will be dissipating heat. Credit: Gorodenkoff
A computer churning out 900W could, in theory, raise the temperature of 1000 cubic feet of air (28 cubic metres) from 20°C/68°F to 40°C/104°F in as little as 17 minutes. This naturally assumes a perfect transfer of heat and perfect insulation, with no movement of the hotter air out of the volume in question.
But while it wouldn't actually be that quick, in reality, all of that heat is still eventually going to be transferred into the PC's surrounding environment, regardless of the rate of transfer.
Cooling fans, no matter the amount or their performance, wouldn't change this, as they only help to lower the temperature of the components. The only way to alleviate the rise in heat of the environment is to allow the heated air to move elsewhere, through a window opening, for example.
If you are planning on spending a large wedge of dollars on the most powerful CPU and GPU you can get, then be prepared for the fact that they are going to dump a significant amount of thermal energy into your gaming room.
Just as with the electricity cost complaint, this is ultimately an individual's concern – 900W of heat may be a chronic problem for one person, but perfectly okay for another.

## The needs of the many outweigh the needs of the few

So it would seem that concerns over heat output and the cost of electricity are very much individual issues. However, it all becomes far more important when scaled across the globe.
There are millions of PCs out there, and although the number of the area packing 250W+ chips is relatively small, eventually all these machines will be replaced with computers fielding components that have a higher power demand than they do now.
To get a sense of this, consider that there has been an estimated 17 million Xbox Series X and 50 million Xbox One consoles sold worldwide. The former uses roughly 90W more power than the latter.
If we assume that all those older units are replaced by the newer ones, that's an additional 3GW of accumulated power demand and, ultimately, dissipated heat. Obviously, these machines aren't all going to be running at the same time, but the extra energy required isn't unique to just this console.
As new processors come out for laptops, desktops, workstations, and servers, they're all going to be requiring more energy, be it a few watts or a hundred. Which in turn means that the energy industry is going to face an ever-higher demand for its ability to supply.
This will be the case anyway, due to population and economic growth, but the problem is just going to get compounded by this rise in semiconductor power.
Even accounting for a decline in PC sales as forecasts indicate so for a number of years, there are other sectors that are doing the opposite: Internet of Things (IoT), artificial intelligence (AI), and big data analysis are all showing plenty of growth.
AI and big data use lots of high-end GPUs to carry out the required calculations and if new components for these machines show no sign of tempering their power demand, then these industries will only make the energy situation worse.
Electricity demand, on a global scale, has been estimated by some to be as high as 3 times what it is now, growing 3 to 4% each year, by 2050. Whether such estimates have accounted for the increase in processor energy consumption is unclear, though.
Since 2005, the estimated global electricity production has risen from 18 PWh (1 PWh = 1,000,000 GWh) to 28 PWh in 2021 – a 56% increase in just 16 years. And that rise is entirely because of increased demand. The growth in semiconductor usage will only add to that in the forthcoming decades.

## So what, if anything, can be done about it?

As an individual, there are plenty of things you can try out to lower the power demand of your biggest PC components. In the case of CPUs, the majority of motherboards have a variety of power options in the BIOS that will force the processor to reduce its energy consumption when idle.
The Advanced Configuration and Power Interface (ACPI) appeared in desktop computers way back in 1996 and has been continually updated since then. Now, all consumer CPUs have features that are ACPI-compliant and for power consumption, there are two notable ones: P-states and C-states.
The former refers to what performance state the processor is operating in, and when enabled in the BIOS, enables the chip to run at a lower frequency and voltage, to save energy. C-states do a similar thing but control what the CPU is able to do (e.g. maintain data in cache or flush it entirely) while running in a less power-demanding format.
For AMD's more recent Ryzen processors (3000 series onwards), enabling Eco Mode in their Ryzen Master software will force the processor to run with a significantly lower TDP, independent of any ACPI option that's enabled.
Depending on the system used and the performance metric measured, the impact of using the lower power value can be surprisingly small .
Depending on the system used and the performance metric measured, the impact of using the lower power value can be surprisingly small . For users of Intel CPUs, something similar can be achieved by delving into the BIOS settings and looking for Internal CPU Power Management (not all models have it).
In this section, the values for PL1 and PL2 can be set lower than the defaults, although they are more likely to be listed under different names. For example, Asus uses Long/Short Package Duration Limit for PL1/PL2.
Graphics cards can be tweaked in the same way, by using software such as MSI Afterburner . This application gives control over the maximum power limit of the card, set as a percentage, and the figure can easily be lowered.
For example, Nvidia's RTX 2080 Super has a 100% power limit of 250W. Dropping this to 70% would cap the GPU's power consumption to 175W. Naturally, this will also lower the performance of the card, but just as with the Ryzen Eco Mode, the impact isn't as large as you might think.
A similar thing can be achieved by lowering the core voltage of the GPU, which in turn will usually require the clock rates to be lowered as well. Alternatively, if a game provides the option to cap the frame rate, fixing it at a lower value will also drop the power demand.
But for sheer simplicity, the adjustment of the power limit, through the use of a simple slider, can't be beaten.
We ran some quick tests, using Shadow of the Tomb Raider , with the aforementioned graphics card (RTX 2080 Super) and an Intel Core i7-9700K . The game's resolution was set to 4K, with all graphics details set to the maximum value, DLSS Quality mode enabled, but with ray tracing disabled.
It might seem incredulous that a 50% reduction in the maximum available power only results in a 10% reduction in the average frame rate (the 1% Low values dropped by less than 5%) but it's also worth noting that this game has quite a high CPU load.
The use of DLSS has also certainly helped in this test, as the game renders at a much lower resolution than that presented, but the GPU will just attempt to render at a faster rate, and still hit its power limit.
Obviously, different games and hardware setups will produce different outcomes from those seen above, but in Red Dead Redemption 2 (1440p, max quality) a 50% reduction in the power limit produced a 15% reduction in the average frame rate, and for Far Cry 6 , the FPS drop was just 7%.
So all of this may beg a simple question – why do hardware vendors set the power limit so high when it seems that it doesn't need to be?
The most likely reason is one that concerns marketing and product status. AMD, Intel, and Nvidia need their models to be as clearly differentiated as possible, especially at the halo end of the range.
These products are supposed to be the very best that you can buy, so the chips used will be selected from the binning process that results in ones that can run at the highest clock speed, if given enough power.
But this can lead to situations like that seen with the GeForce RTX 3090 Ti – it has a TDP 100W higher than the 3090 (29% higher), but even at 4K, our testing only showed it to be around 10% faster in games.
Since all of the major vendors will want to sell on every possible chip that's manufactured for them, the "few-percent-better" models aren't going to disappear, but designers can certainly reduce the power demand.

## Hardware manufacturers need to do better

Vendors such as AMD heavily promote the performance-per-watt aspect of their products and typically use it as a key selling point. For example, for their next desktop GPU architecture, RDNA 3, the improvement forecast is substantial. However, this doesn't mean the Radeon RX 7000 series of graphics cards will suddenly have much lower TDPs.
For RDNA 2, AMD highlighted that it had up to 65% more performance-per-watt than the previous architecture. Yet, the TDP of the Radeon RX 6800 was still 300W.
Our own testing verified AMD's claims for the much-improved performance per unit of power, but that still doesn't detract from the fact that the gains in rendering power require an additional energy hunger to feed.
One might argue that vendors should make it much easier to reduce the power demand of their products, perhaps even having them operating in some kind of 'eco mode' by default.
Manufacturers may say that they already do this, in the form of having their chips operate across various clock levels (e.g. Turbo Mode, Boost Clock, Gaming Clock) and have them significantly drop their voltages when idle.
But when Intel launched their 12th generation of Core desktop CPUs, the press releases were packed full of performance claims but only one section dared to mention power.
The brand new CPU design, mixing two different architectures in the same die, was clearly an improvement on the equivalent 11th-gen model. As the above image shows, Intel could have set the TDP to 95W, and the PL2 to 125W, and still have been able to boast higher performance.
Instead, they kept the same figures as before and simply sliced 10W off the PL2 value. All in the name of having a product that's a fraction faster than the competition in certain tests.
Of course, you don't have to buy these chips, but when it comes time to do an upgrade or simply buy a brand new computer or console, you have little option to accept these power-hungry offerings, because the older models are no longer in production.
And while it's relatively easy to adjust the power limits for CPUs and GPUs, it is arguably something that the end user shouldn't have to do.
People in general are changing their perspective on energy production, demand, and its impact on the climate and their wallets. While halo products and their insatiable appetite for energy grab all the headlines, it's the steady growth in power requirements across the whole sector that really matters.
It could be argued that too many semiconductor manufacturers are stuck in a mindset that's seemingly at odds with the world today – having the highest possible performance, to get one over the competition, at almost any cost.
There is some light toward the end of the tunnel, though. Apple, for example, has shifted almost its entire Mac and MacBook lines to use their own M1/M2 processors . These CPU+GPU combined processors were designed to be as energy efficient as possible and perform on par with x86 offerings from AMD and Intel, at a notably lower power demand (gaming excepted).
Servers and workstations are still generally packed with Intel Xeon or AMD Epyc processors, but the power-efficient Arm architecture utilized by Apple, is spreading into this sector as well. Big cloud providers are replacing their servers with some powered by Ampere's Altra models .
Change is coming – slowly, painfully so at times, but it is coming. It may be many more years before we start seeing new processors being launched with lower energy requirements than their predecessors, but there is some movement in the industry toward that goal.
In the meantime, on a personal level, we can make a simple choice: accept the power demands of the latest hardware and use them as is (with or without tweaking some settings), or vote with our wallets and let vendors know that hundreds of watts of power are too high a price to pay.
- Ad-free TechSpot experience while supporting our work
- Our promise: All reader contributions will go toward funding more content
- That means: More tech features, more benchmarks and analysis
- TESTED Windows 11 vs Windows 10: Which is Faster for Gaming?

### TESTED

## Windows 11 vs Windows 10: Which is Faster for Gaming?

- FUTUROLOGY After 70 years of false starts, fusion energy is finally gaining momentum

### FUTUROLOGY

## After 70 years of false starts, fusion energy is finally gaining momentum

- HARDWARE AMD Ryzen 9850X3D Review: For the FPS Chasers

### HARDWARE

## AMD Ryzen 9850X3D Review: For the FPS Chasers

- SECURITY Lawsuit alleges Meta can read WhatsApp messages despite encryption

### SECURITY

## Lawsuit alleges Meta can read WhatsApp messages despite encryption

- HUMANOID These robots can only work half as fast as humans, but factories are buying them anyway

### HUMANOID

## These robots can only work half as fast as humans, but factories are buying them anyway


--------------------