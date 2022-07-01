/**
 * Dezimalkonverter
 *
 * Konvertiert eine Dezimalzahl in eine Binärzahl.
 *
 * Komplexität: O(log n)
 */

const decimalToBinary = (value: number): string => {
  if (value < 1) {
    return "";
  }
  return decimalToBinary(Math.floor(value / 2)) + (value % 2);
};

const result = decimalToBinary(182);
console.log(`Binary: ${result}`);
export {};
