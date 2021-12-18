import sys
print("state query")
print("\N{CSI}1$w",end="", flush=True)
print()
print("pos query")
print("\N{CSI}6n",end="", flush=True)
print()

print("P1;1;1;0;0;2;0;0{P???owYn||~ywo??/?IRJaVNn^NVbJRI\\")
print("!(P!!")
print("creating font", flush=True)
# print("\N{DCS}1;1;0;10;1;1;16;0{ @??@@BBBB??/?]~'@@~~'?/???___??_?;\N{ST}")
print("\N{DCS}1;1;0;12;1;1;12;0{ @-------/--------/--------;????????/????????/????????;~@@@@@@~/~??????~/~GGGGGG~;TTTTTTTT/TTTTTTTT/TTTTTTTT;\N{ST}")
print("designating font")
#print("\N{ESC}* @F")
print("\N{ESC}) @")
print("using font")
print("\N{SI}", end="")
for i in range(32, 127):
    print(chr(i), end="")
print("\n\N{SO}", end="")
for i in range(32, 127):
    print(chr(i), end="")
print("\n\N{ESC}n", end="")
for i in range(32, 127):
    print(chr(i), end="")
print("\n\N{ESC}o", end="")
for i in range(32, 127):
    print(chr(i), end="")
print("\n\N{SI}")

print("done")
