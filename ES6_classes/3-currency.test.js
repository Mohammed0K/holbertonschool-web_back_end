import Currency from './3-currency.js';

test('Currency displays correctly', () => {
  const dollar = new Currency('USD', 'Dollars');
  expect(dollar.displayFullCurrency()).toBe('Dollars (USD)');
});
