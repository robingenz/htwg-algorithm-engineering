/**
 * Binomialkoeffizient
 *
 * Berechnet den Binomialkoeffizienten aus n und k.
 *
 * Komplexität: O(n^2)
 */

const binomial = (n: number, k: number): number => {
  if (k === 0 || k === n) {
    return 1;
  }
  return binomial(n - 1, k) + binomial(n - 1, k - 1);
};

const result = binomial(49, 6);
console.log(`Result: ${result}`);
export {};
