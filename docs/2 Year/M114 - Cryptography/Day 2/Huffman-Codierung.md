![](../../../_assets/Pasted%20image%2020230601154327.png)
> https://www.youtube.com/watch?v=eSlpTPXbhYw

Angenommen, wir haben den folgenden Text: "BAUMGARTEN".

Schritt 1: Häufigkeitsanalyse
Wir zählen die Häufigkeit jedes Zeichens im Text:

A: 2-mal
B: 1-mal
M: 1-mal
G: 1-mal
R: 1-mal
T: 1-mal
E: 1-mal
N: 1-mal

Schritt 2: Erstellung des Huffman-Baums
Wir erstellen einen Huffman-Baum, indem wir die Zeichen und ihre Häufigkeiten berücksichtigen:

![](../../../_assets/Pasted%20image%2020230601154357.png)
Schritt 3: Codierung
Die Codierung erfolgt, indem man den Huffman-Baum durchläuft und jedem Zeichen ein Codewort zuweist:

A: 10
B: 1110
M: 1100
G: 1101
R: 010
T: 011
E: 000
N: 001

Schritt 4: Codierung der Daten
Wir verwenden die erhaltenen Codewörter, um die ursprünglichen Daten zu codieren. Der ursprüngliche Text "BAUMGARTEN" wird folgendermaßen codiert:

Codierung: 001000111011011101111011111110

Die Huffman-Codierung ermöglicht eine effiziente Komprimierung, da häufige Zeichen mit kürzeren Codewörtern codiert werden. Bei der Dekodierung wird der Huffman-Baum verwendet, um die codierten Daten in den ursprünglichen Text zurückzuwandeln, indem die Codewörter sequenziell abgeglichen werden.
