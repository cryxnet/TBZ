
## Funktionsweise
1. **Farbraumkonvertierung**: Zunächst wird das Eingangsbild vom RGB-Farbraum in den YCbCr-Farbraum umgewandelt. Dabei werden die Helligkeitsinformationen (Y) und die Farbdifferenzinformationen (Cb und Cr) getrennt.   
2. **Unterteilung in Blöcke**: Das Bild wird in kleine 8x8-Blöcke aufgeteilt. Jeder Block enthält Informationen über die Helligkeit und Farbunterschiede.
3. **Diskrete Kosinustransformation (DCT)**: Für jeden 8x8-Block wird eine DCT durchgeführt. Dies bedeutet, dass die Blockdaten in den Frequenzbereich umgewandelt werden. Die DCT erzeugt Koeffizienten, die die Beiträge der verschiedenen Frequenzen im Block darstellen.
4. **Quantisierung**: Die DCT-Koeffizienten werden quantisiert, indem sie durch vordefinierte Quantisierungstabellen geteilt werden. Dadurch werden die weniger signifikanten Koeffizienten aufgerundet oder auf Null gesetzt. Die Quantisierung führt zu einer deutlichen Reduzierung der Datenmenge.
5. **Huffman-Codierung**: Die quantisierten Koeffizienten werden Huffman-codiert. Dabei werden häufig auftretende Koeffizienten mit kurzen Bitfolgen codiert, während seltene Koeffizienten längere Bitfolgen erhalten. Dies ermöglicht eine effiziente Darstellung der Daten.

## Probleme: Artefakte
- **Blockartefakte**: Bei starken Kompressionsraten können die 8x8-Blöcke sichtbare Kanten oder Muster erzeugen. Dies tritt auf, weil Informationen innerhalb der Blöcke verloren gehen und das Auge die Diskontinuitäten wahrnimmt.
- **Farbartefakte**: Die Farbunterschiede (Cb und Cr) werden bei der Quantisierung stärker komprimiert als die Helligkeitsinformationen (Y). Dadurch können ungenaue Farbwerte und sichtbare Farbverzerrungen auftreten.
- **Ringartefakte**: In Bereichen mit starken Farbübergängen können sogenannte "Ringartefakte" auftreten. Dies äußert sich in Form von unerwünschten Ringen oder Wellen, die um kontrastreiche Kanten herum sichtbar sind.