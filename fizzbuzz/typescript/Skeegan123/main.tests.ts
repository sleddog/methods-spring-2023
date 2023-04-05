import { fizzbuzz } from '../fizzbuzz/typescript/Skeegan123'

describe('testing fizzbuzz', () => {
  test('multiples of 3 print fizz', () => {
    expect(fizzbuzz(3).toBe(0));
  });
  test('multiples of 5 print buzz', () => {
    expect(fizzbuzz(5).toBe(0));
  });
  test('multiples of 7 print ping', () => {
    expect(fizzbuzz(7).toBe(0));
  });
  test('multiples of 11 print pong', () => {
    expect(fizzbuzz(11).toBe(0));
  });
  test('multiples of 15 print fizzbuzz', () => {
    expect(fizzbuzz(15).toBe(0));
  });
  test('multiples of 77 print pingpong', () => {
    expect(fizzbuzz(77).toBe(0));
  });
  test('multiples of 1155 print fizzbuzzpingpong', () => {
    expect(fizzbuzz(1155).toBe(0));
  });
});
