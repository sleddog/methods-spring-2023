import { fizzbuzz } from '/main'

describe('testing fizzbuzz', () => {
  test('multiples of 3 print fizz', () => {
    expect(fizzbuzz(3).toMatch('fizz'));
  });
  test('multiples of 5 print buzz', () => {
    expect(fizzbuzz(5).toMatch('buzz'));
  });
  test('multiples of 7 print ping', () => {
    expect(fizzbuzz(7).toMatch('ping'));
  });
  test('multiples of 11 print pong', () => {
    expect(fizzbuzz(11).toMatch('pong'));
  });
  test('multiples of 15 print fizzbuzz', () => {
    expect(fizzbuzz(15).toMatch('fizzbuzz'));
  });
  test('multiples of 77 print pingpong', () => {
    expect(fizzbuzz(77).toMatch('pingpong'));
  });
  test('multiples of 1155 print fizzbuzzpingpong', () => {
    expect(fizzbuzz(1155).toMatch('fizzbuzzpingpong'));
  });
});
