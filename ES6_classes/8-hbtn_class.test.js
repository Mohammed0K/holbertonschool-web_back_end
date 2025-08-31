import HolbertonClass from './8-hbtn_class.js';

test('HolbertonClass returns size as number and location as string', () => {
  const hc = new HolbertonClass(12, 'San Francisco');
  expect(+hc).toBe(12);             // number
  expect(`${hc}`).toBe('San Francisco'); // string
});
