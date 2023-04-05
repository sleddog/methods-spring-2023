import { fizzbuzz } from '../fizzbuzz/typescript/Skeegan123'

describe('testing fizzbuzz', () => {
  test('multiples of 3 print fizz', () => {
    expect(fizzbuzz(3).toBe(0));
  });
});

