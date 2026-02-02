# lost to time
**URL:** https://mathoverflow.net/questions/117292/why-is-a-ring-called-a-ring
**Page Title:** ra.rings and algebras - Why is a ring called a "ring"? - MathOverflow
--------------------


## Why is a ring called a "ring"?

Why is a ring called "ring" (or Zahlring in German)?  There seems to (naive) me nothing more ring-like to a ring than there is to a group or a field.  I am particularly interested to learn why the word "ring" seemed appropriate to the founders.  Thanks for educating me!
- ra.rings-and-algebras
- ho.history-overview
- terminology
- 11 Several lengthy discussion of parts of this question can be found on math.SE, e.g. in this thread: math.stackexchange.com/q/61497 and the threads mentioned there. Theo Buehler – Theo Buehler 2012-12-27 00:41:17 +00:00 Commented Dec 27, 2012 at 0:41
- 4 Wikipedia has the answer. Voting to close. Felipe Voloch – Felipe Voloch 2012-12-27 00:42:13 +00:00 Commented Dec 27, 2012 at 0:42
- 6 See on mathoverflow mathoverflow.net/questions/35286/… . KConrad – KConrad 2012-12-27 01:26:48 +00:00 Commented Dec 27, 2012 at 1:26
- 3 What triggered this question was a piece by David Mumford (in "The Best Writing on Mathematics: 2012"), in which he says: "I have no idea why, but when you have any set of things that [...], mathematicians call this set a ring." Joseph O'Rourke – Joseph O'Rourke 2012-12-27 13:38:06 +00:00 Commented Dec 27, 2012 at 13:38
- 3 See also jeff560.tripod.com/r.html Zsbán Ambrus – Zsbán Ambrus 2012-12-27 17:09:57 +00:00 Commented Dec 27, 2012 at 17:09

## 3 Answers 3

First, a minor correction to the question, but it seems somewhat relevant: ring is not called 'Zahlring' in German, ring in German is 'Ring.'
As mentioned Hilbert introduced the word 'Zahlring' but also in the same sentence as synonyms 'Ring' and 'Integritätsbereich' (so ring and integral domain, resp.); see the embedded document on math.SE mentioned above; the mathematical meaning is that of a ring of algebraic integers in a number field (not necessarily the (full) one. In particular, already in that document he frequently just uses 'Ring', and defines for example 'Ringideale'.
I just browsed the first part of the 'Zahlbericht' where this happens, there seems no motivation for the name to be found, he just gives in a footnote that Dedekind calls this 'Ordnung' [order].
The idea that the name is motivated by 'circling back' might or might not be true. But I could not find any trace of it there. In particular , there seems to be no result close by regarding the fact that the powers 𝛼 𝑛 α n somehow 'circle back' to linear combinations (the idea mentioned by KConrad); also no analogy to rings of residue classes is drawn. (Of course, it is proved somewhere that such a 'ring' has a finite ℤ Z -module basis but the way this is presented does not suggest any particular 'circling back' idea.)
Hilbert's definition for ring is (paraphrasing): given a collection of algebraic integers, a ring is everything that can be written as polynomial functions with integer coefficients of this given collection. 
(As an aside, personally, I now finally understood the idea behind the name integral domain/'Integritätsbereich'; a number field is also called 'Rationalitätsbereich', so rational domain there, being everything one gets with rational functions and the integral domain is what one gets with integral functions. Added: I saw had I started to read MO earlier I could have learned this usage due to Kronecker was mentioned by KConrad on the question linked to).
He then right away comments that a 'ring' is thus closed/invariant under addition, subtraction, and multiplication.
So, perhaps it is a ring just since one does not leave it even if one moves around, say like a boxing-ring. 
Or, I quite like the idea presented earlier of 'Ring' also being used to describe (figuratively) a collection of people with a certain relation among them, a property this word shares with 'Gruppe' [group] and also 'Körper' [field, but literally body], both seem to have been established by then already. 
(Which also is somehow a partial response to why a ring is a ring even though it is not more ring-like than a group or a field; the later two already had a different name.)
Then, it seems the first axiomatisation of some notion of ring is due to Fraenkel (J. Reine Angew. Math., 1915). I stress some notion, since it does not completely match current practise in that each element is either a zero-divisor or invertible (and while non-commuativity is allowed it is only in a somewhat restricted sense in that the two products must only differ by an invertible element). The guiding example seems to be rings of integers modulo composites.
Regarding the name 'Ring' (that paper is also in German) he credits Hilbert but says there is some deviation of the meaning.
By constrast, Steinitz in his earlier axiomatization of fields (J. Reine Angew. Math., 1910) also discusses 'Integritätsbereiche' (integral domains) with exatly the axiomatization common today. 
(comm. ring, with unit, no zero-divisors).
Then to 'Moderne Algebra' (1930) by van der Waerden (based on lectures by Artin and Noether). [To be precise, I could not look at the original edition, but only some later edition, I hope this did not change over time.]
There one finds 'Ring' defined, (essentially) as is done now, as a basic notion; without any discussion of the naming. 
[To be precise, a ring there has not necessarily a multiplicative unit element and the existence of additive inverse and neutral element is expressed together via imposing solubility of 𝑎 + 𝑋 = 𝑏 a + X = b for all 𝑎 , 𝑏 a , b .]
In addition, one also finds 'Integritätsbereich' there with a different meaning than 'Ring'; namely as commutaitve ring without zero-divisors (yet not necessarily with unit element, so somewhat deviating from current usage and Steinitz).
I think one can make an argument that the structure is now called ring because it is called like that in 'Moderne Algebra', and one can note that also the naming of integral domain survived. (Except for slight deviation with unit element, but which until today is not quite uniform.)
And, it seems reasonable to assume that the naming of Artin, Noether, van der Waerden as for Franekel is directly inspired by Hilbert. After all, a ring has (just) the main properties mentioned by Hilbert for his 'rings', closed under addition, subtraction, and multiplication. What I do not know is whether there is any earlier axiomatization of ring  in (or at least closer than Fraenkel's to) the current sense. Fraenkel's
To sum it up, this is all but a 'definite' answer, but I hope it contains some relevant information. 
In my opinion, it could be difficult, possibly even impossible, to ascertain what precisely motivated the choice of name and even more so to really pin down why one name survived and another not (say, Integritätsbereich did, Rationalitätsbereich did not). It could however be interesting to research literature and in particular lecture notes, if existant, of the beginning 20th century to see the development in more detail.
Still, ring seems like a good word as there are some potential intuitions (this circling back and the residue classes), also it is short and was I think quite different from preexisting names.
- 2 Hi quid. It seems to me that the sources I give in the answer to where does the term “integral domain” come from? are somewhat relevant to your answer (bridging the gap between Hilbert and Moderne Algebra ): math.stackexchange.com/q/45945 The history of the concept of rings (as opposed to the etymology) was also discussed in this thread: math.stackexchange.com/q/362 Theo Buehler – Theo Buehler 2012-12-27 12:07:31 +00:00 Commented Dec 27, 2012 at 12:07
- @Theo Buehler: Thanks for the interesting pointer, this is interesting! I just was in the process of editing in Fraenkel and Steinitz while you commented, and did not see you comment before finalizing this. Sorry! So, I reproduced a small part of yours; but I think/hope at least Steinitz is a new piece of information. It is interesting that Noether also in 1921  does not impose unit for intergral domains. user9072 – user9072 2012-12-27 12:34:12 +00:00 Commented Dec 27, 2012 at 12:34
- To mention one very pertinent information from Theo Buehler's answer also directly here: Noether (1921) uses an axiomatization of commutative ring essentially as in use today and as in 'Moderne Algebra' (crediting Fraenkel, but mentioning the modification). The last sentence in my earlier comment was based on a too quick reading: Noether does not directly consider integral domains without unit, but uses and additional adjective, she there calls a comm. ring with unit and without zero-div a 'eigentliche Integritätsbereich' (so something like proper inetegral domains). user9072 – user9072 2012-12-27 13:17:09 +00:00 Commented Dec 27, 2012 at 13:17
- 3 @quid: Thanks for this remarkably erudite answer!  I especially like your explanation "why a ring is a ring even though it is not more ring-like than a group or a field; the later two already had a different name."  This makes perfect sense to me. We all create names for our mathematical constructs, and often the best names are already "taken," forcing us to perhaps slightly misname. Joseph O'Rourke – Joseph O'Rourke 2012-12-27 13:44:08 +00:00 Commented Dec 27, 2012 at 13:44
- @Joseph O'Rourke: You are welcome, and thank you for the kind words! user9072 – user9072 2012-12-28 12:43:49 +00:00 Commented Dec 28, 2012 at 12:43
Ring is also an outdated German word for association or coalition - there is probably a better translation, but it means something along those lines. I would guess Hilbert was thinking of this meaning of the word, not the round shiny object usually seen on fingers.
There is also the word Verband for some algebraic structure here for which I do not know the english name, but this notion probably predates ring. A Verband is also a word for association; nowadays, its mainly used in sports - FIFA, UEFA, IOC are Verbände (to increase the confusion, Verband is also the German word for bandage). One might speculate that Hilbert looked for a similar, but different word to describe a similar, but different algebraic structure.
- 5 "Ring" has this meaning in English sometimes as well, e.g., a spy ring.  So does "circle," e.g., circle of friends, social circle. Timothy Chow – Timothy Chow 2012-12-28 02:27:56 +00:00 Commented Dec 28, 2012 at 2:27
- 1 Verband, that's an interesting additional example. The English name for 'Verband' (in the math sense) is lattice (in the order, not geometry sense, the latter would be 'Gitter'). [BTW, an efficient way to find such info is indeed Wikipedia, just change the language on the respective page.] While I mentioned it in passing myself, I did not fully appreciate this at that moment. The more I think about it the more this interpretation makes sense to me. It fits also better with the idea (there predominant IMO) as thinking of a ring as a certain collection of numbers,... user9072 – user9072 2012-12-28 12:49:59 +00:00 Commented Dec 28, 2012 at 12:49
- ...as opposed to an object in its own right, and a ring then as a physical object often would even be something quite monolithic. user9072 – user9072 2012-12-28 12:56:12 +00:00 Commented Dec 28, 2012 at 12:56
- "Korper" (the original word for what English-speakers call a "field") can also be used to signify a group of people; and in English too one speaks of a "governing body". I think all these coinages were intended to suggest assemblages of individuals. James Propp – James Propp 2024-02-16 23:43:44 +00:00 Commented Feb 16, 2024 at 23:43
I think the classical argument is that the original rings were Z/nZ, which as you'll remember from “clock arithmetic” has a certain cyclicity to it. This theory is backed up by Wikipedia ( https://en.wikipedia.org/wiki/Ring_(mathematics)#History ) citing Harvey Cohn's number theory book with
According to Harvey Cohn, Hilbert used the term for a specific ring that had the property of "circling directly back" to an element of itself.
(citation from the Wikipedia page as of 26th December 2012)
The Hilbert paper in question is Die Theorie der algebraischen Zahlkörper (Jahresbericht der Deutschen Mathematiker Vereinigung, Vol. 4, 1897), credited with introducing the word Zahlring in the first place.
- 1 I personally find this argument hard to believe. If that is the main idea, why is ℂ [ 𝑇 ] C [ T ] a ring too? I don't think this is entirely inaccurate, but I think there is some more to be said about this... François G. Dorais – François G. Dorais 2012-12-27 03:45:01 +00:00 Commented Dec 27, 2012 at 3:45
- 6 He's not postulating that this physical cyclicity is the main idea in the definition of a ring. He's postulating that it motivated the choice of the word "ring", at a time when few examples had yet been studied. Greg Martin – Greg Martin 2012-12-27 07:38:22 +00:00 Commented Dec 27, 2012 at 7:38
- 8 It should however be noted that Hilbert did not call Z/nZ a ring, but strictly only rings of algebraic integers, where admittedly there is too some 'circularity', but at least in his presentation this does not really shine through that much. user9072 – user9072 2012-12-27 10:39:23 +00:00 Commented Dec 27, 2012 at 10:39

## You must log in to answer this question.

Start asking to get answers
Find the answer to your question by asking.
Explore related questions
- ra.rings-and-algebras
- ho.history-overview
- terminology
See similar questions with these tags.
- Featured on Meta
- AI Assist: recent updates (January 2026)
- Community Engagement Across the Network: Focus for 2026
- Citation Helper v2 - User Script edition!

--------------------