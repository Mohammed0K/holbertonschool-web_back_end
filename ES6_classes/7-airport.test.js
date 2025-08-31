import Airport from './7-airport.js';

test('Airport toString works correctly', () => {
  const a = new Airport('Los Angeles International Airport', 'LAX');
  expect(String(a)).toBe('[object LAX]');
});
