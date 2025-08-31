import Pricing from './4-pricing.js';
import Currency from './3-currency.js';

test('Pricing displays full price', () => {
  const euro = new Currency('EUR', 'Euro');
  const price = new Pricing(100, euro);
  expect(price.displayFullPrice()).toBe('100 Euro (EUR)');
});

test('Pricing converts price', () => {
  expect(Pricing.convertPrice(10, 2)).toBe(20);
});
