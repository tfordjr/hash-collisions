I've grabbed a bunch of .txt files of Harry Potter books from github, and compiled
them all into "HP Books.txt". This file is 83,264 lines of text or 6.4MB. Many of those 
those are newlines, and there are some other repeated lines, so those hash values have 
collisions of course because they originate from the same text, but for the likely over
50,000 lines of unique text there hasn't been a single hash collision. 

This absence of collisions is expected becuase SHA-256 is collision resistant. 
Each hash is 64 hexadecimal characters long, and with 16 options per character, that makes
16^64 = 1.1579209e+77 total possible hash values. That's over 1 quattuorvigintillion 
possible hash values. 

My computer which sports an i7-7700 was able to generate 83,264 hashes and compare them
in 200 milliseconds, and I was unable to find any hash collisions. For me to actually find
hash collisions by random chance using SHA-256 we will have to look to the Birthday 
Paradox to find how many of the possible hash values we must generate to find a collision.

I've also submitted birthday-paradox.py to express this. Without the birthday paradox, we
might assume we'd have to generate 16^64 or 1.15e+77 hashes to find a match, but that's 
actually the odds to find a match on a specific hash or vanity hash on average. But the
birthday paradox shows us that we need only generate about 4.01e+37 hashes on average to 
find a collision by brute force of any two hashes generated. 

If my computer accomplished 83,264 hashes in 200 ms, that's 416,320 hashes per second.
4.01e+37/416,320 = 9.64e+7 seconds = approx 10^8 seconds = approx 1200 days
So it would take my meager computer about four years on average of generating unique 
hashes before it could brute force a single collision in SHA-256. 

